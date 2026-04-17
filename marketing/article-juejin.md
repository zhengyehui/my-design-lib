# 我做了一个「AI 专属」的前端设计库，让 AI 写代码不再凭空编样式

> 🎯 **不是又一个 UI 库，而是给 AI 编程助手准备的「设计 DNA」**

## 痛点：AI 写的前端，样式总是差点意思

用过 Cursor、Claude Code、Copilot 写前端的都知道——

AI 生成的 HTML/CSS 有个致命问题：**它不知道你想要什么风格**。

每次都要反复 prompt：
> "用圆角大一点的卡片"
> "按钮用紫色，hover 有动效"
> "间距宽松一点，参考 Apple 风格"

即使这样，生成的代码还是五花八门。**同一个项目里，这个组件用 `#6366f1`，那个用 `#7c3aed`**，完全不统一。

## 解法：给 AI 一个「设计锚点」

我做了一个设计库，核心理念很简单：

> **让 AI 先读到你有什么组件、什么风格，再生成代码。**

它不是 React 组件库，不是 Vue 插件。就是**纯 HTML + CSS**，零依赖，复制粘贴就能用。

### 关键设计：ai-manifest.json

```json
{
  "components": [
    { "name": "button", "variants": ["primary", "secondary", "ghost", "danger"] },
    { "name": "card", "variants": ["default", "flat", "glass", "gradient"] },
    { "name": "hero", "variants": ["default", "compact"] },
    ...
  ],
  "tokens": {
    "primary": "#6366f1",
    "radius": { "sm": "6px", "md": "12px", "lg": "20px" }
  }
}
```

AI 读了这个文件，就知道：
- 你有哪些组件
- 每个组件有哪些变体
- 你的颜色、间距、字体是什么

**生成的代码直接用你的设计语言，不用再调。**

## 三个杀手特性

### 1. 零框架依赖

不是 React 组件，不是 Vue 组件。就是**一段 HTML + 一段 CSS**。

不管你在写 Next.js、Nuxt、纯 HTML、甚至 Flutter Web，都能用。

### 2. MCP Server 集成

写了一个 MCP Server，配到 Claude Desktop 或 Cursor 里：

```json
{
  "mcpServers": {
    "my-design-lib": {
      "command": "python3",
      "args": ["scripts/mcp_server.py"]
    }
  }
}
```

然后直接跟 AI 说：
> "用 button 组件的 primary 变体做一个登录按钮"

AI 就会调用 `get_component("button", "primary")` 拿到你的组件代码，而不是凭空编。

### 3. 统一设计语言

19 个组件，共享同一套设计变量：

```css
--color-primary: #6366f1;    /* 靛蓝紫 */
--color-surface: #ffffff;     /* 纯白背景 */
--spacing-md: 1rem;           /* 16px 间距 */
--radius-md: 12px;            /* 中等圆角 */
```

改一个变量，所有组件跟着变。**一次定义，全局统一。**

## 组件清单（19 个，持续更新中）

| 基础组件 | 布局组件 | 反馈组件 |
|---------|---------|---------|
| Button | Hero | Alert |
| Input | Card | Toast |
| Badge | Navbar | Modal |
| Toggle | Footer | Tooltip |
| Avatar | Table | Progress |
| Dropdown | Tabs | Accordion |
| | Breadcrumb | |

## 怎么用？

### 方式 1：直接复制

```html
<!-- 1. 引入设计变量 -->
<link rel="stylesheet" href="http://101.37.166.208:11930/tokens/tokens.css">

<!-- 2. 复制按钮组件 -->
<button class="btn btn--primary btn--md">
  <span>Hello World</span>
</button>
```

### 方式 2：让 AI 帮你用

在 Cursor 或 Claude Code 中配置 MCP Server 后，直接说：

> "用我的设计库做一个 pricing page，三个卡片，primary 按钮"

AI 会自动获取 card、button 组件，用你的设计变量生成完整页面。

### 方式 3：CDN 引入

```html
<link rel="stylesheet" href="http://101.37.166.208:11930/tokens/tokens.css">
```

## 为什么叫「AI-native」？

传统组件库是**给人用的**——人读文档，人复制代码，人粘贴到项目里。

我的设计库是**给 AI 用的**——AI 读 manifest，AI 获取组件代码，AI 直接生成页面。

人只需要说一句话，AI 就能用你的设计语言写出风格统一的前端。

## 开源 & 合作

🔗 **GitHub**: [github.com/your-repo/my-design-lib](https://github.com/your-repo/my-design-lib)  
🔗 **文档站**: http://101.37.166.208:11930  
📧 **赞助合作**: hello@design-lib.dev

### 下一步计划

- [ ] 组件扩充到 30+
- [ ] 发布 Figma 设计文件
- [ ] 支持更多 AI 工具（Windsurf、Cline、Augment）
- [ ] 社区贡献组件审核机制

---

**如果你也在用 AI 写前端，这个项目可能对你有用。欢迎 Star、提 Issue、贡献组件！**

#前端 #AI编程 #设计系统 #开源项目 #Cursor #ClaudeCode
