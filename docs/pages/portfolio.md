---
layout: false
title: 创意作品集
---

<div class="page-detail">
  <div class="detail-header">
    <a href="/pages/" class="back-link">← 返回画廊</a>
    <div class="detail-meta">
      <h1>创意作品集</h1>
      <div class="detail-tags">
        <span class="tag">暗色</span>
        <span class="tag">作品集</span>
        <span class="tag">动效</span>
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
    <div id="preview-panel" class="panel">
      <iframe src="/pages/portfolio/index.html" sandbox="allow-scripts" loading="lazy"></iframe>
    </div>
    <div id="code-panel" class="panel" style="display:none">
      <pre><code id="code-content">加载中...</code></pre>
    </div>
  </div>
  <div class="design-tips">
    <h2>💡 设计分析</h2>
    <div class="tips-grid">
      <div class="tip"><h3>布局结构</h3><p>全屏 Hero → 作品网格（2列）→ 关于我（图文并排）→ 联系区 → 页脚</p></div>
      <div class="tip"><h3>配色方案</h3><p>纯黑底 (#0a0a0a)，渐变强调色（靛蓝 #6366f1 → 粉色 #ec4899），文字用灰色系层次分明</p></div>
      <div class="tip"><h3>亮点技巧</h3><p>• Hero 背景双色 radial-gradient 营造氛围<br>• 作品卡片 hover 时图片放大 + 遮罩淡入<br>• 渐变文字 (background-clip: text)<br>• 技能标签用 pill 形状边框设计</p></div>
      <div class="tip"><h3>适用场景</h3><p>设计师/开发者个人主页、自由职业者展示页、创意工作室</p></div>
    </div>
  </div>
</div>
<style>
.page-detail { max-width: 1200px; margin: 0 auto; padding: 1rem 2rem; }
.detail-header { padding: 1rem 0; }
.back-link { color: var(--vp-c-brand-1); text-decoration: none; font-size: 0.9rem; display: inline-block; margin-bottom: 1rem; }
.detail-meta h1 { font-size: 1.8rem; font-weight: 800; margin-bottom: 0.5rem; }
.detail-tags { display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap; }
.tag { padding: 0.3rem 0.8rem; background: var(--vp-c-bg-soft); border-radius: 8px; font-size: 0.8rem; color: var(--vp-c-text-2); }
.score { font-size: 0.9rem; font-weight: 700; margin-left: 0.5rem; }
.detail-actions { display: flex; gap: 0.5rem; margin-top: 1rem; flex-wrap: wrap; }
.action-btn { padding: 0.5rem 1.2rem; border: 1px solid var(--vp-c-divider); border-radius: 8px; background: none; cursor: pointer; font-size: 0.85rem; color: var(--vp-c-text-2); text-decoration: none; transition: all 0.2s; }
.action-btn:hover, .action-btn.active { border-color: var(--vp-c-brand-1); color: var(--vp-c-brand-1); }
.detail-body { margin: 1.5rem 0; border: 1px solid var(--vp-c-divider); border-radius: 12px; overflow: hidden; background: #fff; }
.panel iframe { width: 100%; height: 70vh; border: none; }
.panel pre { padding: 1.5rem; overflow: auto; max-height: 70vh; background: #1e1e2e; color: #cdd6f4; font-size: 0.85rem; line-height: 1.6; }
.panel code { font-family: monospace; white-space: pre; }
.design-tips { margin: 2rem 0; }
.design-tips h2 { font-size: 1.3rem; font-weight: 700; margin-bottom: 1rem; }
.tips-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; }
.tip { padding: 1.2rem; border: 1px solid var(--vp-c-divider); border-radius: 12px; }
.tip h3 { font-size: 0.95rem; font-weight: 700; margin-bottom: 0.5rem; color: var(--vp-c-brand-1); }
.tip p { font-size: 0.85rem; color: var(--vp-c-text-2); line-height: 1.6; }
</style>
<script>
function showPreview() { document.getElementById('preview-panel').style.display='block'; document.getElementById('code-panel').style.display='none'; document.querySelectorAll('.action-btn').forEach((b,i)=>{b.classList.toggle('active',i===0)})}
function showCode() { document.getElementById('preview-panel').style.display='none'; document.getElementById('code-panel').style.display='block'; document.querySelectorAll('.action-btn').forEach((b,i)=>{b.classList.toggle('active',i===1)}); fetch('/pages/portfolio/index.html').then(r=>r.text()).then(t=>{document.getElementById('code-content').textContent=t}) }
</script>
