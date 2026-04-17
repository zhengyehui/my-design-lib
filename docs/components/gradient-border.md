---
layout: doc
title: Gradient Border 渐变边框
---

# Gradient Border 动画渐变边框

::: tip 🌈 效果
边框颜色持续旋转流动，视觉冲击力极强。用 `conic-gradient` + `@property` 实现，纯 CSS 无 JS。
:::

## 实时预览

<div style="display: flex; gap: 2rem; flex-wrap: wrap; align-items: flex-start; padding: 2rem 0;">

  <div class="gradient-border-wrap">
    <div class="gradient-border-wrap__inner">
      <div style="font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem;">🚀 默认速度</div>
      <div style="opacity: 0.7; font-size: 0.9rem;">渐变边框持续旋转<br>3秒一圈</div>
    </div>
  </div>

  <div class="gradient-border-wrap gradient-border-wrap--fast gradient-border-wrap--rainbow">
    <div class="gradient-border-wrap__inner">
      <div style="font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem;">⚡ 彩虹加速</div>
      <div style="opacity: 0.7; font-size: 0.9rem;">彩虹色 + 快速旋转<br>1.5秒一圈</div>
    </div>
  </div>

</div>

<div style="display: flex; gap: 2rem; flex-wrap: wrap; align-items: flex-start; padding: 1rem 0;">

  <div class="gradient-border-wrap gradient-border-wrap--slow">
    <div class="gradient-border-wrap__inner">
      <div style="font-size: 1.25rem; font-weight: 700; margin-bottom: 0.5rem;">🐢 优雅慢速</div>
      <div style="opacity: 0.7; font-size: 0.9rem;">6秒一圈，适合高端品牌</div>
    </div>
  </div>

  <div class="gradient-border-wrap gradient-border-wrap--dashed">
    <div class="gradient-border-wrap__inner">
      <div style="font-size: 1.25rem; font-weight: 700; margin-bottom: 0.5rem;">✏️ 虚线边框</div>
      <div style="opacity: 0.7; font-size: 0.9rem;">虚线渐变，适合创意场景</div>
    </div>
  </div>

</div>

## 代码

```html
<!-- 基础用法 -->
<div class="gradient-border-wrap">
  <div class="gradient-border-wrap__inner">
    <h3>标题</h3>
    <p>内容...</p>
  </div>
</div>

<!-- 彩虹 + 快速 -->
<div class="gradient-border-wrap gradient-border-wrap--fast gradient-border-wrap--rainbow">
  <div class="gradient-border-wrap__inner">...</div>
</div>

<!-- 虚线版 -->
<div class="gradient-border-wrap gradient-border-wrap--dashed">
  <div class="gradient-border-wrap__inner">...</div>
</div>
```

```css
<link rel="stylesheet" href="/src/components/gradient-border/gradient-border.css">
```

## 变体

| 变体 | Class | 效果 |
|------|-------|------|
| 默认 | `.gradient-border-wrap` | 靛蓝→粉红渐变，3s 旋转 |
| 慢速 | `--slow` | 6s 旋转，优雅感 |
| 快速 | `--fast` | 1.5s 旋转，活力感 |
| 彩虹 | `--rainbow` | 7色彩虹渐变 |
| 虚线 | `--dashed` | 虚线边框，内部透明 |

## 技术原理

```
┌─────────────────────────────────┐
│  conic-gradient (旋转背景)       │
│  ┌───────────────────────────┐  │
│  │  inner div (盖住中心)      │  │
│  │  background: #0f172a      │  │
│  │  border-radius: 15px      │  │
│  └───────────────────────────┘  │
│  ↑ 露出 3px 形成边框             │
└─────────────────────────────────┘
```

## AI 使用说明

```
组件名: gradient-border
选择器: .gradient-border-wrap
容器: .gradient-border-wrap__inner (必须嵌套)
变体: --slow | --fast | --rainbow | --dashed
依赖: @property --gb-angle (需要现代浏览器)
注意: 外层 padding 控制边框宽度(默认3px)
```
