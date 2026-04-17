---
layout: doc
title: Glassmorphism 毛玻璃
---

# Glassmorphism 毛玻璃卡片

::: tip 💎 视觉效果
半透明背景 + 模糊 + 边框高光，打造层次感十足的 UI。适合放在有背景图/渐变的容器中。
:::

## 实时预览

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 3rem; border-radius: 20px; display: flex; gap: 1.5rem; flex-wrap: wrap; justify-content: center;">
  <div class="glass-card" style="max-width: 280px;">
    <div class="glass-card__icon">✨</div>
    <div class="glass-card__title">Light Glass</div>
    <div class="glass-card__desc">经典毛玻璃效果，半透明白色背景 + 模糊。适合放在深色渐变背景上。</div>
  </div>
  <div class="glass-card glass-card--neon" style="max-width: 280px;">
    <div class="glass-card__icon">💜</div>
    <div class="glass-card__title">Neon Glass</div>
    <div class="glass-card__desc">霓虹变体，带发光边框效果。适合科技感、暗色主题的界面。</div>
  </div>
</div>

## 暗色背景效果

<div style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); padding: 3rem; border-radius: 20px; margin-top: 1.5rem;">
  <div style="display: flex; gap: 1.5rem; flex-wrap: wrap;">
    <div class="glass-card glass-card--dark" style="max-width: 260px;">
      <div class="glass-card__icon">🌙</div>
      <div class="glass-card__title">Dark Glass</div>
      <div class="glass-card__desc">暗色毛玻璃，适合深色模式界面。</div>
    </div>
    <div class="glass-card" style="max-width: 260px;">
      <div class="glass-card__icon">🔮</div>
      <div class="glass-card__title">Default Glass</div>
      <div class="glass-card__desc">默认变体，自适应背景色。</div>
    </div>
    <div class="glass-card glass-card--light" style="max-width: 260px;">
      <div class="glass-card__icon">☁️</div>
      <div class="glass-card__title">Light Glass</div>
      <div class="glass-card__desc">亮色毛玻璃，适合浅色背景。</div>
    </div>
  </div>
</div>

## 代码

```html
<!-- 基础用法 - 放在有背景的容器中 -->
<div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 2rem;">
  <div class="glass-card">
    <div class="glass-card__icon">✨</div>
    <div class="glass-card__title">卡片标题</div>
    <div class="glass-card__desc">卡片描述内容...</div>
  </div>
</div>

<!-- 霓虹变体 -->
<div class="glass-card glass-card--neon">
  <div class="glass-card__title">霓虹卡片</div>
  <div class="glass-card__desc">带发光边框</div>
</div>
```

```css
/* 引入 */
<link rel="stylesheet" href="/src/components/glassmorphism/glassmorphism.css">
```

## 变体

| 变体 | Class | 适用场景 |
|------|-------|---------|
| 默认 | `.glass-card` | 深色渐变背景 |
| 暗色 | `.glass-card--dark` | 深色模式 |
| 亮色 | `.glass-card--light` | 浅色背景 |
| 霓虹 | `.glass-card--neon` | 科技感、暗色主题 |

## AI 使用说明

```
组件名: glassmorphism
选择器: .glass-card
变体: .glass-card--dark | .glass-card--light | .glass-card--neon
子元素: .glass-card__icon | .glass-card__title | .glass-card__desc
依赖: 需要放在有背景色/渐变/图片的容器中才能看到效果
关键属性: backdrop-filter: blur(20px) saturate(180%)
```
