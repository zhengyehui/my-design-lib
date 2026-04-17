---
layout: false
title: 创意作品集
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
  <meta name="description" content="暗色系个人作品集页面模板，渐变背景 + 作品网格 + 技能展示，纯 HTML+CSS，适合设计师和开发者。">
  <meta name="keywords" content="作品集, portfolio, 暗色, 个人主页, 前端模板">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="article">
  <meta property="og:title" content="创意作品集 — My Design Lib">
  <meta property="og:description" content="暗色系个人作品集页面模板，渐变背景 + 作品网格 + 技能展示，纯 HTML+CSS，适合设计师和开发者。">
  <meta property="og:url" content="http://101.37.166.208:11930/pages/portfolio.html">
  <link rel="canonical" href="http://101.37.166.208:11930/pages/portfolio.html">
  <script type="application/ld+json">{"@context":"https://schema.org","@type":"CreativeWork","name":"创意作品集 — My Design Lib","description":"暗色系个人作品集页面模板，渐变背景 + 作品网格 + 技能展示，纯 HTML+CSS，适合设计师和开发者。","url":"http://101.37.166.208:11930/pages/portfolio.html","genre":"portfolio","author":{"@type":"Organization","name":"My Design Lib"}}</script>


  <div class="detail-header">
    <a href="/pages/" class="back-link">← 返回画廊</a>
    <div class="detail-meta">
      <h1>创意作品集</h1>
      <div class="detail-tags">
        <span class="tag">暗色</span><span class="tag">作品集</span><span class="tag">动效</span>
        <span class="score">⭐ 9.5</span>
      </div>
    </div>
    <div class="detail-actions">
      <button class="action-btn active" onclick="showPreview()">👁 预览</button>
      <button class="action-btn" onclick="showCode()">📝 源码</button>
      <a href="/pages/portfolio/index.html" target="_blank" class="action-btn">↗ 新窗口打开</a>
    </div>
  </div>
  <div class="detail-body">
    <div id="preview-panel" class="panel"><iframe src="/pages/portfolio/index.html" sandbox="allow-scripts" loading="lazy"></iframe></div>
    <div id="code-panel" class="panel" style="display:none"><pre><code id="code-content">加载中...</code></pre></div>
  </div>
  <div class="design-tips">
    <h2>💡 设计分析</h2>
    <div class="tips-grid">
      <div class="tip"><h3>布局结构</h3><p>全屏 Hero → 作品网格（2列）→ 关于我（图文并排）→ 联系区 → 页脚</p></div>
      <div class="tip"><h3>配色方案</h3><p>纯黑底 (#0a0a0a)，渐变强调色（靛蓝→粉），灰色系文字层次分明</p></div>
      <div class="tip"><h3>亮点技巧</h3><p>• Hero 双色 radial-gradient 氛围<br>• 作品卡片 hover 图片放大+遮罩<br>• 渐变文字 background-clip:text<br>• 技能标签 pill 形状</p></div>
      <div class="tip"><h3>适用场景</h3><p>设计师/开发者个人主页、自由职业者、创意工作室</p></div>
    </div>
  </div>
  <div class="detail-footer">
    <a href="/pages/" class="back-btn">← 返回画廊</a>
    <div class="nav-prevnext">
      <a href="/pages/saas-landing.html">← SaaS 落地页</a>
      <a href="/pages/dashboard-dark.html">数据仪表盘 →</a>
    </div>
  </div>
</div>
<style>
*{margin:0;padding:0;box-sizing:border-box}body{font-family:-apple-system,'Segoe UI',sans-serif}
.detail-nav{position:sticky;top:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:.8rem 2rem;background:rgba(10,10,10,.9);backdrop-filter:blur(12px);border-bottom:1px solid #1e1e2a}
.nav-logo{font-size:1.1rem;font-weight:800;color:#6366f1;text-decoration:none}
.nav-links{display:flex;gap:1.5rem;align-items:center}
.nav-links a{text-decoration:none;color:#888;font-size:.9rem;font-weight:500;transition:color .2s}
.nav-links a:hover,.nav-links a.active{color:#6366f1}
.page-detail{max-width:1200px;margin:0 auto;padding:1rem 2rem;color:#e2e8f0}
.detail-header{padding:1rem 0}.back-link{color:#6366f1;text-decoration:none;font-size:.9rem;display:inline-block;margin-bottom:1rem}.back-link:hover{text-decoration:underline}
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
<script>
function showPreview(){document.getElementById('preview-panel').style.display='block';document.getElementById('code-panel').style.display='none';document.querySelectorAll('.action-btn').forEach((b,i)=>{b.classList.toggle('active',i===0)})}
function showCode(){document.getElementById('preview-panel').style.display='none';document.getElementById('code-panel').style.display='block';document.querySelectorAll('.action-btn').forEach((b,i)=>{b.classList.toggle('active',i===1)});fetch('/pages/portfolio/index.html').then(r=>r.text()).then(t=>{document.getElementById('code-content').textContent=t})}
</script>
