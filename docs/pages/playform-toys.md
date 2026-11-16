---
layout: page
sidebar: false
title: Playform 设计积木玩具商店
pageDetail:
  tags:
  - 电商首页
  - 玩具品牌
  - 北欧极简
  - SVG 插画
  - 交互组件
  rating: 9.1
  iframeSrc: /pages/playform-toys/index.html
  openUrl: /pages/playform-toys/index.html
  tips:
  - title: 布局结构
    content: 单页纵向 9 段式电商首页——吸顶导航 → Hero（大标题 + 浮动玩具剪影）→ 年龄分段选择带 → 3×2 产品网格 → 三条编号理念 → 旗舰单品左右宽幅 → 三栏口碑 → 三档订阅卡 → Newsletter + 深色页脚；全站 1240px 容器 + 40px 留白，1024px 降两列、768px 降单列。
  - title: 配色方案
    content: 纯白 #FFFFFF 主场 + #FAF8F4/#F5F5F5 交替暖灰区；文字 #272727、按钮 #333333（hover #000）、次要 #A9A9A9、描边 #D9D9D9；珊瑚红 #EF6B6B（hover #EE5757）只用于价格/CTA/选中态；蓝 #2F6BE6、黄 #F5C542、绿 #3BA55C 仅作 SVG 玩具微点缀。参考 Vitra Chair Finder 的瑞士产品极简语言。
  - title: 亮点技巧
    content: '• 全部玩具用 inline SVG 手绘（积木塔/陀螺/算盘/拼图/小车/形状分拣器），零图片依赖，浏览器直开完整展示

      • 分段选择器签名控件：#F5F5F5 圆角 10px 轨道 + 24px 圆形手柄，选中态切珊瑚红，年龄/礼盒两个分段均由 vanilla JS 驱动并联动下方内容

      • 滚动入场严格用 html.js 守卫（html.js .reveal:not(.in){opacity:0;translateY(10px)}），IntersectionObserver 加 .in，无 IO 时全量兜底

      • 浮动玩具剪影 8-12s keyframes 缓慢漂浮 + 全场唯一缓动 cubic-bezier(0.19,1,0.22,1) 0.6s；细节处有 ⓘ 信息圆钮、15×3px 三点进度指示、微小大写标签系统'
  - title: 适用场景
    content: 儿童/母婴/木玩品牌电商首页参考、北欧极简商城模板、"设计感消费品"品类落地页、需要 SVG 玩具插画与分段控件等交互组件的设计系统示例。
  prev:
    text: Nova Mobile 运营商套餐
    link: /pages/nova-mobile.html
  next:
    text: Cirrus Airways 精品航司预订
    link: /pages/cirrus-airways.html
---

<PageDetail />
