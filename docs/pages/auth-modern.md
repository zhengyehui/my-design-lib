---
layout: false
head:
  - - script
    - src: /pages/page-detail.js
      defer: true
title: AuthKit 现代认证页
---

<div class="page-detail">
  <nav class="detail-nav">
    <a href="/" class="nav-logo">◆ My Design Lib</a>
    <div class="nav-links">
      <a href="/">首页</a>
      <a href="/components/button.html">组件</a>
      <a href="/tokens/colors.html">设计变量</a>
      <a href="/pages/" class="active">🎨 页面画廊</a>
      <a href="/sponsor.html">赞助</a>
    </div>
  </nav>

  <!-- SEO Meta -->
  <meta name="description" content="现代认证登录页面模板，灵感来自 AuthKit/WorkOS，包含登录表单、社交登录、OTP 验证、明暗主题切换，纯 HTML+CSS 零依赖。">
  <meta name="keywords" content="登录页, 认证页面, AuthKit, 社交登录, 表单设计">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="article">
  <meta property="og:title" content="AuthKit 现代认证页 — My Design Lib">
  <meta property="og:description" content="现代认证登录页面模板，灵感来自 AuthKit/WorkOS，包含登录表单、社交登录、明暗主题切换。">
  <meta property="og:url" content="http://101.37.166.208:11930/pages/auth-modern.html">
  <link rel="canonical" href="http://101.37.166.208:11930/pages/auth-modern.html">
  <script type="application/ld+json">{"@context":"https://schema.org","@type":"CreativeWork","name":"AuthKit 现代认证页 — My Design Lib","description":"现代认证登录页面模板，灵感来自 AuthKit/WorkOS，包含登录表单、社交登录、明暗主题切换。","url":"http://101.37.166.208:11930/pages/auth-modern.html","genre":"app","author":{"@type":"Organization","name":"My Design Lib"}}</script>


  <div class="detail-header">
    <a href="/pages/" class="back-link">← 返回画廊</a>
    <div class="detail-meta">
      <h1>AuthKit 现代认证页</h1>
      <div class="detail-tags">
        <span class="tag">认证</span><span class="tag">登录</span><span class="tag">社交登录</span><span class="tag">明暗主题</span>
        <span class="score">⭐ 9.4</span>
      </div>
    </div>
    <div class="detail-actions">
      <button class="action-btn active" onclick="showPreview()">👁 预览</button>
      <button class="action-btn" onclick="showCode()">📝 源码</button>
      <a href="/pages/auth-modern/index.html" target="_blank" class="action-btn">↗ 新窗口打开</a>
    </div>
  </div>

  <div class="detail-body">
    <div id="preview-panel" class="panel"><iframe src="/pages/auth-modern/index.html" sandbox="allow-scripts" loading="lazy"></iframe></div>
    <div id="code-panel" class="panel" style="display:none">
    <button id="copy-btn" class="copy-btn" onclick="copySourceCode()">📋 复制源码</button>
    <pre><code id="code-content">加载中...</code></pre>
  </div>
  </div>

  <div class="design-tips">
    <h2>💡 设计分析</h2>
    <div class="tips-grid">
      <div class="tip"><h3>布局结构</h3><p>左右分栏布局：左侧品牌展示区（渐变背景+浮动动画）+ 右侧表单区。移动端自动切换为上下布局。</p></div>
      <div class="tip"><h3>配色方案</h3><p>左侧深色渐变背景 (#0f0f14 → #1a1a2e)，右侧浅色表单区。主色靛蓝紫 (#6366f1) 用于按钮和焦点态。</p></div>
      <div class="tip"><h3>亮点技巧</h3><p>• 品牌区浮动光球动画<br>• 社交登录按钮（Google/Microsoft）<br>• 明暗主题切换功能<br>• 输入框焦点态发光效果</p></div>
      <div class="tip"><h3>适用场景</h3><p>SaaS 产品登录页、企业应用认证、开发者平台、需要社交登录的场景</p></div>
    </div>
  </div>

  <div class="detail-footer">
    <a href="/pages/" class="back-btn">← 返回画廊</a>
    <div class="nav-prevnext">
      <a href="/pages/studio-creative.html">← VOID 创意工作室</a>
      <a href="/pages/product-minimal.html">FlowDesk 极简产品页 →</a>
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
