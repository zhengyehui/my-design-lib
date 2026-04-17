---
layout: doc
title: 3D Tilt 3D倾斜卡片
---

# 3D Tilt 3D 倾斜卡片

::: tip 🎯 效果
鼠标悬停时卡片产生 3D 倾斜效果，配合光影变化，极具空间感。纯 CSS 实现基础版，JS 增强版可跟随鼠标角度。
:::

## 实时预览

<div style="display: flex; gap: 2rem; flex-wrap: wrap; padding: 2rem 0;">

  <div class="tilt-card">
    <div class="tilt-card__inner">
      <div class="tilt-card__shine"></div>
      <div class="tilt-card__icon">🎮</div>
      <div class="tilt-card__title">基础 3D</div>
      <div class="tilt-card__desc">鼠标悬停试试看！卡片会向左上方倾斜，产生 3D 空间感。</div>
    </div>
  </div>

  <div class="tilt-card tilt-card--gradient">
    <div class="tilt-card__inner">
      <div class="tilt-card__shine"></div>
      <div class="tilt-card__icon">🌈</div>
      <div class="tilt-card__title">渐变变体</div>
      <div class="tilt-card__desc">渐变背景 + 3D 倾斜，适合展示产品特性或定价卡片。</div>
    </div>
  </div>

  <div class="tilt-card tilt-card--glass">
    <div class="tilt-card__inner">
      <div class="tilt-card__shine"></div>
      <div class="tilt-card__icon">💎</div>
      <div class="tilt-card__title">玻璃变体</div>
      <div class="tilt-card__desc">毛玻璃 + 3D 倾斜的组合效果，高级感拉满。</div>
    </div>
  </div>

</div>

## 代码

```html
<!-- 基础用法 -->
<div class="tilt-card">
  <div class="tilt-card__inner">
    <div class="tilt-card__shine"></div>
    <div class="tilt-card__icon">🎮</div>
    <div class="tilt-card__title">标题</div>
    <div class="tilt-card__desc">描述内容...</div>
  </div>
</div>

<!-- 渐变变体 -->
<div class="tilt-card tilt-card--gradient">
  <div class="tilt-card__inner">...</div>
</div>
```

## JS 增强版（跟随鼠标）

```html
<div class="tilt-card tilt-card--js">
  <div class="tilt-card__inner" id="myTilt">
    <div class="tilt-card__icon">🎯</div>
    <div class="tilt-card__title">跟随鼠标</div>
    <div class="tilt-card__desc">鼠标在卡片上移动时，倾斜角度跟随变化。</div>
  </div>
</div>

<script>
const card = document.getElementById('myTilt');
card.parentElement.addEventListener('mousemove', (e) => {
  const rect = card.getBoundingClientRect();
  const x = (e.clientX - rect.left) / rect.width - 0.5;
  const y = (e.clientY - rect.top) / rect.height - 0.5;
  card.style.transform = `
    rotateY(${x * 20}deg) 
    rotateX(${-y * 20}deg) 
    translateZ(20px)
  `;
});
card.parentElement.addEventListener('mouseleave', () => {
  card.style.transform = '';
});
</script>
```

## 变体

| 变体 | Class | 效果 |
|------|-------|------|
| 默认 | `.tilt-card` | 深色背景 3D 倾斜 |
| 渐变 | `--gradient` | 紫粉渐变背景 |
| 玻璃 | `--glass` | 毛玻璃效果 |

## AI 使用说明

```
组件名: 3d-tilt
选择器: .tilt-card
结构: .tilt-card > .tilt-card__inner > (.tilt-card__shine + 内容)
变体: --gradient | --glass
JS增强: .tilt-card--js + mousemove 事件监听
关键属性: perspective: 1000px + transform-style: preserve-3d
注意: 内部元素用 translateZ() 实现深度差
```
