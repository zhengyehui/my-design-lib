---
layout: page
sidebar: false
title: AVIFAUNA — 鸟类野外图鉴
pageDetail:
  tags:
  - 博物图鉴
  - HUD标注
  - 等宽排版
  - CSS网点质感
  rating: 9.2
  iframeSrc: /pages/avifauna-guide/index.html
  openUrl: /pages/avifauna-guide/index.html
  tips:
  - title: 布局结构
    content: 'HUD 风格 Hero（大标题 + 四角图版标注 + 标本统计条）→ 图版网格（6 种真实鸟类 SVG 标本卡，每卡 HUD 四角标注 + 体长/翼展/IUCN 数据 + 观察笔记）→ 翼型解剖图解（SVG 飞羽分区 + 引线标注 + 圆形 mask 注释面板）→ 迁徙路线地图（SVG 虚线动画 + 停歇地标注）→ 鸣叫频谱条（JS 确定性包络 CSS 条形图）→ 分类系统表（tabular 检索表）→ 野外观察季节时间线（12 月物候带）→ 四栏页脚'
  - title: 配色方案
    content: '近黑 #080808 底 + 白 #F7F8F9 主体单色；1px 白线分隔 opacity .5（rgba(247,248,249,.5)），层级仅靠 400/700 字重与 10-12px 全大写等宽标签；点缀色观测橙 #FF6B35 仅用于 IUCN 濒危等级、繁殖季物候带、频谱共振峰与图版红顶高亮，UI 主体保持黑白'
  - title: 亮点技巧
    content: '• 全部鸟形为 inline SVG 几何构造线稿（身体/喙/翼/尾分件绘制），零外部图片，body 覆羽用 <pattern> 网点填充

      • 网点质感三层实现：radial-gradient 网点底纹 + repeating-conic-gradient 棋盘 dither + SVG halftonePat 图案填充，模拟制版网线

      • 四角 HUD 标注组件（左上标本名 / 右上图版号 / 左下科考编号 / 右下比例尺刻度）复用于 Hero、图版卡与地图

      • 注释面板用 @property 注册 --mr 自定义属性驱动 mask-image 圆形揭示动画，配合 html.js 守卫的滚动入场

      • 迁徙路线 stroke-dashoffset「行军蚁」虚线动画，三通道不同周期；鸣叫频谱条由种子伪随机生成确定性包络并逐条延时入场

      • hover 字重 400→700 突变无位移，0.15s cubic-bezier(.4,0,.2,1) 全站统一过渡，border-radius 全站 0'
  - title: 适用场景
    content: '博物/自然类内容页、野外图鉴与物种档案、科学考察记录库、博物馆展签数字化、HUD 仪表风编辑排版、暗色单色文档系统'
---

<PageDetail />
