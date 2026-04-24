---
layout: false
head:
  - - script
    - src: /pages/page-detail.js
      defer: true
title: NovaPay SaaS 落地页
---

<div class="page-detail">
  <nav class="detail-nav">
    <a href="/" class="nav-logo">◆ My Design Lib</a>
    <div class="nav-links">
      <a href="/">首页</a>
      <a href="/components/button.html">组件</a>
      <a href="/tokens/colors.html">设计变量</a>
      <a href="/patterns/landing.html">布局模式</a>
      <a href="/pages/" class="active">🎨 页面画廊</a>
      <a href="/sponsor.html">🤝 赞助</a>
    </div>
  </nav>

  <!-- SEO Meta -->
  <meta name="description" content="现代 SaaS 产品落地页模板，渐变 Hero + 特性卡片 + CTA 区域，纯 HTML+CSS 零依赖，可直接复制使用。">
  <meta name="keywords" content="SaaS, landing page, 落地页, 渐变, 前端模板">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="article">
  <meta property="og:title" content="NovaPay SaaS 落地页 — My Design Lib">
  <meta property="og:description" content="现代 SaaS 产品落地页模板，渐变 Hero + 特性卡片 + CTA 区域，纯 HTML+CSS 零依赖，可直接复制使用。">
  <meta property="og:url" content="http://101.37.166.208:11930/pages/saas-landing.html">
  <link rel="canonical" href="http://101.37.166.208:11930/pages/saas-landing.html">
  <script type="application/ld+json">{"@context":"https://schema.org","@type":"CreativeWork","name":"NovaPay SaaS 落地页 — My Design Lib","description":"现代 SaaS 产品落地页模板，渐变 Hero + 特性卡片 + CTA 区域，纯 HTML+CSS 零依赖，可直接复制使用。","url":"http://101.37.166.208:11930/pages/saas-landing.html","genre":"landing","author":{"@type":"Organization","name":"My Design Lib"}}</script>


  <div class="detail-header">
    <a href="/pages/" class="back-link">← 返回画廊</a>
    <div class="detail-meta">
      <h1>NovaPay SaaS 落地页</h1>
      <div class="detail-tags">
        <span class="tag">SaaS</span><span class="tag">落地页</span><span class="tag">渐变</span>
        <span class="score">⭐ 9.2</span>
      </div>
    </div>
    <div class="detail-actions">
      <button class="action-btn active" onclick="showPreview()">👁 预览</button>
      <button class="action-btn" onclick="showCode()">📝 源码</button>
      <a href="/pages/saas-landing/index.html" target="_blank" class="action-btn">↗ 新窗口打开</a>
    </div>
  </div>

  <div class="detail-body">
    <div id="preview-panel" class="panel"><iframe src="/pages/saas-landing/index.html" sandbox="allow-scripts" loading="lazy"></iframe></div>
    <div id="code-panel" class="panel" style="display:none">
    <button id="copy-btn" class="copy-btn" onclick="copySourceCode()">📋 复制源码</button>
    <pre><code id="code-content">加载中...</code></pre>
  </div>
  </div>

  <div class="design-tips">
    <h2>💡 设计分析</h2>
    <div class="tips-grid">
      <div class="tip"><h3>布局结构</h3><p>经典 SaaS 落地页：固定导航 → Hero（渐变背景+CTA）→ 数据统计 → 特性网格 → CTA → 页脚</p></div>
      <div class="tip"><h3>配色方案</h3><p>主色靛蓝紫 (#6366f1) 渐变到紫色 (#7c3aed)，搭配冷灰色系。Hero 区浅色渐变背景。</p></div>
      <div class="tip"><h3>亮点技巧</h3><p>• Hero 背景 radial-gradient 装饰圆形<br>• 统计数字大号粗体突出<br>• 特性卡片 hover 上浮+阴影<br>• CTA 全宽渐变背景视觉冲击</p></div>
      <div class="tip"><h3>适用场景</h3><p>SaaS 产品、工具类网站、API 服务、开发者平台首页</p></div>
    </div>
  </div>

  <div class="detail-footer">
    <a href="/pages/" class="back-btn">← 返回画廊</a>
    <div class="nav-prevnext">
      <a href="/pages/404-creative.html">← 太空主题 404</a>
      <a href="/pages/portfolio.html">创意作品集 →</a>
    </div>
  </div>
</div>

<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, 'Segoe UI', sans-serif; }

.detail-nav {
  position: sticky; top: 0; z-index: 100;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0.8rem 2rem;
  background: rgba(255,255,255,0.9); backdrop-filter: blur(12px);
  border-bottom: 1px solid #e5e7eb;
}
.nav-logo { font-size: 1.1rem; font-weight: 800; color: #6366f1; text-decoration: none; }
.nav-links { display: flex; gap: 1.5rem; align-items: center; }
.nav-links a { text-decoration: none; color: #666; font-size: 0.9rem; font-weight: 500; transition: color 0.2s; }
.nav-links a:hover, .nav-links a.active { color: #6366f1; }

.page-detail { max-width: 1200px; margin: 0 auto; padding: 1rem 2rem; }
.detail-header { padding: 1rem 0; }
.back-link { color: #6366f1; text-decoration: none; font-size: 0.9rem; display: inline-block; margin-bottom: 1rem; }
.back-link:hover { text-decoration: underline; }
.detail-meta h1 { font-size: 1.8rem; font-weight: 800; margin-bottom: 0.5rem; }
.detail-tags { display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap; }
.tag { padding: 0.3rem 0.8rem; background: #f3f4f6; border-radius: 8px; font-size: 0.8rem; color: #666; }
.score { font-size: 0.9rem; font-weight: 700; margin-left: 0.5rem; }
.detail-actions { display: flex; gap: 0.5rem; margin-top: 1rem; flex-wrap: wrap; }
.action-btn { padding: 0.5rem 1.2rem; border: 1px solid #e5e7eb; border-radius: 8px; background: none; cursor: pointer; font-size: 0.85rem; color: #666; text-decoration: none; transition: all 0.2s; }
.action-btn:hover, .action-btn.active { border-color: #6366f1; color: #6366f1; background: rgba(99,102,241,0.05); }

.detail-body { margin: 1.5rem 0; border: 1px solid #e5e7eb; border-radius: 12px; overflow: hidden; background: #fff; }
.panel iframe { width: 100%; height: 70vh; border: none; }
.panel pre { padding: 1.5rem; overflow: auto; max-height: 70vh; background: #1e1e2e; color: #cdd6f4; font-size: 0.85rem; line-height: 1.6; }
.panel code { font-family: 'JetBrains Mono', monospace; white-space: pre; }

.design-tips { margin: 2rem 0; }
.design-tips h2 { font-size: 1.3rem; font-weight: 700; margin-bottom: 1rem; }
.tips-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; }
.tip { padding: 1.2rem; border: 1px solid #e5e7eb; border-radius: 12px; }
.tip h3 { font-size: 0.95rem; font-weight: 700; margin-bottom: 0.5rem; color: #6366f1; }
.tip p { font-size: 0.85rem; color: #666; line-height: 1.6; }

.detail-footer {
  display: flex; justify-content: space-between; align-items: center;
  padding: 2rem 0; margin-top: 2rem; border-top: 1px solid #e5e7eb;
}
.back-btn { color: #6366f1; text-decoration: none; font-weight: 600; }
.nav-prevnext { display: flex; gap: 2rem; }
.nav-prevnext a { color: #666; text-decoration: none; font-size: 0.9rem; }
.nav-prevnext a:hover { color: #6366f1; }

</style>

