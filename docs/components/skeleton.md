---
layout: doc
title: Skeleton 骨架屏
---

# Skeleton 骨架屏加载

::: tip 💀 效果
内容加载前的闪烁占位屏，比"Loading..."文字高级 10 倍。shimmer 光效从左到右扫过，暗示内容即将到来。
:::

## 实时预览

<div style="display: flex; gap: 2rem; flex-wrap: wrap; padding: 1rem 0;">

  <!-- 卡片骨架 -->
  <div class="skeleton-card" style="width: 300px;">
    <div class="skeleton-card__image"></div>
    <div class="skeleton-card__body">
      <div class="skeleton-card__line" style="width: 70%; height: 1.1em;"></div>
      <div class="skeleton-card__line"></div>
      <div class="skeleton-card__line"></div>
      <div class="skeleton-card__line"></div>
    </div>
  </div>

  <!-- 文本骨架 -->
  <div style="flex: 1; min-width: 250px;">
    <div class="skeleton skeleton--title" style="margin-bottom: 1.5rem;"></div>
    <div class="skeleton skeleton--text"></div>
    <div class="skeleton skeleton--text"></div>
    <div class="skeleton skeleton--text" style="width: 80%;"></div>
    <div class="skeleton skeleton--text" style="width: 55%; margin-bottom: 2rem;"></div>
    
    <div style="display: flex; gap: 1rem; align-items: center; margin-bottom: 1.5rem;">
      <div class="skeleton skeleton--avatar"></div>
      <div style="flex: 1;">
        <div class="skeleton skeleton--text" style="width: 40%; margin-bottom: 0.4em;"></div>
        <div class="skeleton skeleton--text-sm"></div>
      </div>
    </div>
    
    <div class="skeleton skeleton--button"></div>
  </div>

</div>

## 暗色变体

<div style="background: #1e293b; padding: 2rem; border-radius: 16px; margin-top: 1rem;">
  <div style="display: flex; gap: 1.5rem;">
    <div style="flex: 1;">
      <div class="skeleton skeleton--dark skeleton--title" style="width: 50%;"></div>
      <div class="skeleton skeleton--dark skeleton--text"></div>
      <div class="skeleton skeleton--dark skeleton--text" style="width: 70%;"></div>
      <div class="skeleton skeleton--dark skeleton--text" style="width: 90%;"></div>
    </div>
    <div class="skeleton skeleton--dark skeleton--image" style="width: 200px;"></div>
  </div>
</div>

## 代码

```html
<!-- 卡片骨架 -->
<div class="skeleton-card">
  <div class="skeleton-card__image"></div>
  <div class="skeleton-card__body">
    <div class="skeleton-card__line" style="width: 70%;"></div>
    <div class="skeleton-card__line"></div>
    <div class="skeleton-card__line"></div>
  </div>
</div>

<!-- 文本骨架 -->
<div class="skeleton skeleton--title"></div>
<div class="skeleton skeleton--text"></div>
<div class="skeleton skeleton--text" style="width: 60%;"></div>

<!-- 头像 + 文字 -->
<div style="display: flex; gap: 1rem;">
  <div class="skeleton skeleton--avatar"></div>
  <div style="flex: 1;">
    <div class="skeleton skeleton--text" style="width: 40%;"></div>
    <div class="skeleton skeleton--text-sm"></div>
  </div>
</div>
```

## 预设形状

| 形状 | Class | 尺寸 |
|------|-------|------|
| 标题 | `.skeleton--title` | 1.5em 高, 40% 宽 |
| 文本行 | `.skeleton--text` | 1em 高, 100% 宽 |
| 短文本 | `.skeleton--text-sm` | 0.75em 高, 60% 宽 |
| 头像 | `.skeleton--avatar` | 48×48 圆形 |
| 大头像 | `.skeleton--avatar-lg` | 80×80 圆形 |
| 图片 | `.skeleton--image` | 100% 宽, 200px 高 |
| 按钮 | `.skeleton--button` | 120×40px |
| 卡片 | `.skeleton--card` | 100% 宽, 280px 高 |

## AI 使用说明

```
组件名: skeleton
选择器: .skeleton
变体: --text | --title | --avatar | --image | --button | --card | --dark
动画: shimmer (默认) | pulse (.skeleton--pulse)
组合: .skeleton-card (完整卡片骨架)
关键属性: overflow: hidden + ::after shimmer 动画
```
