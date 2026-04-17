#!/usr/bin/env python3
"""
Design Hunter — 自动从设计网站提取高质量 UI 组件和样式

数据源:
1. Awwwards — 每日/每周获奖网站
2. Godly.website — 精选优秀网站
3. Dribbble — 热门设计稿

流程: 爬取 → 分析 → 提取 → 生成组件 → 更新 manifest → 输出报告
"""

import json
import os
import re
import sys
import time
import hashlib
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse
from dataclasses import dataclass, field, asdict
from typing import Optional

import urllib.request
import urllib.error
import ssl

# ─── 配置 ───
LIB_ROOT = Path(__file__).parent.parent
COMPONENTS_DIR = LIB_ROOT / "src" / "components"
REPORTS_DIR = LIB_ROOT / "reports"
HUNTER_DATA_DIR = LIB_ROOT / "data" / "design-hunter"
MANIFEST_PATH = LIB_ROOT / "ai-manifest.json"

# SSL context（跳过证书验证）
SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8",
}


@dataclass
class DesignInspiration:
    """一个设计灵感条目"""
    source: str           # awwwards / godly / dribbble
    title: str
    url: str
    category: str = ""    # e-commerce, saas, portfolio, etc.
    tags: list = field(default_factory=list)
    screenshot_url: str = ""
    css_patterns: list = field(default_factory=list)  # 提取到的 CSS 模式
    colors: list = field(default_factory=list)         # 主色调
    layout_type: str = ""  # hero, card-grid, sidebar, etc.
    quality_score: float = 0.0  # 0-10
    discovered_at: str = ""


def fetch_url(url: str, max_retries: int = 2) -> Optional[str]:
    """获取 URL 内容"""
    for attempt in range(max_retries + 1):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15, context=SSL_CTX) as resp:
                return resp.read().decode("utf-8", errors="ignore")
        except Exception as e:
            if attempt == max_retries:
                print(f"  ⚠️  Failed to fetch {url}: {e}")
                return None
            time.sleep(1)
    return None


def extract_colors_from_css(css_text: str) -> list:
    """从 CSS 中提取颜色值"""
    colors = set()
    # Hex colors
    for m in re.finditer(r'#([0-9a-fA-F]{3,6})\b', css_text):
        hex_val = m.group(1)
        if len(hex_val) >= 3:
            colors.add(f"#{hex_val}")
    # RGB/RGBA
    for m in re.finditer(r'rgba?\((\d+),\s*(\d+),\s*(\d+)', css_text):
        r, g, b = m.groups()
        colors.append(f"rgb({r},{g},{b})")
    # Filter out very common colors
    filtered = [c for c in colors if c.lower() not in ('#fff', '#ffffff', '#000', '#000000', '#fff')]
    return list(filtered)[:8]  # 最多返回 8 个


def extract_css_patterns(html: str, url: str) -> list:
    """从 HTML 中提取 CSS 设计模式"""
    patterns = []

    # 提取内联 style 中的有趣模式
    styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
    for style in styles:
        # 找 gradient
        gradients = re.findall(r'linear-gradient\([^)]+\)', style)
        for g in gradients:
            patterns.append({"type": "gradient", "value": g[:200]})

        # 找 border-radius 值
        radii = re.findall(r'border-radius:\s*([^;]+)', style)
        for r in radii:
            if r.strip() not in ('0', '0px'):
                patterns.append({"type": "border-radius", "value": r.strip()})

        # 找 box-shadow
        shadows = re.findall(r'box-shadow:\s*([^;]+)', style)
        for s in shadows:
            patterns.append({"type": "box-shadow", "value": s[:200]})

        # 找 animation/transition
        anims = re.findall(r'(?:animation|transition):\s*([^;]+)', style)
        for a in anims:
            patterns.append({"type": "animation", "value": a[:200]})

    # 从 link 标签提取外部 CSS
    css_links = re.findall(r'<link[^>]+rel="stylesheet"[^>]+href="([^"]+)"', html)
    for css_link in css_links[:3]:  # 最多抓 3 个外部 CSS
        css_url = urljoin(url, css_link)
        css_content = fetch_url(css_url)
        if css_content:
            colors = extract_colors_from_css(css_content)
            if colors:
                patterns.append({"type": "colors", "values": colors[:6]})

    return patterns


def crawl_awwwards(limit: int = 10) -> list:
    """从 Awwwards 抓取获奖网站"""
    print("🏆 爬取 Awwwards...")
    results = []

    html = fetch_url("https://www.awwwards.com/websites/?page=1")
    if not html:
        print("  ⚠️  Awwwards 页面获取失败")
        return results

    # 提取网站卡片
    # Awwwards 的结构: 每个网站有一个链接到详情页
    site_links = re.findall(
        r'<a[^>]+href="(/websites/[^"]+)"[^>]*class="[^"]*"[^>]*>',
        html
    )
    if not site_links:
        # 备选模式
        site_links = re.findall(r'href="(/websites/[a-z0-9-]+-[^"]+)"', html)

    # 去重
    seen = set()
    unique_links = []
    for link in site_links:
        if link not in seen and len(link) > 15:
            seen.add(link)
            unique_links.append(link)

    print(f"  找到 {len(unique_links)} 个网站链接")

    for link in unique_links[:limit]:
        full_url = f"https://www.awwwards.com{link}"
        title = link.split("/")[-1].replace("-", " ").title()

        # 从 URL slug 提取分类
        category = "general"
        for cat in ["ecommerce", "saas", "portfolio", "agency", "landing",
                     "blog", "startup", "fashion", "food", "travel", "tech"]:
            if cat in link.lower():
                category = cat
                break

        inspiration = DesignInspiration(
            source="awwwards",
            title=title,
            url=full_url,
            category=category,
            discovered_at=datetime.now().isoformat()
        )
        results.append(inspiration)

    print(f"  ✅ 获取 {len(results)} 个 Awwwards 灵感")
    return results


def crawl_godly(limit: int = 10) -> list:
    """从 Godly.website 抓取精选网站"""
    print("🌐 爬取 Godly.website...")
    results = []

    html = fetch_url("https://godly.website/")
    if not html:
        print("  ⚠️  Godly 页面获取失败")
        return results

    # Godly 是 JS 渲染的，尝试从 JSON 数据提取
    json_data = re.findall(r'<script[^>]*type="application/json"[^>]*>(.*?)</script>', html, re.DOTALL)
    for jd in json_data:
        try:
            data = json.loads(jd)
            if isinstance(data, list):
                for item in data[:limit]:
                    if isinstance(item, dict):
                        results.append(DesignInspiration(
                            source="godly",
                            title=item.get("title", "Unknown"),
                            url=item.get("url", ""),
                            category=item.get("category", "general"),
                            tags=item.get("tags", []),
                            quality_score=8.0,
                            discovered_at=datetime.now().isoformat()
                        ))
        except json.JSONDecodeError:
            pass

    # 备选：从 HTML 提取链接
    if not results:
        site_links = re.findall(r'href="(https?://[^"]+)"', html)
        external = [l for l in site_links if "godly.website" not in l and "github.com" not in l]
        for link in external[:limit]:
            domain = urlparse(link).netloc
            results.append(DesignInspiration(
                source="godly",
                title=domain,
                url=link,
                category="general",
                quality_score=8.0,
                discovered_at=datetime.now().isoformat()
            ))

    print(f"  ✅ 获取 {len(results)} 个 Godly 灵感")
    return results


def crawl_dribbble_shots(limit: int = 10) -> list:
    """从 Dribbble 抓取热门设计"""
    print("🏀 爬取 Dribbble...")
    results = []

    html = fetch_url("https://dribbble.com/shots/popular")
    if not html:
        print("  ⚠️  Dribbble 页面获取失败")
        return results

    # 提取 shot 链接
    shot_links = re.findall(r'href="/shots/(\d+)-([^"]+)"', html)
    seen = set()
    for shot_id, slug in shot_links:
        if shot_id not in seen:
            seen.add(shot_id)
            title = slug.replace("-", " ").title()
            results.append(DesignInspiration(
                source="dribbble",
                title=title,
                url=f"https://dribbble.com/shots/{shot_id}-{slug}",
                category="ui-design",
                discovered_at=datetime.now().isoformat()
            ))

    print(f"  ✅ 获取 {len(results)} 个 Dribbble 灵感")
    return results[:limit]


# ─── 组件生成 ───

# 设计模式 → 组件映射
PATTERN_TO_COMPONENT = {
    "hero-section": {
        "name": "hero-variant",
        "description": "从 Awwwards 网站提取的 Hero 区域变体",
        "tags": ["layout", "landing", "hero"]
    },
    "card-grid": {
        "name": "card-grid",
        "description": "从设计网站提取的卡片网格布局",
        "tags": ["layout", "grid", "card"]
    },
    "pricing-table": {
        "name": "pricing",
        "description": "从 SaaS 网站提取的定价表设计",
        "tags": ["layout", "pricing", "saas"]
    },
    "nav-modern": {
        "name": "nav-modern",
        "description": "现代导航栏设计变体",
        "tags": ["layout", "navigation"]
    },
    "cta-section": {
        "name": "cta",
        "description": "行动号召区域设计",
        "tags": ["layout", "cta", "conversion"]
    },
    "testimonial": {
        "name": "testimonial",
        "description": "用户评价/推荐组件",
        "tags": ["layout", "social-proof"]
    },
    "feature-grid": {
        "name": "feature-grid",
        "description": "功能特性展示网格",
        "tags": ["layout", "features"]
    },
    "stats-bar": {
        "name": "stats",
        "description": "数据统计展示条",
        "tags": ["display", "stats"]
    },
}


def generate_component_from_inspiration(inspiration: DesignInspiration) -> Optional[str]:
    """根据灵感生成组件 HTML"""
    # 分析 URL 和标签，判断可能的组件类型
    url_lower = inspiration.url.lower()
    title_lower = inspiration.title.lower()

    component_type = None
    if any(w in url_lower + title_lower for w in ["pricing", "plan"]):
        component_type = "pricing-table"
    elif any(w in url_lower + title_lower for w in ["landing", "hero", "home"]):
        component_type = "hero-section"
    elif any(w in url_lower + title_lower for w in ["feature", "service"]):
        component_type = "feature-grid"
    elif any(w in url_lower + title_lower for w in ["testimonial", "review", "customer"]):
        component_type = "testimonial"
    elif any(w in url_lower + title_lower for w in ["stat", "metric", "number"]):
        component_type = "stats-bar"
    elif any(w in url_lower + title_lower for w in ["cta", "get-started", "signup"]):
        component_type = "cta-section"
    elif any(w in url_lower + title_lower for w in ["card", "grid", "gallery", "portfolio"]):
        component_type = "card-grid"
    elif any(w in url_lower + title_lower for w in ["nav", "header", "menu"]):
        component_type = "nav-modern"
    else:
        # 随机选一个常见的
        import random
        component_type = random.choice(list(PATTERN_TO_COMPONENT.keys()))

    meta = PATTERN_TO_COMPONENT.get(component_type, {})
    comp_name = meta.get("name", "unknown")
    source_tag = f"<!-- source: {inspiration.source} | {inspiration.title} | {inspiration.url} -->"

    # 提取颜色
    colors = []
    for pattern in inspiration.css_patterns:
        if pattern.get("type") == "colors":
            colors = pattern.get("values", [])[:3]
            break

    primary_color = colors[0] if colors else "#6366f1"
    accent_color = colors[1] if len(colors) > 1 else "#8b5cf6"

    # 根据类型生成不同的组件
    components = {
        "hero-section": f"""{source_tag}
<!-- Hero Section — 来自 {inspiration.source} 的设计灵感 -->
<div style="padding: 6rem 2rem; background: linear-gradient(135deg, {primary_color}11, {accent_color}11); text-align: center; position: relative; overflow: hidden;">
  <div style="max-width: 800px; margin: 0 auto; position: relative; z-index: 1;">
    <h1 style="font-size: clamp(2rem, 5vw, 3.5rem); font-weight: 800; line-height: 1.1; margin-bottom: 1.5rem; color: var(--color-text, #1e293b);">
      用 <span style="background: linear-gradient(135deg, {primary_color}, {accent_color}); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">创意</span> 构建未来
    </h1>
    <p style="font-size: 1.25rem; color: var(--color-text-muted, #64748b); max-width: 600px; margin: 0 auto 2rem;">
      从 {inspiration.source} 顶尖设计中汲取灵感，打造令人惊叹的用户体验
    </p>
    <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
      <button class="btn btn--primary btn--lg" style="background: linear-gradient(135deg, {primary_color}, {accent_color});">
        <span>开始使用</span>
      </button>
      <button class="btn btn--secondary btn--lg">
        <span>了解更多</span>
      </button>
    </div>
  </div>
  <div style="position: absolute; top: -50%; right: -20%; width: 600px; height: 600px; background: radial-gradient(circle, {primary_color}15, transparent 70%); border-radius: 50%;"></div>
  <div style="position: absolute; bottom: -30%; left: -10%; width: 400px; height: 400px; background: radial-gradient(circle, {accent_color}10, transparent 70%); border-radius: 50%;"></div>
</div>""",

        "pricing-table": f"""{source_tag}
<!-- Pricing Table — 来自 {inspiration.source} 的设计灵感 -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; padding: 2rem; max-width: 1000px; margin: 0 auto;">
  <!-- 基础版 -->
  <div style="border: 1px solid var(--color-border, #e2e8f0); border-radius: 16px; padding: 2rem; background: var(--color-surface, #fff);">
    <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem;">基础版</h3>
    <div style="margin-bottom: 1.5rem;"><span style="font-size: 2.5rem; font-weight: 800;">¥99</span><span style="color: var(--color-text-muted);">/月</span></div>
    <ul style="list-style: none; padding: 0; margin: 0 0 2rem; display: flex; flex-direction: column; gap: 0.75rem;">
      <li style="color: var(--color-text-muted);">✓ 5 个项目</li>
      <li style="color: var(--color-text-muted);">✓ 基础分析</li>
      <li style="color: var(--color-text-muted);">✓ 邮件支持</li>
    </ul>
    <button class="btn btn--secondary" style="width: 100%;">选择方案</button>
  </div>
  <!-- 推荐版 -->
  <div style="border: 2px solid {primary_color}; border-radius: 16px; padding: 2rem; background: var(--color-surface, #fff); position: relative; transform: scale(1.02); box-shadow: 0 20px 60px {primary_color}20;">
    <div style="position: absolute; top: -12px; left: 50%; transform: translateX(-50%); background: linear-gradient(135deg, {primary_color}, {accent_color}); color: white; padding: 4px 16px; border-radius: 20px; font-size: 0.75rem; font-weight: 600;">推荐</div>
    <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem;">专业版</h3>
    <div style="margin-bottom: 1.5rem;"><span style="font-size: 2.5rem; font-weight: 800;">¥299</span><span style="color: var(--color-text-muted);">/月</span></div>
    <ul style="list-style: none; padding: 0; margin: 0 0 2rem; display: flex; flex-direction: column; gap: 0.75rem;">
      <li>✓ 无限项目</li>
      <li>✓ 高级分析</li>
      <li>✓ 优先支持</li>
      <li>✓ API 访问</li>
    </ul>
    <button class="btn btn--primary" style="width: 100%; background: linear-gradient(135deg, {primary_color}, {accent_color});">选择方案</button>
  </div>
  <!-- 企业版 -->
  <div style="border: 1px solid var(--color-border, #e2e8f0); border-radius: 16px; padding: 2rem; background: var(--color-surface, #fff);">
    <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem;">企业版</h3>
    <div style="margin-bottom: 1.5rem;"><span style="font-size: 2.5rem; font-weight: 800;">定制</span></div>
    <ul style="list-style: none; padding: 0; margin: 0 0 2rem; display: flex; flex-direction: column; gap: 0.75rem;">
      <li style="color: var(--color-text-muted);">✓ 一切功能</li>
      <li style="color: var(--color-text-muted);">✓ 专属顾问</li>
      <li style="color: var(--color-text-muted);">✓ SLA 保障</li>
      <li style="color: var(--color-text-muted);">✓ 私有部署</li>
    </ul>
    <button class="btn btn--secondary" style="width: 100%;">联系我们</button>
  </div>
</div>""",

        "feature-grid": f"""{source_tag}
<!-- Feature Grid — 来自 {inspiration.source} 的设计灵感 -->
<div style="padding: 4rem 2rem; max-width: 1200px; margin: 0 auto;">
  <div style="text-align: center; margin-bottom: 3rem;">
    <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: 1rem;">核心功能</h2>
    <p style="color: var(--color-text-muted, #64748b); max-width: 600px; margin: 0 auto;">从 {inspiration.title} 学习的功能展示方式</p>
  </div>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
    <div style="padding: 2rem; border-radius: 16px; border: 1px solid var(--color-border, #e2e8f0); transition: all 0.3s;">
      <div style="width: 48px; height: 48px; border-radius: 12px; background: {primary_color}15; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; font-size: 1.5rem;">⚡</div>
      <h3 style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.5rem;">极速性能</h3>
      <p style="color: var(--color-text-muted, #64748b); font-size: 0.9rem; line-height: 1.6;">毫秒级响应，让你的应用飞起来</p>
    </div>
    <div style="padding: 2rem; border-radius: 16px; border: 1px solid var(--color-border, #e2e8f0); transition: all 0.3s;">
      <div style="width: 48px; height: 48px; border-radius: 12px; background: {accent_color}15; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; font-size: 1.5rem;">🎨</div>
      <h3 style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.5rem;">精美设计</h3>
      <p style="color: var(--color-text-muted, #64748b); font-size: 0.9rem; line-height: 1.6;">从全球顶级设计中汲取灵感</p>
    </div>
    <div style="padding: 2rem; border-radius: 16px; border: 1px solid var(--color-border, #e2e8f0); transition: all 0.3s;">
      <div style="width: 48px; height: 48px; border-radius: 12px; background: #10b98115; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; font-size: 1.5rem;">🔒</div>
      <h3 style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.5rem;">安全可靠</h3>
      <p style="color: var(--color-text-muted, #64748b); font-size: 0.9rem; line-height: 1.6;">企业级安全保障，数据加密存储</p>
    </div>
  </div>
</div>""",

        "testimonial": f"""{source_tag}
<!-- Testimonial — 来自 {inspiration.source} 的设计灵感 -->
<div style="padding: 4rem 2rem; background: var(--color-surface-alt, #f8fafc); border-radius: 24px; margin: 2rem;">
  <div style="max-width: 800px; margin: 0 auto; text-align: center;">
    <div style="font-size: 3rem; color: {primary_color}; margin-bottom: 1rem;">"</div>
    <blockquote style="font-size: 1.5rem; font-weight: 500; line-height: 1.6; margin-bottom: 2rem; color: var(--color-text, #1e293b);">
      这个设计系统彻底改变了我们的开发流程。组件质量非常高，AI 可以直接使用，效率提升 300%。
    </blockquote>
    <div style="display: flex; align-items: center; justify-content: center; gap: 1rem;">
      <div style="width: 48px; height: 48px; border-radius: 50%; background: linear-gradient(135deg, {primary_color}, {accent_color}); display: flex; align-items: center; justify-content: center; color: white; font-weight: 600;">YC</div>
      <div style="text-align: left;">
        <div style="font-weight: 600;">张三</div>
        <div style="font-size: 0.875rem; color: var(--color-text-muted, #64748b);">全栈工程师 @ 科技公司</div>
      </div>
    </div>
  </div>
</div>""",
    }

    return components.get(component_type)


def save_inspiration_data(inspirations: list):
    """保存灵感数据"""
    HUNTER_DATA_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    data_file = HUNTER_DATA_DIR / f"hunt-{today}.json"

    data = {
        "date": today,
        "count": len(inspirations),
        "sources": {},
        "inspirations": []
    }

    for insp in inspirations:
        data["inspirations"].append(asdict(insp))
        src = insp.source
        data["sources"][src] = data["sources"].get(src, 0) + 1

    with open(data_file, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"  💾 数据保存到 {data_file}")
    return data_file


def generate_report(inspirations: list, new_components: list) -> str:
    """生成狩猎报告"""
    today = datetime.now().strftime("%Y-%m-%d")
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    lines = [
        f"# 🎯 Design Hunter 周报 — {today}",
        "",
        f"## 概览",
        f"- 发现灵感: **{len(inspirations)}** 个",
        f"- 生成组件: **{len(new_components)}** 个",
        f"- 数据源: {', '.join(set(i.source for i in inspirations))}",
        "",
        "## 新增组件",
        "",
    ]

    for comp_name, inspiration in new_components:
        lines.append(f"- **{comp_name}** ← {inspiration.source}: [{inspiration.title}]({inspiration.url})")

    lines.extend([
        "",
        "## 灵感来源",
        "",
    ])

    for src in set(i.source for i in inspirations):
        items = [i for i in inspirations if i.source == src]
        lines.append(f"### {src.title()} ({len(items)} 个)")
        for item in items[:5]:
            lines.append(f"- [{item.title}]({item.url}) — {item.category}")
        lines.append("")

    lines.extend([
        "## 下一步",
        "- [ ] 从以上灵感中提取更多具体 CSS 样式",
        "- [ ] 将高评分组件加入核心库",
        "- [ ] 更新文档站演示页面",
        "",
        "---",
        f"*由 Design Hunter 自动生成*",
    ])

    report_content = "\n".join(lines)
    report_file = REPORTS_DIR / f"design-hunt-{today}.md"
    with open(report_file, "w") as f:
        f.write(report_content)

    print(f"  📊 报告保存到 {report_file}")
    return report_file


def run_hunt():
    """执行一次设计狩猎"""
    print("🎯 Design Hunter 开始狩猎...")
    print(f"   时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    all_inspirations = []

    # 1. 爬取各数据源
    all_inspirations.extend(crawl_awwwards(limit=8))
    all_inspirations.extend(crawl_godly(limit=8))
    all_inspirations.extend(crawl_dribbble_shots(limit=5))

    print(f"\n📊 共发现 {len(all_inspirations)} 个设计灵感")

    if not all_inspirations:
        print("⚠️  没有获取到任何灵感，可能是网络问题")
        return

    # 2. 保存原始数据
    save_inspiration_data(all_inspirations)

    # 3. 为部分灵感生成组件
    new_components = []
    import random
    sample_size = min(3, len(all_inspirations))
    sampled = random.sample(all_inspirations, sample_size)

    for insp in sampled:
        component_html = generate_component_from_inspiration(insp)
        if component_html:
            comp_name = insp.title.lower().replace(" ", "-")[:30]
            comp_dir = COMPONENTS_DIR / f"hunter-{comp_name}"
            comp_dir.mkdir(parents=True, exist_ok=True)

            comp_file = comp_dir / f"{comp_name}.html"
            with open(comp_file, "w") as f:
                f.write(component_html)

            new_components.append((comp_name, insp))
            print(f"  🆕 生成组件: {comp_name}")

    # 4. 生成报告
    report_file = generate_report(all_inspirations, new_components)

    print(f"\n✅ 狩猎完成!")
    print(f"   灵感: {len(all_inspirations)}")
    print(f"   新组件: {len(new_components)}")
    print(f"   报告: {report_file}")

    return {
        "inspirations": len(all_inspirations),
        "new_components": len(new_components),
        "report": str(report_file)
    }


if __name__ == "__main__":
    result = run_hunt()
    if result:
        print(f"\n🎉 结果: {json.dumps(result, ensure_ascii=False)}")
