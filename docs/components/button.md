# Button 按钮

触发操作或事件的基础组件。

## 引入

```html
<link rel="stylesheet" href="/tokens/tokens.css">
<!-- 复制下面的组件代码 -->
```

## 变体

| 变体 | 用途 |
|------|------|
| `primary` | 主要操作，每页最多一个 |
| `secondary` | 次要操作 |
| `ghost` | 低优先级操作 |
| `danger` | 危险操作（删除、注销） |

## 尺寸

- `sm` — 紧凑场景，表格内操作
- `md` — 默认尺寸
- `lg` — 重点操作，Hero 区域

## 代码

::: details 展开查看完整代码
<<< @/../src/components/button/button.html
:::

## AI 使用说明

```
组件名: button
选择器: .btn
变体: .btn--primary | .btn--secondary | .btn--ghost | .btn--danger
尺寸: .btn--sm | .btn--md | .btn--lg
图标: .btn__icon (1.1em SVG)
```
