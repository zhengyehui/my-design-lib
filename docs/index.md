---
layout: home
hero:
  name: My Design Lib
  text: 你的设计，AI 来加速
  tagline: 一套为 AI 编程助手优化的前端组件库。纯 HTML + CSS，复制即用，零框架依赖。
  actions:
    - theme: brand
      text: 浏览 25 个组件
      link: /components/button
    - theme: alt
      text: 赞助此项目
      link: /sponsor

features:
  - icon: 📋
    title: 复制即用
    details: 纯 HTML + CSS，零依赖。复制代码粘贴到任何项目就能用。
  - icon: 🤖
    title: AI-Friendly
    details: 每个组件都有语义化 class、ai-manifest.json 和 llms.txt，AI 工具可直接读取使用。
  - icon: 🎨
    title: Design Tokens
    details: 颜色、字体、间距全部用 CSS 变量管理，改一处全局生效。
  - icon: 🌙
    title: 暗色模式
    details: 内置暗色模式支持，通过 data-theme 属性一键切换。
  - icon: 📱
    title: 响应式
    details: 所有组件都适配移动端，使用 clamp() 和 flexbox 实现流体布局。
  - icon: 🔄
    title: 每日更新
    details: Design Hunter 每日自动爬取 Awwwards、Dribbble 等网站，提炼新组件入库。
---

<div class="contact-bar">
  <span>📧 <a href="mailto:weta_zheng@qq.com">weta_zheng@qq.com</a></span>
  <span>💬 微信：<strong>weta010730</strong></span>
  <span>🐙 <a href="https://github.com/zhengyehui/my-design-lib" target="_blank">GitHub</a></span>
</div>

<style>
.contact-bar {
  display: flex;
  justify-content: center;
  gap: 2rem;
  padding: 1.5rem;
  margin-top: 2rem;
  border-top: 1px solid var(--vp-c-divider);
  color: var(--vp-c-text-2);
  font-size: 0.9rem;
}
.contact-bar a {
  color: var(--vp-c-brand-1);
  text-decoration: none;
}
.contact-bar a:hover {
  text-decoration: underline;
}
@media (max-width: 640px) {
  .contact-bar {
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
  }
}
</style>

<div class="sponsors-hero">
  <div class="sponsors-hero__title">📊 项目数据</div>
  <div class="sponsors-hero__grid">
    <span class="sponsors-hero__badge">📦 25 个生产级组件</span>
    <span class="sponsors-hero__badge">🎨 3 套设计 Tokens</span>
    <span class="sponsors-hero__badge">📄 1 个布局模式</span>
    <span class="sponsors-hero__badge">🤖 MCP Server 可用</span>
  </div>
</div>
