# Colors 颜色

## 主色

| 变量 | 值 | 用途 |
|------|-----|------|
| `--color-primary` | `#6366f1` | 主色调（靛蓝紫） |
| `--color-primary-light` | `#818cf8` | 悬浮/高亮 |
| `--color-primary-dark` | `#4f46e5` | 按下/深色 |
| `--color-primary-ghost` | `rgba(99,102,241,0.08)` | 背景装饰 |

## 语义色

| 变量 | 值 |
|------|-----|
| `--color-success` | `#10b981` |
| `--color-warning` | `#f59e0b` |
| `--color-danger` | `#ef4444` |
| `--color-info` | `#3b82f6` |

## 中性色

| 变量 | 亮色模式 | 暗色模式 |
|------|---------|---------|
| `--color-bg` | `#ffffff` | `#0f172a` |
| `--color-text` | `#0f172a` | `#f1f5f9` |
| `--color-border` | `#e2e8f0` | `#334155` |

## 使用方式

```css
.my-element {
  color: var(--color-text);
  background: var(--color-primary);
  border: 1px solid var(--color-border);
}
```

## 暗色模式

```html
<html data-theme="dark">
```
