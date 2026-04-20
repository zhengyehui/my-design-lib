---
layout: home
hero:
  name: My Design Lib
  text: 你的设计，AI 来加速
  tagline: 一套为 AI 编程助手优化的前端组件库。纯 HTML + CSS，复制即用，零框架依赖。
  actions:
    - theme: brand
      text: 🎨 浏览页面画廊
      link: /pages/
    - theme: alt
      text: 📦 25 个组件
      link: /components/button
    - theme: alt
      text: 🤝 赞助此项目
      link: /sponsor

features:
  - icon: 🎨
    title: 设计系统优先
    details: 完整 Design Tokens（色彩、排版、间距、阴影、动画）。一套 tokens 统一全站风格，改一处全局生效。
  - icon: 🎯
    title: 页面灵感画廊
    details: 完整页面设计展示，像 Awwwards 一样浏览。点击预览实时效果，查看源码和设计分析。
  - icon: 🤖
    title: AI-Friendly
    details: 每个组件都有语义化 class、ai-manifest.json 和 llms.txt，AI 工具可直接读取使用。
  - icon: 📦
    title: 复制即用
    details: 纯 HTML + CSS，零依赖。复制代码粘贴到任何项目就能用。
  - icon: 🌙
    title: 暗色优先设计
    details: 墨色(Ink)调色板为主，内置暗色/亮色模式，data-theme 属性一键切换。
  - icon: 🚀
    title: 生产级质量
    details: 25 个组件、5 个完整页面、3 套设计系统，均已可投入生产使用。
---

<!-- 页面画廊预览 -->
<div class="gallery-preview">
  <div class="gallery-preview__header">
    <h2>🎨 页面灵感画廊</h2>
    <a href="/pages/" class="gallery-preview__more">查看全部 →</a>
  </div>
  <div class="gallery-preview__grid">
    <a href="/pages/saas-landing.html" class="preview-card">
      <div class="preview-card__visual" style="background: linear-gradient(135deg, #eef2ff, #e0e7ff)">
        <div class="mini-mockup">
          <div class="mm-bar"><span></span><span></span><span></span></div>
          <div class="mm-body">
            <div class="mm-line" style="width:60%;background:#6366f133"></div>
            <div class="mm-line" style="width:40%;background:#6366f122"></div>
            <div class="mm-row"><div class="mm-box"></div><div class="mm-box"></div><div class="mm-box"></div></div>
          </div>
        </div>
      </div>
      <div class="preview-card__info">
        <span class="preview-score" style="color:#6366f1">9.2</span>
        <span class="preview-title">NovaPay SaaS 落地页</span>
      </div>
    </a>
    <a href="/pages/portfolio.html" class="preview-card">
      <div class="preview-card__visual" style="background: linear-gradient(135deg, #1a1a2e, #0a0a0a)">
        <div class="mini-mockup dark">
          <div class="mm-bar"><span></span><span></span><span></span></div>
          <div class="mm-body">
            <div class="mm-line" style="width:50%;background:#6366f144"></div>
            <div class="mm-line" style="width:30%;background:#ec489933"></div>
            <div class="mm-row"><div class="mm-box"></div><div class="mm-box"></div></div>
          </div>
        </div>
      </div>
      <div class="preview-card__info">
        <span class="preview-score" style="color:#22c55e">9.5</span>
        <span class="preview-title">创意作品集</span>
      </div>
    </a>
    <a href="/pages/dashboard-dark.html" class="preview-card">
      <div class="preview-card__visual" style="background: linear-gradient(135deg, #1a1a24, #0f0f14)">
        <div class="mini-mockup dark">
          <div class="mm-sidebar"></div>
          <div class="mm-body" style="margin-left:20px">
            <div class="mm-row"><div class="mm-box small"></div><div class="mm-box small"></div><div class="mm-box small"></div><div class="mm-box small"></div></div>
            <div class="mm-line" style="width:80%;background:#6366f122"></div>
          </div>
        </div>
      </div>
      <div class="preview-card__info">
        <span class="preview-score" style="color:#6366f1">9.0</span>
        <span class="preview-title">Nexus 数据仪表盘</span>
      </div>
    </a>
    <a href="/pages/404-creative.html" class="preview-card">
      <div class="preview-card__visual" style="background: linear-gradient(135deg, #0a0a0a, #1a1a2e)">
        <div class="mini-mockup centered">
          <div class="mm-big-number">404</div>
        </div>
      </div>
      <div class="preview-card__info">
        <span class="preview-score" style="color:#a855f7">9.3</span>
        <span class="preview-title">太空主题 404</span>
      </div>
    </a>
  </div>
</div>

<!-- 联系方式 -->
<div class="contact-bar">
  <span>📧 <a href="mailto:weta_zheng@qq.com">weta_zheng@qq.com</a></span>
  <span>💬 微信：<strong>weta010730</strong></span>
  <span>🐙 <a href="https://github.com/zhengyehui/my-design-lib" target="_blank">GitHub</a></span>
</div>

<div class="sponsors-hero">
  <div class="sponsors-hero__title">📊 项目数据</div>
  <div class="sponsors-hero__grid">
    <span class="sponsors-hero__badge">📦 25 个生产级组件</span>
    <span class="sponsors-hero__badge">🎨 5 个完整页面</span>
    <span class="sponsors-hero__badge">🏷️ 3 套设计 Tokens</span>
    <span class="sponsors-hero__badge">🤖 MCP Server 可用</span>
  </div>
</div>

<div class="design-tokens-showcase">
  <div class="showcase-header">
    <h2>🎨 Design Tokens 系统</h2>
    <p>墨色(Ink)优先设计，紫色品牌色，语义化配色</p>
  </div>
  
  <div class="tokens-grid">
    <!-- Color Palette -->
    <div class="token-section">
      <h3>颜色系统</h3>
      <div class="color-palette">
        <div class="color-swatch" style="background: #7c5cff; color: white; border-radius: 8px; padding: 12px;">
          <strong>Brand</strong><br><small>#7C5CFF</small>
        </div>
        <div class="color-swatch" style="background: #3ecf8e; color: white; border-radius: 8px; padding: 12px;">
          <strong>Success</strong><br><small>#3ECF8E</small>
        </div>
        <div class="color-swatch" style="background: #ffb454; color: #000; border-radius: 8px; padding: 12px;">
          <strong>Warning</strong><br><small>#FFB454</small>
        </div>
        <div class="color-swatch" style="background: #ff6b6b; color: white; border-radius: 8px; padding: 12px;">
          <strong>Danger</strong><br><small>#FF6B6B</small>
        </div>
      </div>
    </div>

    <!-- Component Preview -->
    <div class="token-section">
      <h3>组件示例</h3>
      <div class="component-demo">
        <button class="btn btn-primary">Primary Button</button>
        <button class="btn btn-secondary">Secondary</button>
        <button class="btn btn-ghost">Ghost</button>
      </div>
    </div>
  </div>
</div>

<style>
/* Design Tokens Showcase */
.design-tokens-showcase {
  max-width: 1100px;
  margin: 4rem auto;
  padding: 3rem 2rem;
  background: linear-gradient(135deg, var(--ink-900, #131316) 0%, var(--ink-950, #0a0a0b) 100%);
  border-radius: 16px;
  border: 1px solid var(--ink-800, #1a1a1f);
}

.showcase-header {
  text-align: center;
  margin-bottom: 2rem;
}

.showcase-header h2 {
  margin: 0 0 0.5rem;
  font-size: 2rem;
  color: var(--ink-50, #f5f5f8);
}

.showcase-header p {
  margin: 0;
  color: var(--ink-300, #a0a0ab);
  font-size: 1rem;
}

.tokens-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.token-section h3 {
  margin: 0 0 1rem;
  font-size: 1.2rem;
  color: var(--ink-100, #ebebf0);
}

.color-palette {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.color-swatch {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 120px;
  cursor: pointer;
  transition: transform 0.2s;
}

.color-swatch:hover {
  transform: scale(1.05);
}

.color-swatch strong {
  font-size: 0.95rem;
  margin-bottom: 0.25rem;
}

.color-swatch small {
  font-size: 0.8rem;
  opacity: 0.9;
}

.component-demo {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.component-demo button {
  padding: 10px 20px;
  border-radius: 8px;
  border: none;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  font-family: var(--font-body, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif);
}

.component-demo button:nth-child(1) {
  background: #7c5cff;
  color: white;
}

.component-demo button:nth-child(1):hover {
  background: #6b4fe8;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(124, 92, 255, 0.3);
}

.component-demo button:nth-child(2) {
  background: var(--ink-800, #1a1a1f);
  color: var(--ink-100, #ebebf0);
  border: 1px solid var(--ink-700, #25252d);
}

.component-demo button:nth-child(2):hover {
  background: var(--ink-700, #25252d);
  border-color: var(--ink-600, #3d3d47);
}

.component-demo button:nth-child(3) {
  background: transparent;
  color: var(--ink-100, #ebebf0);
  border: 1px solid var(--ink-700, #25252d);
}

.component-demo button:nth-child(3):hover {
  background: rgba(124, 92, 255, 0.08);
  border-color: #7c5cff;
  color: #7c5cff;
}

/* Gallery Preview Section */
.gallery-preview {
  max-width: 1100px;
  margin: 0 auto;
  padding: 3rem 2rem;
}
.gallery-preview__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}
.gallery-preview__header h2 {
  font-size: 1.5rem;
  font-weight: 800;
}
.gallery-preview__more {
  color: var(--vp-c-brand-1);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.95rem;
}
.gallery-preview__more:hover {
  text-decoration: underline;
}
.gallery-preview__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
}

/* Enhanced hero section styling */
:root {
  --hero-gradient: linear-gradient(135deg, var(--ink-950, #0a0a0b) 0%, var(--ink-900, #131316) 100%);
}

/* Override VitePress hero */
.VPHero {
  background: var(--hero-gradient);
  padding-bottom: 4rem;
}

.VPHero .tagline {
  color: var(--ink-300, #a0a0ab);
  font-size: 1.1rem;
}

.VPHero .brand {
  color: var(--brand, #7c5cff);
  font-weight: 700;
}

/* Preview Card */
.preview-card {
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid var(--vp-c-divider);
  text-decoration: none;
  color: inherit;
  transition: all 0.3s;
}
.preview-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0,0,0,0.08), 0 0 32px rgba(124, 92, 255, 0.15);
  border-color: var(--vp-c-brand-1);
}
.preview-card__visual {
  aspect-ratio: 16/10;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  padding: 12%;
}
.preview-card__info {
  padding: 0.8rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: var(--vp-c-bg);
}
.preview-score {
  font-size: 1rem;
  font-weight: 900;
}
.preview-title {
  font-size: 0.85rem;
  color: var(--vp-c-text-2);
}

/* Mini Mockup */
.mini-mockup {
  width: 100%;
  height: 100%;
  border-radius: 6px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0,0,0,0.15);
  background: #fff;
  position: relative;
}
.mini-mockup.dark { background: #1a1a24; }
.mini-mockup.centered { display: flex; align-items: center; justify-content: center; background: #0a0a0a; }
.mm-bar {
  height: 12px;
  background: rgba(0,0,0,0.1);
  display: flex;
  align-items: center;
  gap: 3px;
  padding: 0 6px;
}
.mini-mockup.dark .mm-bar { background: rgba(0,0,0,0.3); }
.mm-bar span {
  width: 4px;
  height: 4px;
  border-radius: 50%;
}
.mm-bar span:nth-child(1) { background: #ff5f57; }
.mm-bar span:nth-child(2) { background: #febc2e; }
.mm-bar span:nth-child(3) { background: #28c840; }
.mm-body { padding: 8px; }
.mm-line { height: 4px; border-radius: 2px; margin-bottom: 6px; }
.mm-row { display: flex; gap: 4px; margin-top: 8px; }
.mm-box { flex: 1; height: 20px; border-radius: 3px; background: rgba(99,102,241,0.08); }
.mm-box.small { height: 14px; background: rgba(99,102,241,0.12); }
.mm-sidebar { position: absolute; left: 0; top: 12px; bottom: 0; width: 20px; background: rgba(99,102,241,0.08); }
.mm-big-number {
  font-size: 1.8rem;
  font-weight: 900;
  background: linear-gradient(135deg, #6366f1, #a855f7, #ec4899);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* Contact Bar */
.contact-bar {
  display: flex;
  justify-content: center;
  gap: 2rem;
  padding: 1.5rem;
  margin-top: 1rem;
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

@media (max-width: 768px) {
  .gallery-preview__grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .contact-bar {
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
  }
}
@media (max-width: 480px) {
  .gallery-preview__grid {
    grid-template-columns: 1fr;
  }
}
</style>
