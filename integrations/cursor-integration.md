# My Design Lib — Cursor 集成指南

## 方法 1：MCP Server（推荐）

1. 打开 Cursor Settings → Features → MCP
2. 添加新的 MCP Server:
   - Name: `my-design-lib`
   - Command: `python3`
   - Args: `["/path/to/design-lib/scripts/mcp_server.py"]`

3. 在 Cursor 中使用:
   ```
   @my-design-lib 帮我用 button 组件做一个登录按钮
   ```

## 方法 2：@code 指向组件文件

在 Cursor 的 `.cursorrules` 中添加:

```
当需要 UI 组件时，优先从以下路径读取:
~/desktop/project/design-lib/src/components/

可用组件:
- button/ (primary, secondary, ghost, danger)
- card/ (default, flat, glass, gradient)
- hero/ (标准落地页首屏)
- input/ (表单输入)
- badge/ (标签徽章)
- modal/ (对话框)

设计变量: ~/desktop/project/design-lib/src/tokens/tokens.css
```

## 方法 3：直接引用 CDN

在项目中引入:
```html
<link rel="stylesheet" href="http://101.37.166.208:11930/tokens/tokens.css">
<script src="http://101.37.166.208:11930/ai-manifest.json"></script>
```
