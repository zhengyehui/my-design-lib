---
layout: doc
title: Dashboard 仪表盘
---

# Dashboard 仪表盘

后台管理页面的经典布局模式，组合 Navbar + Sidebar + Content + Table。

## 结构

```
┌──────────────────────────────────────┐
│            Navbar 导航栏              │ ← navbar.html
├────────┬─────────────────────────────┤
│        │  Page Header (标题+操作)     │
│  侧边栏 │─────────────────────────────│
│        │  Stats Cards (统计卡片)      │ ← card.html × 4
│ Sidebar│─────────────────────────────│
│        │  Data Table (数据表格)       │ ← table.html
│        │─────────────────────────────│
│        │  Pagination (分页)           │
└────────┴─────────────────────────────┘
```

## 组件清单

| 区域 | 组件 | 文件 |
|------|------|------|
| 顶部导航 | Navbar | `src/components/navbar/navbar.html` |
| 侧边栏 | 自定义 (Nav + Links) | `src/components/navbar/navbar.html` (vertical variant) |
| 统计卡片 | Card × 4 | `src/components/card/card.html` |
| 数据表格 | Table | `src/components/table/table.html` |
| 操作按钮 | Button | `src/components/button/button.html` |
| 状态标签 | Badge | `src/components/badge/badge.html` |

## 设计原则

- **侧边栏固定宽度**：240px，收起时 64px
- **内容区自适应**：`flex: 1` 填充剩余空间
- **统计卡片用 4 列 grid**：移动端变 2 列
- **表格支持排序和筛选**：表头可点击
- **面包屑导航**：帮助用户定位当前页面层级

## 代码示例

```html
<div class="dashboard">
  <!-- 顶部导航 -->
  <nav class="navbar navbar--horizontal">...</nav>
  
  <div class="dashboard__body">
    <!-- 侧边栏 -->
    <aside class="sidebar">...</aside>
    
    <!-- 主内容区 -->
    <main class="dashboard__content">
      <div class="stats-grid">
        <div class="card card--flat">用户数: 1,234</div>
        <div class="card card--flat">订单数: 567</div>
        <div class="card card--flat">收入: ¥89,012</div>
        <div class="card card--flat">转化率: 3.2%</div>
      </div>
      <table class="table">...</table>
    </main>
  </div>
</div>
```
