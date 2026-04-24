---
layout: false
head:
  - - script
    - src: /pages/page-detail.js
      defer: true
title: Nexus 数据仪表盘
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
  <meta name="description" content="暗色模式数据分析仪表盘模板，侧边栏 + 统计卡片 + 图表 + 数据表格，纯 HTML+CSS。">
  <meta name="keywords" content="仪表盘, dashboard, 暗色, 数据可视化, 管理后台">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="article">
  <meta property="og:title" content="Nexus 数据仪表盘 — My Design Lib">
  <meta property="og:description" content="暗色模式数据分析仪表盘模板，侧边栏 + 统计卡片 + 图表 + 数据表格，纯 HTML+CSS。">
  <meta property="og:url" content="http://101.37.166.208:11930/pages/dashboard-dark.html">
  <link rel="canonical" href="http://101.37.166.208:11930/pages/dashboard-dark.html">
  <script type="application/ld+json">{"@context":"https://schema.org","@type":"CreativeWork","name":"Nexus 数据仪表盘 — My Design Lib","description":"暗色模式数据分析仪表盘模板，侧边栏 + 统计卡片 + 图表 + 数据表格，纯 HTML+CSS。","url":"http://101.37.166.208:11930/pages/dashboard-dark.html","genre":"dashboard","author":{"@type":"Organization","name":"My Design Lib"}}</script>


  <div class="detail-header">
    <a href="/pages/" class="back-link">← 返回画廊</a>
    <div class="detail-meta">
      <h1>Nexus 数据仪表盘</h1>
      <div class="detail-tags">
        <span class="tag">暗色</span><span class="tag">数据</span><span class="tag">管理后台</span>
        <span class="score">⭐ 9.0</span>
      </div>
    </div>
    <div class="detail-actions">
      <button class="action-btn active" onclick="showPreview()">👁 预览</button>
      <button class="action-btn" onclick="showCode()">📝 源码</button>
      <a href="/pages/dashboard-dark/index.html" target="_blank" class="action-btn">↗ 新窗口打开</a>
    </div>
  </div>
  <div class="detail-body">
    <div id="preview-panel" class="panel"><iframe src="/pages/dashboard-dark/index.html" sandbox="allow-scripts" loading="lazy"></iframe></div>
    <div id="code-panel" class="panel" style="display:none">
    <button id="copy-btn" class="copy-btn" onclick="copySourceCode()">📋 复制源码</button>
    <pre><code id="code-content">加载中...</code></pre>
  </div>
  </div>
  <div class="design-tips">
    <h2>💡 设计分析</h2>
    <div class="tips-grid">
      <div class="tip"><h3>布局结构</h3><p>左侧固定侧边栏 → 顶栏（搜索+头像）→ 统计卡片（4列）→ 图表区（2:1）→ 数据表格</p></div>
      <div class="tip"><h3>配色方案</h3><p>深色背景 (#0f0f14)，卡片 (#1a1a24)，边框 (#1e1e2a)。靛蓝紫强调，绿/橙/红状态色。</p></div>
      <div class="tip"><h3>亮点技巧</h3><p>• 侧边栏 active 右边框高亮<br>• 卡片 hover 边框变色<br>• conic-gradient 环形图<br>• 状态徽章区分表格行</p></div>
      <div class="tip"><h3>适用场景</h3><p>SaaS 管理后台、数据分析平台、CRM、运营看板</p></div>
    </div>
  </div>
  <div class="detail-footer">
    <a href="/pages/" class="back-btn">← 返回画廊</a>
    <div class="nav-prevnext">
      <a href="/pages/portfolio.html">← 创意作品集</a>
      <a href="/pages/checkout.html">电商结账页 →</a>
    </div>
  </div>
</div>
<style>
*{margin:0;padding:0;box-sizing:border-box}body{font-family:-apple-system,'Segoe UI',sans-serif}
.detail-nav{position:sticky;top:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:.8rem 2rem;background:rgba(15,15,20,.9);backdrop-filter:blur(12px);border-bottom:1px solid #1e1e2a}
.nav-logo{font-size:1.1rem;font-weight:800;color:#1e1b4b;text-decoration:none}
.nav-links{display:flex;gap:1.5rem;align-items:center}
.nav-links a{text-decoration:none;color:#4b5563;font-size:.9rem;font-weight:500;transition:color .2s}
.nav-links a:hover,.nav-links a.active{color:#6366f1}
.page-detail{max-width:1200px;margin:0 auto;padding:1rem 2rem;color:#e2e8f0}
.detail-header{padding:1rem 0}.back-link{color:#6366f1;text-decoration:none;font-size:.9rem;display:inline-block;margin-bottom:1rem}
.detail-meta h1{font-size:1.8rem;font-weight:800;margin-bottom:.5rem}
.detail-tags{display:flex;gap:.5rem;align-items:center;flex-wrap:wrap}
.tag{padding:.3rem .8rem;background:#1a1a24;border-radius:8px;font-size:.8rem;color:#888}
.score{font-size:.9rem;font-weight:700;margin-left:.5rem}
.detail-actions{display:flex;gap:.5rem;margin-top:1rem;flex-wrap:wrap}
.action-btn{padding:.5rem 1.2rem;border:1px solid #333;border-radius:8px;background:none;cursor:pointer;font-size:.85rem;color:#888;text-decoration:none;transition:all .2s}
.action-btn:hover,.action-btn.active{border-color:#6366f1;color:#6366f1}
.detail-body{margin:1.5rem 0;border:1px solid #1e1e2a;border-radius:12px;overflow:hidden;background:#0a0a0a}
.panel iframe{width:100%;height:70vh;border:none}
.panel pre{padding:1.5rem;overflow:auto;max-height:70vh;background:#1e1e2e;color:#cdd6f4;font-size:.85rem;line-height:1.6}
.panel code{font-family:monospace;white-space:pre}
.design-tips{margin:2rem 0}.design-tips h2{font-size:1.3rem;font-weight:700;margin-bottom:1rem}
.tips-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1rem}
.tip{padding:1.2rem;border:1px solid #1e1e2a;border-radius:12px}
.tip h3{font-size:.95rem;font-weight:700;margin-bottom:.5rem;color:#6366f1}
.tip p{font-size:.85rem;color:#888;line-height:1.6}
.detail-footer{display:flex;justify-content:space-between;align-items:center;padding:2rem 0;margin-top:2rem;border-top:1px solid #1e1e2a}
.back-btn{color:#6366f1;text-decoration:none;font-weight:600}
.nav-prevnext{display:flex;gap:2rem}
.nav-prevnext a{color:#888;text-decoration:none;font-size:.9rem}
.nav-prevnext a:hover{color:#6366f1}

</style>
