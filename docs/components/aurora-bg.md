---
layout: doc
title: Aurora 极光背景
---

# Aurora Background 极光背景

::: tip 🌌 效果
多色光球缓慢漂移 + 模糊，模拟北极光效果。适合 Hero 区域、landing page 头部、产品展示等需要视觉冲击力的场景。
:::

## 实时预览

<div class="aurora" style="margin: 1rem 0;">
  <div class="aurora__bg">
    <div class="aurora__blob aurora__blob--1"></div>
    <div class="aurora__blob aurora__blob--2"></div>
    <div class="aurora__blob aurora__blob--3"></div>
  </div>
  <div class="aurora__grid"></div>
  <div class="aurora__content" style="text-align: center;">
    <div style="font-size: 3rem; margin-bottom: 1rem;">🌌</div>
    <h2 style="font-size: 2rem; font-weight: 800; margin-bottom: 0.5rem; background: linear-gradient(135deg, #fff, #a5b4fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Aurora Background</h2>
    <p style="opacity: 0.8; max-width: 500px; margin: 0 auto;">三个模糊光球缓慢漂移，叠加网格纹理，打造深邃的极光效果。</p>
  </div>
</div>

## 日落变体

<div class="aurora aurora--sunset" style="margin: 1.5rem 0;">
  <div class="aurora__bg">
    <div class="aurora__blob aurora__blob--1"></div>
    <div class="aurora__blob aurora__blob--2"></div>
    <div class="aurora__blob aurora__blob--3"></div>
  </div>
  <div class="aurora__content" style="text-align: center;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🌅</div>
    <h3 style="font-size: 1.5rem; font-weight: 700;">Sunset Variant</h3>
    <p style="opacity: 0.7; font-size: 0.9rem;">橙红粉暖色调，适合活动页、节日主题</p>
  </div>
</div>

## 蓝色变体

<div class="aurora aurora--blue" style="margin: 1.5rem 0;">
  <div class="aurora__bg">
    <div class="aurora__blob aurora__blob--1"></div>
    <div class="aurora__blob aurora__blob--2"></div>
    <div class="aurora__blob aurora__blob--3"></div>
  </div>
  <div class="aurora__content" style="text-align: center;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🌊</div>
    <h3 style="font-size: 1.5rem; font-weight: 700;">Ocean Blue</h3>
    <p style="opacity: 0.7; font-size: 0.9rem;">蓝青冷色调，适合 SaaS、企业级产品</p>
  </div>
</div>

## 代码

```html
<div class="aurora">
  <div class="aurora__bg">
    <div class="aurora__blob aurora__blob--1"></div>
    <div class="aurora__blob aurora__blob--2"></div>
    <div class="aurora__blob aurora__blob--3"></div>
  </div>
  <div class="aurora__grid"></div>  <!-- 可选：网格纹理 -->
  <div class="aurora__content">
    <h2>你的内容</h2>
    <p>放在这里...</p>
  </div>
</div>

<!-- 日落变体 -->
<div class="aurora aurora--sunset">...</div>

<!-- 蓝色变体 -->
<div class="aurora aurora--blue">...</div>
```

## 变体

| 变体 | Class | 色调 | 适用场景 |
|------|-------|------|---------|
| 默认 | `.aurora` | 靛蓝+绿+粉 | 科技感、通用 |
| 蓝色 | `.aurora--blue` | 蓝+靛+青 | SaaS、企业 |
| 日落 | `.aurora--sunset` | 橙+红+粉 | 活动、节日 |

## AI 使用说明

```
组件名: aurora-bg
选择器: .aurora
结构: .aurora > .aurora__bg > 3×.aurora__blob + .aurora__content
变体: --blue | --sunset
可选: .aurora__grid (网格叠加层)
关键属性: filter: blur(80px) on blobs
注意: 容器需要 overflow: hidden + 相对定位
```
