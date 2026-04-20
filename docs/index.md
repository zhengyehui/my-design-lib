---
layout: home
hero:
  name: My Design Lib
  text: 你的设计，AI 来加速
  tagline: 一套为 AI 编程助手优化的前端组件库。纯 HTML + CSS，复制即用，零框架依赖。

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

<!-- 组件快速预览 - Phase 2 展示 -->
<div class="component-quick-preview">
<div class="cqp-container">
<h2>🎨 组件快速预览</h2>
<p class="cqp-subtitle">立即查看设计系统中的核心组件</p>

<div class="cqp-grid">
<!-- Button 组件 -->
<div class="cqp-card">
<h3>Button 按钮</h3>
<div class="cqp-demo">
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-ghost">Ghost</button>
</div>
</div>

<!-- Card 组件 -->
<div class="cqp-card">
<h3>Card 卡片</h3>
<div class="cqp-demo" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.5rem;">
<div class="card card-flat">Flat</div>
<div class="card card-elevated">Elevated</div>
<div class="card card-featured">Featured</div>
</div>
</div>

<!-- Badge 组件 -->
<div class="cqp-card">
<h3>Badge 徽章</h3>
<div class="cqp-demo" style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
<span class="badge">默认</span>
<span class="badge badge-success">成功</span>
<span class="badge badge-warning">警告</span>
<span class="badge badge-danger">危险</span>
</div>
</div>

<!-- 设计系统统计 -->
<div class="cqp-card">
<h3>📊 库统计</h3>
<div class="cqp-stats">
<div><strong>25</strong><br/>组件</div>
<div><strong>5</strong><br/>页面</div>
<div><strong>3</strong><br/>系统</div>
</div>
</div>
</div>

<div class="cqp-cta">
<a href="/components/button" class="btn btn-primary">📦 浏览全部组件库</a>
<a href="/tokens/colors" class="btn btn-secondary">🎨 查看设计令牌</a>
</div>
</div>
</div>

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

<!-- 项目统计 -->
<div class="project-stats">
  <div class="stats-container">
    <div class="stat-card">
      <div class="stat-icon">📦</div>
      <div class="stat-content">
        <div class="stat-value">25</div>
        <div class="stat-name">生产级组件</div>
      </div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">🎨</div>
      <div class="stat-content">
        <div class="stat-value">5</div>
        <div class="stat-name">完整页面</div>
      </div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">🏷️</div>
      <div class="stat-content">
        <div class="stat-value">3</div>
        <div class="stat-name">设计系统</div>
      </div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">🤖</div>
      <div class="stat-content">
        <div class="stat-value">MCP</div>
        <div class="stat-name">AI 集成</div>
      </div>
    </div>
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
/* ═════════════════════════════════════════════════════════════════════════
   Enhanced Hero Section — Left/Right Layout
   ═════════════════════════════════════════════════════════════════════════ */

.hero-enhanced {
  max-width: 1200px;
  margin: 0 auto;
  padding: 4rem 2rem;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
}

.hero-left {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  width: fit-content;
  padding: 0.5rem 1rem;
  background: rgba(124, 92, 255, 0.1);
  border: 1px solid rgba(124, 92, 255, 0.2);
  border-radius: 20px;
  font-size: 0.875rem;
  color: #7c5cff;
  font-weight: 600;
}

.hero-left h1 {
  font-size: 3.5rem;
  margin: 0;
  font-weight: 700;
  line-height: 1.1;
  background: linear-gradient(135deg, #7c5cff, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-size: 1.25rem;
  margin: 0;
  color: var(--text-primary, #0f172a);
  font-weight: 600;
}

.hero-description {
  font-size: 1rem;
  margin: 0;
  color: var(--text-secondary, #475569);
  line-height: 1.6;
  max-width: 500px;
}

.hero-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  padding: 1.5rem 0;
  border-top: 1px solid var(--border-primary, #e2e8f0);
  border-bottom: 1px solid var(--border-primary, #e2e8f0);
}

.stat-item {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.stat-number {
  font-size: 1.75rem;
  font-weight: 700;
  color: #7c5cff;
}

.stat-label {
  font-size: 0.875rem;
  color: var(--text-muted, #94a3b8);
}

.hero-actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.hero-actions .btn {
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  border-radius: 8px;
}

/* Right Hero — Component Showcase */
.hero-right {
  display: flex;
  justify-content: center;
}

.component-showcase {
  background: var(--bg-secondary, #f8fafc);
  border: 1px solid var(--border-primary, #e2e8f0);
  border-radius: 16px;
  padding: 2rem;
  width: 100%;
  max-width: 500px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
}

.dark .component-showcase {
  background: var(--ink-800, #1a1a1f);
  border-color: var(--ink-700, #25252d);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.showcase-title {
  font-size: 0.875rem;
  font-weight: 600;
  color: #7c5cff;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 1.5rem;
}

.showcase-section {
  margin-bottom: 1.75rem;
}

.showcase-section:last-child {
  margin-bottom: 0;
}

.showcase-section h4 {
  font-size: 0.95rem;
  margin: 0 0 0.75rem;
  color: var(--text-primary, #0f172a);
  font-weight: 600;
}

.showcase-buttons {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.showcase-buttons .btn {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
  width: 100%;
  text-align: center;
}

.showcase-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.75rem;
}

.showcase-cards .card {
  padding: 1rem;
  text-align: center;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-primary, #0f172a);
  cursor: pointer;
  transition: all 0.2s;
}

.showcase-cards .card:hover {
  transform: translateY(-2px);
}

.showcase-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.showcase-badges .badge {
  font-size: 0.75rem;
}

/* Responsive Hero */
@media (max-width: 768px) {
  .hero-enhanced {
    grid-template-columns: 1fr;
    gap: 2rem;
    padding: 2rem 1rem;
  }

  .hero-left h1 {
    font-size: 2.5rem;
  }

  .hero-stats {
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
  }

  .stat-number {
    font-size: 1.5rem;
  }

  .component-showcase {
    max-width: 100%;
  }

  .hero-actions {
    flex-direction: column;
  }

  .hero-actions .btn {
    width: 100%;
  }
}

/* ═════════════════════════════════════════════════════════════════════════
   Design Tokens Showcase
   ═════════════════════════════════════════════════════════════════════════ */

/* Design Tokens Showcase */
.design-tokens-showcase {
  max-width: 1100px;
  margin: 4rem auto;
  padding: 3rem 2rem;
  background: linear-gradient(135deg, #f5f5f8, #ebebf0);
  border-radius: 16px;
  border: 1px solid #e2e8f0;
}

.showcase-header {
  text-align: center;
  margin-bottom: 2rem;
}

.showcase-header h2 {
  margin: 0 0 0.5rem;
  font-size: 2rem;
  color: var(--ink-950, #0a0a0b);
}

.showcase-header p {
  margin: 0;
  color: var(--ink-600, #3d3d47);
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
  color: var(--ink-900, #131316);
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

/* ═════════════════════════════════════════════════════════════════════════
   Project Stats Section
   ═════════════════════════════════════════════════════════════════════════ */

.project-stats {
  max-width: 1100px;
  margin: 3rem auto;
  padding: 3rem 2rem;
  background: linear-gradient(135deg, var(--ink-950, #0a0a0b) 0%, var(--ink-900, #131316) 100%);
  border-radius: 16px;
  border: 1px solid var(--ink-800, #1a1a1f);
}

.stats-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
}

.stat-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.5rem;
  background: rgba(124, 92, 255, 0.05);
  border: 1px solid rgba(124, 92, 255, 0.1);
  border-radius: 12px;
  transition: all 0.3s;
}

.stat-card:hover {
  border-color: rgba(124, 92, 255, 0.3);
  background: rgba(124, 92, 255, 0.08);
  transform: translateY(-2px);
}

.stat-icon {
  font-size: 2rem;
  flex-shrink: 0;
}

.stat-content {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.stat-value {
  font-size: 1.5rem;
  font-weight: 700;
  color: #7c5cff;
}

.stat-name {
  font-size: 0.875rem;
  color: var(--ink-300, #a0a0ab);
}

@media (max-width: 768px) {
  .stats-container {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }

  .stat-card {
    padding: 1rem;
  }

  .stat-value {
    font-size: 1.25rem;
  }

  .stat-name {
    font-size: 0.8rem;
  }
}

/* ═════════════════════════════════════════════════════════════════════════
   Component Quick Preview — Phase 2 Showcase
   ═════════════════════════════════════════════════════════════════════════ */

.component-quick-preview {
  max-width: 1100px;
  margin: 2rem auto 3rem;
  padding: 2.5rem;
  background: linear-gradient(135deg, var(--ink-900, #131316) 0%, var(--ink-800, #1a1a1f) 100%);
  border: 1px solid var(--ink-700, #25252d);
  border-radius: 16px;
}

.cqp-container h2 {
  text-align: center;
  font-size: 1.75rem;
  margin: 0 0 0.5rem;
  color: var(--ink-50, #f5f5f8);
}

.cqp-subtitle {
  text-align: center;
  color: var(--ink-300, #a0a0ab);
  margin-bottom: 2rem;
  font-size: 1rem;
}

.cqp-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.cqp-card {
  background: rgba(124, 92, 255, 0.05);
  border: 1px solid rgba(124, 92, 255, 0.1);
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.3s;
}

.cqp-card:hover {
  border-color: rgba(124, 92, 255, 0.2);
  background: rgba(124, 92, 255, 0.08);
  transform: translateY(-2px);
}

.cqp-card h3 {
  font-size: 0.95rem;
  margin: 0 0 1rem;
  color: var(--ink-100, #ebebf0);
  font-weight: 600;
}

.cqp-demo {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.cqp-demo .btn {
  padding: 0.5rem 1rem;
  font-size: 0.85rem;
  width: 100%;
  text-align: center;
  border-radius: 6px;
}

.cqp-demo .card {
  padding: 0.75rem;
  text-align: center;
  font-size: 0.8rem;
  font-weight: 600;
}

.cqp-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.75rem;
  text-align: center;
}

.cqp-stats div {
  color: var(--ink-100, #ebebf0);
  font-size: 0.9rem;
  line-height: 1.4;
}

.cqp-stats strong {
  font-size: 1.5rem;
  color: #7c5cff;
  display: block;
}

.cqp-cta {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.cqp-cta .btn {
  padding: 0.75rem 1.5rem;
  font-size: 0.95rem;
}

@media (max-width: 768px) {
  .component-quick-preview {
    padding: 1.5rem;
  }

  .cqp-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .cqp-cta {
    flex-direction: column;
  }

  .cqp-cta .btn {
    width: 100%;
  }
}
</style>
