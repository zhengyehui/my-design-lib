---
layout: false
title: 太空主题 404
---

<div class="page-detail">
  <div class="detail-header">
    <a href="/pages/" class="back-link">← 返回画廊</a>
    <div class="detail-meta">
      <h1>太空主题 404</h1>
      <div class="detail-tags">
        <span class="tag">404</span>
        <span class="tag">动效</span>
        <span class="tag">创意</span>
        <span class="score">⭐ 9.3</span>
      </div>
    </div>
    <div class="detail-actions">
      <button class="action-btn active" onclick="showPreview()">👁 预览</button>
      <button class="action-btn" onclick="showCode()">📝 源码</button>
      <a href="/pages/404-creative/index.html" target="_blank" class="action-btn">↗ 新窗口打开</a>
    </div>
  </div>
  <div class="detail-body">
    <div id="preview-panel" class="panel"><iframe src="/pages/404-creative/index.html" sandbox="allow-scripts" loading="lazy"></iframe></div>
    <div id="code-panel" class="panel" style="display:none"><pre><code id="code-content">加载中...</code></pre></div>
  </div>
  <div class="design-tips">
    <h2>💡 设计分析</h2>
    <div class="tips-grid">
      <div class="tip"><h3>布局结构</h3><p>全屏居中布局：旋转 emoji → 渐变 404 数字 → 标题 → 描述 → 操作按钮 → 搜索提示</p></div>
      <div class="tip"><h3>配色方案</h3><p>纯黑底 (#0a0a0a)，404 数字用多色渐变动画（靛蓝→紫→粉→橙），装饰元素半透明。</p></div>
      <div class="tip"><h3>亮点技巧</h3><p>• JS 动态生成 100 颗闪烁星星<br>• background-size: 300% 渐变动画<br>• 宇宙元素漂浮动画（随机位置/时长）<br>• 行星脉冲呼吸效果</p></div>
      <div class="tip"><h3>适用场景</h3><p>创意网站、个人博客、品牌官网的 404 页面，让错误页也成为亮点</p></div>
    </div>
  </div>
</div>
<style>
.page-detail{max-width:1200px;margin:0 auto;padding:1rem 2rem}.detail-header{padding:1rem 0}.back-link{color:var(--vp-c-brand-1);text-decoration:none;font-size:.9rem;display:inline-block;margin-bottom:1rem}.detail-meta h1{font-size:1.8rem;font-weight:800;margin-bottom:.5rem}.detail-tags{display:flex;gap:.5rem;align-items:center;flex-wrap:wrap}.tag{padding:.3rem .8rem;background:var(--vp-c-bg-soft);border-radius:8px;font-size:.8rem;color:var(--vp-c-text-2)}.score{font-size:.9rem;font-weight:700;margin-left:.5rem}.detail-actions{display:flex;gap:.5rem;margin-top:1rem;flex-wrap:wrap}.action-btn{padding:.5rem 1.2rem;border:1px solid var(--vp-c-divider);border-radius:8px;background:none;cursor:pointer;font-size:.85rem;color:var(--vp-c-text-2);text-decoration:none;transition:all .2s}.action-btn:hover,.action-btn.active{border-color:var(--vp-c-brand-1);color:var(--vp-c-brand-1)}.detail-body{margin:1.5rem 0;border:1px solid var(--vp-c-divider);border-radius:12px;overflow:hidden;background:#fff}.panel iframe{width:100%;height:70vh;border:none}.panel pre{padding:1.5rem;overflow:auto;max-height:70vh;background:#1e1e2e;color:#cdd6f4;font-size:.85rem;line-height:1.6}.panel code{font-family:monospace;white-space:pre}.design-tips{margin:2rem 0}.design-tips h2{font-size:1.3rem;font-weight:700;margin-bottom:1rem}.tips-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1rem}.tip{padding:1.2rem;border:1px solid var(--vp-c-divider);border-radius:12px}.tip h3{font-size:.95rem;font-weight:700;margin-bottom:.5rem;color:var(--vp-c-brand-1)}.tip p{font-size:.85rem;color:var(--vp-c-text-2);line-height:1.6}
</style>
<script>
function showPreview(){document.getElementById('preview-panel').style.display='block';document.getElementById('code-panel').style.display='none';document.querySelectorAll('.action-btn').forEach((b,i)=>{b.classList.toggle('active',i===0)})}
function showCode(){document.getElementById('preview-panel').style.display='none';document.getElementById('code-panel').style.display='block';document.querySelectorAll('.action-btn').forEach((b,i)=>{b.classList.toggle('active',i===1)});fetch('/pages/404-creative/index.html').then(r=>r.text()).then(t=>{document.getElementById('code-content').textContent=t})}
</script>
