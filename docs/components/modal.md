# Modal 对话框

模态对话框组件，用于确认操作、表单弹窗、详情展示。

## 结构

- `.modal-overlay` — 遮罩层（带模糊）
- `.modal` — 对话框主体
- `.modal__header` — 头部（标题 + 关闭按钮）
- `.modal__body` — 内容区（可滚动）
- `.modal__footer` — 底部操作区

## 动画

- 遮罩淡入
- 对话框缩放弹入（spring easing）
- 关闭时反向动画

## 代码

::: details 展开查看完整代码
<<< @/../src/components/modal/modal.html
:::
