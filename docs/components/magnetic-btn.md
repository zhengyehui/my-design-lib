---
layout: doc
title: Magnetic Button 磁性按钮
---

# Magnetic Button 磁性按钮

::: tip 🧲 效果
悬停时按钮微微放大并发光，像被磁力吸引一样。配合粒子效果和渐变光晕，让 CTA 按钮成为页面焦点。
:::

## 实时预览

<div style="display: flex; gap: 1.5rem; flex-wrap: wrap; align-items: center; padding: 2rem 0;">

  <button class="magnetic-btn">
    <span class="magnetic-btn__text">🚀 主要按钮</span>
  </button>

  <button class="magnetic-btn magnetic-btn--outline">
    <span class="magnetic-btn__text">✨ 描边按钮</span>
  </button>

  <button class="magnetic-btn magnetic-btn--ghost">
    <span class="magnetic-btn__text">👻 幽灵按钮</span>
  </button>

  <button class="magnetic-btn magnetic-btn--glow">
    <span class="magnetic-btn__text">💡 发光按钮</span>
  </button>

</div>

## 暗色背景效果

<div style="background: #0f172a; padding: 3rem; border-radius: 20px; margin-top: 1rem; text-align: center;">
  <p style="color: #94a3b8; margin-bottom: 1.5rem;">在深色背景上效果更突出 👇</p>
  <div style="display: flex; gap: 1.5rem; flex-wrap: wrap; justify-content: center;">
    <button class="magnetic-btn">
      <span class="magnetic-btn__text">开始使用 →</span>
    </button>
    <button class="magnetic-btn magnetic-btn--glow">
      <span class="magnetic-btn__text">⚡ 立即体验</span>
    </button>
  </div>
</div>

## 代码

```html
<!-- 基础 -->
<button class="magnetic-btn">
  <span class="magnetic-btn__text">按钮文字</span>
</button>

<!-- 描边 -->
<button class="magnetic-btn magnetic-btn--outline">
  <span class="magnetic-btn__text">描边按钮</span>
</button>

<!-- 幽灵 -->
<button class="magnetic-btn magnetic-btn--ghost">
  <span class="magnetic-btn__text">幽灵按钮</span>
</button>

<!-- 发光 -->
<button class="magnetic-btn magnetic-btn--glow">
  <span class="magnetic-btn__text">发光按钮</span>
</button>
```

## JS 磁性增强

```html
<button class="magnetic-btn magnetic-btn--magnetic" id="magBtn">
  <span class="magnetic-btn__text">跟随鼠标</span>
</button>

<script>
const btn = document.getElementById('magBtn');
btn.addEventListener('mousemove', (e) => {
  const rect = btn.getBoundingClientRect();
  const x = e.clientX - rect.left - rect.width / 2;
  const y = e.clientY - rect.top - rect.height / 2;
  btn.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px) scale(1.05)`;
});
btn.addEventListener('mouseleave', () => {
  btn.style.transform = '';
});
</script>
```

## 变体

| 变体 | Class | 效果 |
|------|-------|------|
| 默认 | `.magnetic-btn` | 渐变填充，悬停发光 |
| 描边 | `--outline` | 边框样式，悬停填充 |
| 幽灵 | `--ghost` | 半透明，低调优雅 |
| 发光 | `--glow` | 持续发光 + 悬停增强 |

## AI 使用说明

```
组件名: magnetic-btn
选择器: .magnetic-btn
结构: .magnetic-btn > .magnetic-btn__text
变体: --outline | --ghost | --glow
JS增强: --magnetic + mousemove (磁性跟随)
关键属性: cubic-bezier(0.23, 1, 0.32, 1) 缓动
注意: 文字必须包在 .magnetic-btn__text 中以保持层级
```
