# 🤝 Contributing to My Design Lib

感谢你对 My Design Lib 的兴趣！这个项目欢迎任何形式的贡献。

## 🎯 贡献方式

### 提交新组件

1. Fork 本仓库
2. 在 `src/components/` 下创建组件目录
3. 组件文件结构：
   ```
   src/components/your-component/
   ├── your-component.html    # 组件 HTML + 内联 CSS
   └── your-component.css     # 独立 CSS 文件（可选）
   ```
4. 更新 `ai-manifest.json`，添加组件信息
5. 在 `docs/components/` 下创建文档页
6. 提交 PR

### 组件规范

- ✅ **零依赖**：只用原生 HTML + CSS，不引入任何框架
- ✅ **响应式**：移动端友好
- ✅ **可主题化**：使用 `tokens.css` 中的 CSS 变量
- ✅ **语义化**：使用正确的 HTML 标签和 ARIA 属性
- ✅ **变体支持**：通过 CSS 类名切换变体（如 `.btn--primary`）
- ✅ **暗色模式**：支持 `data-theme="dark"` 自动切换

### 组件模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Component Name</title>
  <style>
    /* 引入设计变量 */
    @import url('../../tokens/tokens.css');

    /* 组件样式 */
    .component-name {
      /* 使用 tokens 中的变量 */
      color: var(--color-text);
      padding: var(--spacing-md);
      border-radius: var(--radius-md);
    }

    /* 变体 */
    .component-name--variant { }

    /* 尺寸 */
    .component-name--sm { }
    .component-name--lg { }

    /* 暗色模式 */
    [data-theme="dark"] .component-name {
      color: var(--color-text-dark);
    }
  </style>
</head>
<body>
  <!-- 组件 HTML -->
</body>
</html>
```

### ai-manifest.json 格式

```json
{
  "name": "component-name",
  "description": "组件描述",
  "variants": ["default", "variant-1", "variant-2"],
  "sizes": ["sm", "md", "lg"],
  "tags": ["category", "type"],
  "css_path": "/components/component-name/component-name.css",
  "html_path": "/components/component-name/component-name.html",
  "demo_path": "/docs/components/component-name"
}
```

## 🐛 报告 Bug

请在 [Issues](../../issues) 中报告，包含：
- 浏览器和版本
- 复现步骤
- 预期行为 vs 实际行为
- 截图（如有）

## 💡 提出新功能

欢迎在 Issues 中讨论新组件想法！

## 📄 License

贡献即表示你同意你的贡献将采用 MIT License。
