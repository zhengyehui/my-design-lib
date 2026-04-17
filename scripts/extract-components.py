#!/usr/bin/env python3
"""
extract-components.py — 从项目代码中自动提取可复用的 UI 组件

用法:
  python scripts/extract-components.py ~/projects/my-app
  python scripts/extract-components.py ~/projects/my-app --threshold 3

工作流程:
  1. 扫描指定目录下的 HTML/JSX/Vue/TSX 文件
  2. 提取带 class 的 HTML 片段
  3. 识别重复模式（同一 class 出现 ≥ threshold 次）
  4. 提取对应的 CSS
  5. 输出到 src/incoming/ 目录
"""

import os
import sys
import json
import hashlib
import re
from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict

# ── 配置 ──────────────────────────────────────────────────
DESIGN_LIB_ROOT = Path(__file__).parent.parent
INCOMING_DIR = DESIGN_LIB_ROOT / "src" / "incoming"
REGISTRY_FILE = DESIGN_LIB_ROOT / "registry.json"
SCAN_EXTENSIONS = {".html", ".jsx", ".tsx", ".vue", ".svelte"}
CSS_EXTENSIONS = {".css", ".scss", ".less"}
IGNORE_DIRS = {"node_modules", ".git", "dist", "build", ".next", "__pycache__"}
DEFAULT_THRESHOLD = 3  # 同一模式出现次数阈值


def find_files(project_dir: Path) -> dict:
    """扫描项目目录，返回 {扩展名: [文件路径]}"""
    files = defaultdict(list)
    for root, dirs, filenames in os.walk(project_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for f in filenames:
            p = Path(root) / f
            if p.suffix in SCAN_EXTENSIONS | CSS_EXTENSIONS:
                files[p.suffix].append(p)
    return dict(files)


def extract_html_blocks(filepath: Path) -> list[dict]:
    """从 HTML/JSX 文件中提取带 class 的 HTML 块"""
    try:
        content = filepath.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return []

    blocks = []
    # 简化版：提取带 class 的 div 块（正则方式，适合 MVP）
    # 正式版应该用 BeautifulSoup / babel 做 AST 解析
    pattern = r'<(\w+)[^>]*class=["\']([^"\']+)["\'][^>]*>[\s\S]*?</\1>'
    for match in re.finditer(pattern, content):
        tag = match.group(1)
        classes = match.group(2)
        html = match.group(0)
        blocks.append({
            "file": str(filepath),
            "tag": tag,
            "classes": classes,
            "html": html[:500],  # 截断，只保留前 500 字符
            "hash": hashlib.md5(html.encode()).hexdigest()[:8]
        })
    return blocks


def find_duplicate_patterns(blocks: list[dict], threshold: int) -> list[dict]:
    """找出重复出现的组件模式"""
    # 按 class 组合分组
    class_groups = defaultdict(list)
    for block in blocks:
        # 取主要 class（第一个）
        main_class = block["classes"].split()[0] if block["classes"] else ""
        if main_class:
            class_groups[main_class].append(block)

    # 筛选超过阈值的
    duplicates = []
    for cls, group in sorted(class_groups.items(), key=lambda x: -len(x[1])):
        if len(group) >= threshold:
            duplicates.append({
                "pattern": cls,
                "count": len(group),
                "tag": group[0]["tag"],
                "sources": list(set(b["file"] for b in group)),
                "sample_html": group[0]["html"],
                "hash": group[0]["hash"]
            })
    return duplicates


def extract_css_for_classes(project_dir: Path, classes: list[str]) -> dict:
    """尝试从项目 CSS 文件中提取相关样式"""
    css_files = []
    for root, dirs, filenames in os.walk(project_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for f in filenames:
            if Path(f).suffix in CSS_EXTENSIONS:
                css_files.append(Path(root) / f)

    results = {}
    for cls in classes:
        pattern = re.compile(rf'\.{re.escape(cls)}\s*\{{[^}}]+\}}', re.DOTALL)
        for css_file in css_files:
            try:
                content = css_file.read_text(encoding="utf-8", errors="ignore")
                matches = pattern.findall(content)
                if matches:
                    results[cls] = {
                        "css": "\n".join(matches),
                        "source": str(css_file)
                    }
            except Exception:
                continue
    return results


def save_incoming(pattern: dict, css_data: dict):
    """保存提取的组件到 incoming 目录"""
    INCOMING_DIR.mkdir(parents=True, exist_ok=True)

    component_name = f"{pattern['pattern']}-{pattern['hash']}"
    component_dir = INCOMING_DIR / component_name
    component_dir.mkdir(exist_ok=True)

    # 保存 HTML
    (component_dir / "source.html").write_text(
        f"<!-- Extracted from: {', '.join(pattern['sources'])} -->\n"
        f"<!-- Usage count: {pattern['count']} -->\n\n"
        f"{pattern['sample_html']}",
        encoding="utf-8"
    )

    # 保存 CSS（如果有）
    if pattern['pattern'] in css_data:
        (component_dir / "source.css").write_text(
            f"/* Extracted from: {css_data[pattern['pattern']]['source']} */\n\n"
            f"{css_data[pattern['pattern']]['css']}",
            encoding="utf-8"
        )

    # 保存 meta
    meta = {
        "name": component_name,
        "tag": pattern["tag"],
        "classes": pattern["pattern"],
        "usage_count": pattern["count"],
        "source_projects": pattern["sources"],
        "extracted_at": datetime.now().isoformat(),
        "status": "pending",  # pending → reviewing → approved / rejected
        "hash": pattern["hash"]
    }
    (component_dir / "meta.json").write_text(
        json.dumps(meta, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    return component_name


def main():
    if len(sys.argv) < 2:
        print("用法: python extract-components.py <项目目录> [--threshold N]")
        sys.exit(1)

    project_dir = Path(sys.argv[1]).expanduser().resolve()
    if not project_dir.is_dir():
        print(f"❌ 目录不存在: {project_dir}")
        sys.exit(1)

    threshold = DEFAULT_THRESHOLD
    if "--threshold" in sys.argv:
        idx = sys.argv.index("--threshold")
        threshold = int(sys.argv[idx + 1])

    print(f"🔍 扫描项目: {project_dir}")
    print(f"📊 重复阈值: {threshold} 次\n")

    # 1. 找文件
    files = find_files(project_dir)
    total_files = sum(len(v) for v in files.values())
    print(f"📁 发现 {total_files} 个文件")

    # 2. 提取 HTML 块
    all_blocks = []
    for ext, file_list in files.items():
        if ext in SCAN_EXTENSIONS:
            for f in file_list:
                blocks = extract_html_blocks(f)
                all_blocks.extend(blocks)
    print(f"📦 提取到 {len(all_blocks)} 个 HTML 块")

    # 3. 找重复模式
    patterns = find_duplicate_patterns(all_blocks, threshold)
    print(f"🔄 发现 {len(patterns)} 个重复模式\n")

    if not patterns:
        print("✅ 没有发现重复模式，代码很干净！")
        return

    # 4. 提取 CSS
    class_names = [p["pattern"] for p in patterns]
    css_data = extract_css_for_classes(project_dir, class_names)

    # 5. 保存
    saved = []
    for pattern in patterns:
        name = save_incoming(pattern, css_data)
        saved.append(name)
        print(f"  ✅ {name} (出现 {pattern['count']} 次)")

    print(f"\n🎉 提取完成！{len(saved)} 个组件已保存到 src/incoming/")
    print(f"   运行 'design-lib review' 审核组件")


if __name__ == "__main__":
    main()
