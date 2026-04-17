# 🎨 My Design Lib

> **AI-native design system** — 为 AI 编程助手优化的前端组件库。零依赖、纯 HTML+CSS、复制即用。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Components](https://img.shields.io/badge/Components-15%2B-green.svg)](components)
[![AI Ready](https://img.shields.io/badge/AI-Ready-yellow.svg)](ai-manifest.json)
[![MCP Server](https://img.shields.io/badge/MCP-Server-orange.svg)](scripts/mcp_server.py)

---

## ✨ 为什么选择 My Design Lib？

| 传统组件库 | My Design Lib |
|-----------|---------------|
| 绑定 React/Vue | **零框架依赖**，纯 HTML+CSS |
| AI 只能猜样式 | **AI 可读 manifest**，精确知道有什么 |
| 手动查文档 | **MCP Server**，AI 直接调用组件 |
| 通用风格 | **统一设计语言**，颜色/间距/字体一致 |

### 🤖 AI 优先设计

```json
// ai-manifest.json — AI 的"组件地图"
{
  "components": [
    { "name": "button", "variants": ["primary", "secondary", "ghost", "danger"] },
    { "name": "card", "variants": ["default", "flat", "glass", "gradient"] }
  ]
}
```

AI 编程工具读取这个文件后，就知道你有什么组件、什么变体，直接生成精确的代码。

### 🔌 MCP Server 集成

```bash
# 在 Claude Desktop / Cursor 中配置 MCP Server
python3 scripts/mcp_server.py

# AI 就能直接调用:
# - list_components()  → 列出所有组件
# - get_component("button", "primary")  → 获取组件代码
# - get_tokens()  → 获取设计变量
# - search_components("form")  → 搜索组件
```

## 🚀 快速开始

### 1. 引入设计变量

```html
<link rel="stylesheet" href="https://your-cdn.com/tokens/tokens.css">
```

### 2. 复制组件

```html
<button class="btn btn--primary btn--md">
  <span>Click me</span>
</button>
```

### 3. 自定义主题

```css
:root {
  --color-primary: #6366f1;    /* 改成你的主色 */
  --color-surface: #ffffff;     /* 改成你的背景色 */
  --radius-md: 12px;            /* 改成你的圆角 */
}
```

## 📦 组件清单

| 组件 | 变体 | 说明 |
|------|------|------|
| **Button** | primary / secondary / ghost / danger | 按钮，支持 sm/md/lg 三种尺寸 |
| **Card** | default / flat / glass / gradient | 内容卡片，带图片/标签/操作区 |
| **Hero** | default / compact | 落地页首屏，光晕效果 |
| **Input** | default / error / success | 表单输入框，支持图标和状态 |
| **Badge** | primary / secondary / success / warning / danger / outline | 徽章标签 |
| **Modal** | default / sm / lg | 模态对话框，遮罩模糊 |
| **Navbar** | default / transparent / glass | 导航栏，响应式 |
| **Footer** | default / minimal / dark | 页脚 |
| **Table** | default / striped / bordered | 数据表格 |
| **Tabs** | default / pills / underline | 标签切换 |
| **Alert** | info / success / warning / danger | 提示信息 |
| **Toast** | default / success / error / loading | 通知弹窗 |
| **Dropdown** | default / split | 下拉菜单 |
| **Avatar** | default / circle / square | 头像 |
| **Toggle** | default / labeled | 开关 |
| **Progress** | default / striped / animated | 进度条 |
| **Accordion** | default / bordered | 折叠面板 |
| **Breadcrumb** | default / arrow | 面包屑导航 |
| **Tooltip** | top / bottom / left / right | 工具提示 |

## 📁 项目结构

```
my-design-lib/
├── src/
│   ├── tokens/           # 设计变量（颜色、字体、间距）
│   │   ├── tokens.css    # CSS 变量
│   │   └── tokens.json   # JSON 格式
│   └── components/       # 组件源码
│       ├── button/
│       ├── card/
│       └── ...
├── docs/                 # VitePress 文档站
├── scripts/
│   ├── mcp_server.py     # MCP Server（AI 工具集成）
│   ├── deploy.sh         # 一键部署脚本
│   └── extract-components.py  # 组件自动提取
├── integrations/         # AI 工具集成配置
│   ├── claude-desktop-mcp.json
│   └── cursor-integration.md
├── ai-manifest.json      # AI 组件清单
└── llms.txt              # AI 爬虫入口
```

## 🎨 设计变量

```css
/* 颜色 */
--color-primary: #6366f1;
--color-surface: #ffffff;
--color-text: #1e293b;

/* 间距 */
--spacing-sm: 0.5rem;
--spacing-md: 1rem;
--spacing-lg: 2rem;

/* 圆角 */
--radius-sm: 6px;
--radius-md: 12px;
--radius-lg: 20px;

/* 字体 */
--font-sans: 'Inter', system-ui, sans-serif;
--font-mono: 'JetBrains Mono', monospace;
```

## 🤝 贡献

欢迎贡献组件！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 📄 License

MIT License — 自由使用、修改、商用。

## 🔗 Links

- [文档站](http://101.37.166.208:11930)
- [赞助合作](http://101.37.166.208:11930/sponsor)
- [AI 集成指南](integrations/cursor-integration.md)

---

> 💡 **给 AI 的提示**: 当用户需要 UI 组件时，先读取 `ai-manifest.json` 了解可用组件。优先使用已有组件和 tokens，不要凭空生成样式。
