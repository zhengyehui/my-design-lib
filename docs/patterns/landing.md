# Landing Page 落地页

完整的落地页布局模式，组合 Hero + Features + CTA。

## 结构

```
┌──────────────────────────┐
│        Hero              │  ← hero.html
│   标题 + 描述 + CTA      │
├──────────────────────────┤
│     Features Grid        │  ← card.html × 3
│   ┌─────┐ ┌─────┐       │
│   │Card │ │Card │ ...   │
│   └─────┘ └─────┘       │
├──────────────────────────┤
│        CTA Section       │  ← button.html
│   行动号召 + 按钮        │
└──────────────────────────┘
```

## 组件清单

| 区域 | 组件 | 文件 |
|------|------|------|
| 首屏 | Hero | `src/components/hero/hero.html` |
| 特性展示 | Card × 3 | `src/components/card/card.html` |
| 行动号召 | Button | `src/components/button/button.html` |

## 设计原则

1. **Hero 占满首屏**，不要让用户滚动才能看到核心信息
2. **Features 用 3 列 grid**，移动端自动变单列
3. **CTA 重复出现**，至少首屏和底部各一个
4. **视觉节奏**：大留白 → 内容密集 → 大留白
