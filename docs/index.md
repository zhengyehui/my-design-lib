---
layout: home

hero:
  name: My Design Lib
  text: 你的设计，AI 来加速
  tagline: 为 AI 编程助手优化的前端组件库。纯 HTML + CSS，复制即用，零依赖。
  actions:
    - theme: brand
      text: 浏览组件
      link: /components/button
    - theme: alt
      text: 查看画廊
      link: /pages/
---

<div class="home-gallery">
  <div class="home-gallery__header">
    <div>
      <h2>页面灵感画廊</h2>
      <p class="home-gallery__sub">12 个完整页面，一键查看真实效果</p>
    </div>
    <a href="/pages/" class="home-gallery__more">查看全部 →</a>
  </div>
  <div class="home-gallery__grid">
    <a href="/pages/saas-landing.html" class="thumb-card">
      <div class="thumb-card__frame">
        <iframe src="/pages/saas-landing/index.html" scrolling="no" loading="lazy" tabindex="-1" sandbox="allow-same-origin allow-scripts" title="NovaPay SaaS"></iframe>
        <div class="thumb-card__overlay"></div>
      </div>
      <div class="thumb-card__meta">
        <span class="thumb-card__title">NovaPay SaaS</span>
        <span class="thumb-card__tag">落地页</span>
      </div>
    </a>
    <a href="/pages/ai-saas-landing.html" class="thumb-card">
      <div class="thumb-card__frame">
        <iframe src="/pages/ai-saas-landing/index.html" scrolling="no" loading="lazy" tabindex="-1" sandbox="allow-same-origin allow-scripts" title="NexusAI"></iframe>
        <div class="thumb-card__overlay"></div>
      </div>
      <div class="thumb-card__meta">
        <span class="thumb-card__title">NexusAI 智能平台</span>
        <span class="thumb-card__tag">AI SaaS</span>
      </div>
    </a>
    <a href="/pages/portfolio.html" class="thumb-card">
      <div class="thumb-card__frame">
        <iframe src="/pages/portfolio/index.html" scrolling="no" loading="lazy" tabindex="-1" sandbox="allow-same-origin allow-scripts" title="创意作品集"></iframe>
        <div class="thumb-card__overlay"></div>
      </div>
      <div class="thumb-card__meta">
        <span class="thumb-card__title">创意作品集</span>
        <span class="thumb-card__tag">Portfolio</span>
      </div>
    </a>
    <a href="/pages/dashboard-dark.html" class="thumb-card">
      <div class="thumb-card__frame">
        <iframe src="/pages/dashboard-dark/index.html" scrolling="no" loading="lazy" tabindex="-1" sandbox="allow-same-origin allow-scripts" title="Nexus 仪表盘"></iframe>
        <div class="thumb-card__overlay"></div>
      </div>
      <div class="thumb-card__meta">
        <span class="thumb-card__title">Nexus 仪表盘</span>
        <span class="thumb-card__tag">Dashboard</span>
      </div>
    </a>
    <a href="/pages/checkout.html" class="thumb-card">
      <div class="thumb-card__frame">
        <iframe src="/pages/checkout/index.html" scrolling="no" loading="lazy" tabindex="-1" sandbox="allow-same-origin allow-scripts" title="ShopFlow 结账"></iframe>
        <div class="thumb-card__overlay"></div>
      </div>
      <div class="thumb-card__meta">
        <span class="thumb-card__title">ShopFlow 结账页</span>
        <span class="thumb-card__tag">电商</span>
      </div>
    </a>
    <a href="/pages/product-minimal.html" class="thumb-card">
      <div class="thumb-card__frame">
        <iframe src="/pages/product-minimal/index.html" scrolling="no" loading="lazy" tabindex="-1" sandbox="allow-same-origin allow-scripts" title="FlowDesk"></iframe>
        <div class="thumb-card__overlay"></div>
      </div>
      <div class="thumb-card__meta">
        <span class="thumb-card__title">FlowDesk 极简产品</span>
        <span class="thumb-card__tag">极简</span>
      </div>
    </a>
  </div>
</div>

<div class="home-features">
  <div class="home-features__grid">
    <div class="home-feature">
      <div class="home-feature__num">01</div>
      <h3>设计系统</h3>
      <p>完整 Design Tokens，25 个生产级组件，统一视觉风格</p>
    </div>
    <div class="home-feature">
      <div class="home-feature__num">02</div>
      <h3>AI-Friendly</h3>
      <p>语义化 class + ai-manifest.json，AI 工具可直接读取使用</p>
    </div>
    <div class="home-feature">
      <div class="home-feature__num">03</div>
      <h3>零依赖</h3>
      <p>纯 HTML + CSS，复制粘贴即可使用，无需任何框架</p>
    </div>
  </div>
</div>

<div class="minimal-stats">
  <div class="minimal-stats__item">
    <div class="minimal-stats__value">25</div>
    <div class="minimal-stats__label">Components</div>
  </div>
  <div class="minimal-stats__divider"></div>
  <div class="minimal-stats__item">
    <div class="minimal-stats__value">12</div>
    <div class="minimal-stats__label">Pages</div>
  </div>
  <div class="minimal-stats__divider"></div>
  <div class="minimal-stats__item">
    <div class="minimal-stats__value">3</div>
    <div class="minimal-stats__label">Design Systems</div>
  </div>
  <div class="minimal-stats__divider"></div>
  <div class="minimal-stats__item">
    <div class="minimal-stats__value">MCP</div>
    <div class="minimal-stats__label">AI Integration</div>
  </div>
</div>

<style>
/* ═══════════════════════════════════════════════════════════════════════════
   Minimal Homepage — Hero → Gallery → Features → Stats
   ═══════════════════════════════════════════════════════════════════════════ */

/* Hero 紧凑化 */
.VPHero {
  background: transparent !important;
  padding: 4rem 2rem 2.5rem !important;
}

.VPHero .container {
  max-width: 1200px;
}

.VPHero .name {
  font-size: 3rem !important;
  font-weight: 800 !important;
  letter-spacing: -0.03em !important;
  background: linear-gradient(135deg, #7c5cff, #a855f7);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.VPHero .text {
  font-size: 1.5rem !important;
  color: var(--ink-800, #1a1a1f) !important;
  font-weight: 600 !important;
  margin-top: 0.5rem !important;
}

.VPHero .tagline {
  color: var(--ink-500, #525260) !important;
  font-size: 1rem !important;
  max-width: 560px;
  line-height: 1.6 !important;
  margin-top: 1.25rem !important;
}

.VPHero .actions {
  margin-top: 2rem !important;
  gap: 0.75rem !important;
}

.VPHero .action {
  margin: 0 !important;
}

.VPButton.brand {
  background: var(--ink-950, #0a0a0b) !important;
  border-color: var(--ink-950, #0a0a0b) !important;
}

.VPButton.brand:hover {
  background: var(--ink-800, #1a1a1f) !important;
  border-color: var(--ink-800, #1a1a1f) !important;
  transform: translateY(-1px);
}

.VPButton.alt {
  background: transparent !important;
  border: 1px solid #ebebf0 !important;
  color: var(--ink-800, #1a1a1f) !important;
}

.VPButton.alt:hover {
  background: #fafafa !important;
  border-color: #d4d4db !important;
}

/* 隐藏 VitePress 默认 features（我们用自定义版本） */
.VPFeatures {
  display: none !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   Gallery — 真实 iframe 预览
   ═══════════════════════════════════════════════════════════════════════════ */

.home-gallery {
  max-width: 1200px;
  margin: 2rem auto 5rem;
  padding: 0 2rem;
}

.home-gallery__header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 2rem;
  padding-bottom: 1.25rem;
  border-bottom: 1px solid #ebebf0;
}

.home-gallery__header h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--ink-950, #0a0a0b);
  margin: 0;
  letter-spacing: -0.02em;
  border: none;
  padding: 0;
}

.home-gallery__sub {
  font-size: 0.875rem;
  color: var(--ink-500, #525260);
  margin: 0.375rem 0 0;
}

.home-gallery__more {
  color: var(--ink-500, #525260);
  font-size: 0.875rem;
  text-decoration: none;
  transition: color 0.2s;
  white-space: nowrap;
}

.home-gallery__more:hover {
  color: #7c5cff;
}

.home-gallery__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

/* 缩略图卡片 */
.thumb-card {
  text-decoration: none;
  color: inherit;
  display: block;
}

.thumb-card__frame {
  position: relative;
  aspect-ratio: 16/10;
  border-radius: 10px;
  border: 1px solid #ebebf0;
  overflow: hidden;
  background: #fafafa;
  transition: all 0.3s ease;
}

.thumb-card:hover .thumb-card__frame {
  border-color: #c8c8d0;
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08);
}

.thumb-card__frame iframe {
  /* 按桌面宽 1440 渲染，然后缩放到卡片宽度 */
  position: absolute;
  top: 0;
  left: 0;
  width: 1440px;
  height: 900px;
  border: 0;
  transform: scale(0.266667);
  transform-origin: top left;
  pointer-events: none;
  background: #fff;
}

/* 覆盖层：防止 iframe 捕获点击，且提供微妙 hover 变暗效果 */
.thumb-card__overlay {
  position: absolute;
  inset: 0;
  background: transparent;
  transition: background 0.25s ease;
  z-index: 2;
}

.thumb-card:hover .thumb-card__overlay {
  background: rgba(124, 92, 255, 0.04);
}

.thumb-card__meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.875rem 0.125rem 0;
}

.thumb-card__title {
  font-size: 0.9rem;
  color: var(--ink-900, #131316);
  font-weight: 600;
}

.thumb-card__tag {
  font-size: 0.7rem;
  color: var(--ink-500, #525260);
  background: #f4f4f8;
  padding: 0.2rem 0.55rem;
  border-radius: 999px;
  font-weight: 500;
}

/* ═══════════════════════════════════════════════════════════════════════════
   Features — 极简编号卡
   ═══════════════════════════════════════════════════════════════════════════ */

.home-features {
  max-width: 1200px;
  margin: 0 auto 4rem;
  padding: 0 2rem;
}

.home-features__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2.5rem;
  padding: 3rem 0;
  border-top: 1px solid #ebebf0;
}

.home-feature__num {
  font-family: var(--font-mono, monospace);
  font-size: 0.75rem;
  color: #a855f7;
  letter-spacing: 0.1em;
  margin-bottom: 0.75rem;
  font-weight: 600;
}

.home-feature h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--ink-950, #0a0a0b);
  margin: 0 0 0.5rem;
  border: none;
  padding: 0;
}

.home-feature p {
  color: var(--ink-500, #525260);
  font-size: 0.9rem;
  line-height: 1.6;
  margin: 0;
}

/* ═══════════════════════════════════════════════════════════════════════════
   Stats — 极简内联
   ═══════════════════════════════════════════════════════════════════════════ */

.minimal-stats {
  max-width: 1200px;
  margin: 0 auto;
  padding: 3rem 2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0;
  border-top: 1px solid #ebebf0;
  border-bottom: 1px solid #ebebf0;
}

.minimal-stats__item {
  flex: 1;
  text-align: center;
}

.minimal-stats__value {
  font-size: 2.25rem;
  font-weight: 700;
  color: var(--ink-950, #0a0a0b);
  line-height: 1;
  letter-spacing: -0.03em;
}

.minimal-stats__label {
  font-size: 0.75rem;
  color: var(--ink-500, #525260);
  margin-top: 0.625rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 500;
}

.minimal-stats__divider {
  width: 1px;
  height: 36px;
  background: #ebebf0;
}

/* Contact */
.minimal-contact {
  max-width: 1200px;
  margin: 3rem auto 4rem;
  padding: 0 2rem;
  text-align: center;
  font-size: 0.875rem;
  color: var(--ink-500, #525260);
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.minimal-contact a {
  color: var(--ink-700, #25252d);
  text-decoration: none;
  transition: color 0.2s;
}

.minimal-contact a:hover {
  color: #7c5cff;
}

.minimal-contact .dot {
  color: #d4d4db;
}

/* ═══════════════════════════════════════════════════════════════════════════
   Responsive
   ═══════════════════════════════════════════════════════════════════════════ */

@media (max-width: 960px) {
  .home-gallery__grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .thumb-card__frame iframe {
    transform: scale(0.35);
  }
  .home-features__grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
}

@media (max-width: 640px) {
  .VPHero {
    padding: 2.5rem 1.5rem 1.5rem !important;
  }
  .VPHero .name { font-size: 2rem !important; }
  .VPHero .text { font-size: 1.125rem !important; }
  .VPHero .tagline { font-size: 0.9rem !important; }

  .home-gallery {
    margin: 1.5rem auto 3rem;
  }
  .home-gallery__grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  .thumb-card__frame iframe {
    transform: scale(0.45);
  }

  .minimal-stats {
    flex-wrap: wrap;
    gap: 1.5rem;
    padding: 2rem 1rem;
  }
  .minimal-stats__item {
    flex: 0 0 calc(50% - 0.75rem);
  }
  .minimal-stats__value { font-size: 1.75rem; }
  .minimal-stats__divider { display: none; }

  .minimal-contact {
    flex-direction: column;
    gap: 0.5rem;
  }
  .minimal-contact .dot { display: none; }
}
</style>
