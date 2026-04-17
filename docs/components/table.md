# Table 表格



## 实时预览

<iframe src="/components/table/preview.html" style="width:100%; border:1px solid var(--color-border, #e5e7eb); border-radius:8px; min-height:200px; background:white;" loading="lazy"></iframe>

## 引入

```html
<link rel="stylesheet" href="/tokens/tokens.css">
<link rel="stylesheet" href="/components/table/table.css">
```

## 代码

### HTML

```html
<!-- Table Component — 数据表格组件，3种变体: default/striped/bordered -->


<!-- Demo: Table 组件 -->
<div style="background: var(--color-bg-subtle); padding: 20px; border-radius: var(--radius-lg);">
  <!-- 默认表格 -->
  <div style="margin-bottom: 40px;">
    <h3 style="margin-bottom: 16px; color: var(--color-text); font-size: var(--text-lg);">默认表格</h3>
    <table class="table">
      <thead>
        <tr>
          <th>用户</th>
          <th>状态</th>
          <th>角色</th>
          <th>最后登录</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <div class="table__user">
              <div class="table__avatar">张</div>
              <div class="table__user-info">
                <span class="table__user-name">张三</span>
                <span class="table__user-email">zhangsan@example.com</span>
              </div>
            </div>
          </td>
          <td><span class="table__badge table__badge--success">活跃</span></td>
          <td class="table__text--secondary">管理员</td>
          <td class="table__text--muted">2024-01-15 14:30</td>
          <td>
            <div class="table__actions">
              <button class="table__action-btn">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7"></path>
                  <path d="M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                </svg>
              </button>
              <button class="table__action-btn table__action-btn--danger">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M3 6h18"></path>
                  <path d="M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"></path>
                  <line x1="10" y1="11" x2="10" y2="17"></line>
                  <line x1="14" y1="11" x2="14" y2="17"></line>
                </svg>
              </button>
            </div>
          </td>
        </tr>
        <tr>
          <td>
            <div class="table__user">
              <div class="table__avatar">李</div>
              <div class="table__user-info">
                <span class="table__user-name">李四</span>
                <span class="table__user-email">lisi@example.com</span>
              </div>
            </div>
          </td>
          <td><span class="table__badge table__badge--warning">待审核</span></td>
          <td class="table__text--secondary">编辑</td>
          <td class="table__text--muted">2024-01-14 09:15</td>
          <td>
            <div class="table__actions">
              <button class="table__action-btn">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7"></path>
                  <path d="M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                </svg>
              </button>
              <button class="table__action-btn table__action-btn--danger">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M3 6h18"></path>
                  <path d="M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"></path>
                  <line x1="10" y1="11" x2="10" y2="17"></line>
                  <line x1="14" y1="11" x2="14" y2="17"></line>
                </svg>
              </button>
            </div>
          </td>
        </tr>
        <tr>
          <td>
            <div class="table__user">
              <div class="table__avatar">王</div>
              <div class="table__user-info">
                <span class="table__user-name">王五</span>
                <span class="table__user-email">wangwu@example.com</span>
              </div>
            </div>
          </td>
          <td><span class="table__badge table__badge--danger">禁用</span></td>
          <td class="table__text--secondary">访客</td>
          <td class="table__text--muted">2024-01-10 16:45</td>
          <td>
            <div class="table__actions">
              <button class="table__action-btn">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7"></path>
                  <path d="M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                </svg>
              </button>
              <button class="table__action-btn table__action-btn--danger">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M3 6h18"></path>
                  <path d="M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"></path>
                  <line x1="10" y1="11" x2="10" y2="17"></line>
                  <line x1="14" y1="11" x2="14" y2="17"></line>
                </svg>
              </button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  
  <!-- 斑马纹表格 -->
  <div style="margin-bottom: 40px;">
    <h3 style="margin-bottom: 16px; color: var(--color-text); font-size: var(--text-lg);">斑马纹表格</h3>
    <table class="table table--striped">
      <thead>
        <tr>
          <th>产品</th>
          <th>分类</th>
          <th>价格</th>
          <th>库存</th>
          <th>状态</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="table__text--secondary">MacBook Pro 14"</td>
          <td>笔记本电脑</td>
          <td>¥16,999</td>
          <td>45</td>
          <td><span class="table__badge table__badge--success">在售</span></td>
        </tr>
        <tr>
          <td class="table__text--secondary">iPhone 15 Pro</td>
          <td>智能手机</td>
          <td>¥8,999</td>
          <td>120</td>
          <td><span class="table__badge table__badge--success">在售</span></td>
        </tr>
        <tr>
          <td class="table__text--secondary">AirPods Pro</td>
          <td>耳机</td>
          <td>¥1,899</td>
          <td>0</td>
          <td><span class="table__badge table__badge--warning">缺货</span></td>
        </tr>
        <tr>
          <td class="table__text--secondary">iPad Air</td>
          <td>平板电脑</td>
          <td>¥4,799</td>
          <td>28</td>
          <td><span class="table__badge table__badge--success">在售</span></td>
        </tr>
        <tr>
          <td class="table__text--secondary">Apple Watch</td>
          <td>智能手表</td>
          <td>¥3,199</td>
          <td>67</td>
          <td><span class="table__badge table__badge--info">预售</span></td>
        </tr>
      </tbody>
    </table>
  </div>
  
  <!-- 边框表格 -->
  <div>
    <h3 style="margin-bottom: 16px; color: var(--color-text); font-size: var(--text-lg);">边框表格</h3>
    <table class="table table--bordered">
      <thead>
        <tr>
          <th>日期</th>
          <th>订单号</th>
          <th>客户</th>
          <th>金额</th>
          <th>支付方式</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="table__text--muted">2024-01-15</td>
          <td class="table__text--secondary">#ORD-001</td>
          <td>张三</td>
          <td>¥2,450</td>
          <td>微信支付</td>
        </tr>
        <tr>
          <td class="table__text--muted">2024-01-14</td>
          <td class="table__text--secondary">#ORD-002</td>
          <td>李四</td>
          <td>¥1,280</td>
          <td>支付宝</td>
        </tr>
        <tr>
          <td class="table__text--muted">2024-01-13</td>
          <td class="table__text--secondary">#ORD-003</td>
          <td>王五</td>
          <td>¥3,650</td>
          <td>信用卡</td>
        </tr>
        <tr>
          <td class="table__text--muted">2024-01-12</td>
          <td class="table__text--secondary">#ORD-004</td>
          <td>赵六</td>
          <td>¥890</td>
          <td>微信支付</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
```

### CSS

```css
/* Table.css */
.table {
  width: 100%;
  border-collapse: collapse;
  font-family: var(--font-sans);
  font-size: var(--text-sm);
  color: var(--color-text);
  background: var(--color-surface);
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
}

/* ── 表头 ──────────────────────────── */
.table thead {
  background: var(--color-bg-muted);
}

.table th {
  padding: var(--space-3) var(--space-4);
  text-align: left;
  font-weight: var(--weight-semibold);
  color: var(--color-text-secondary);
  border-bottom: 2px solid var(--color-border);
  white-space: nowrap;
}

.table th:first-child {
  padding-left: var(--space-6);
}

.table th:last-child {
  padding-right: var(--space-6);
}

/* ── 表格体 ────────────────────────── */
.table tbody {
  border-bottom: 1px solid var(--color-border);
}

.table td {
  padding: var(--space-3) var(--space-4);
  border-bottom: 1px solid var(--color-border);
  vertical-align: middle;
}

.table td:first-child {
  padding-left: var(--space-6);
}

.table td:last-child {
  padding-right: var(--space-6);
}

.table tbody tr:last-child td {
  border-bottom: none;
}

.table tbody tr:hover {
  background: var(--color-bg-subtle);
}

/* ── 变体 ──────────────────────────── */
.table--striped tbody tr:nth-child(even) {
  background: var(--color-bg-subtle);
}

.table--striped tbody tr:nth-child(even):hover {
  background: var(--color-bg-muted);
}

.table--bordered {
  border: 1px solid var(--color-border);
  box-shadow: none;
}

.table--bordered th,
.table--bordered td {
  border: 1px solid var(--color-border);
}

.table--bordered thead th {
  border-bottom: 2px solid var(--color-border);
}

/* ── 表格单元格内容 ────────────────── */
.table__text {
  color: var(--color-text);
}

.table__text--secondary {
  color: var(--color-text-secondary);
}

.table__text--muted {
  color: var(--color-text-muted);
}

/* ── 状态标签 ──────────────────────── */
.table__badge {
  display: inline-flex;
  align-items: center;
  padding: 2px 8px;
  border-radius: var(--radius-full);
  font-size: var(--text-xs);
  font-weight: var(--weight-medium);
}

.table__badge--success {
  background: rgba(16, 185, 129, 0.1);
  color: var(--color-success);
}

.table__badge--warning {
  background: rgba(245, 158, 11, 0.1);
  color: var(--color-warning);
}

.table__badge--danger {
  background: rgba(239, 68, 68, 0.1);
  color: var(--color-danger);
}

.table__badge--info {
  background: rgba(59, 130, 246, 0.1);
  color: var(--color-info);
}

/* ── 头像和用户信息 ────────────────── */
.table__user {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.table__avatar {
  width: 32px;
  height: 32px;
  border-radius: var(--radius-full);
  background: var(--color-primary-ghost);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-primary);
  font-weight: var(--weight-semibold);
  font-size: var(--text-sm);
}

.table__user-info {
  display: flex;
  flex-direction: column;
}

.table__user-name {
  font-weight: var(--weight-medium);
  color: var(--color-text);
}

.table__user-email {
  font-size: var(--text-xs);
  color: var(--color-text-muted);
}

/* ── 操作按钮 ──────────────────────── */
.table__actions {
  display: flex;
  gap: var(--space-2);
}

.table__action-btn {
  width: 32px;
  height: 32px;
  border-radius: var(--radius-md);
  border: none;
  background: transparent;
  color: var(--color-text-secondary);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all var(--duration-fast) var(--ease-default);
}

.table__action-btn:hover {
  background: var(--color-bg-muted);
  color: var(--color-text);
}

.table__action-btn--danger:hover {
  background: rgba(239, 68, 68, 0.1);
  color: var(--color-danger);
}

/* ── 响应式设计 ────────────────────── */
@media (max-width: 768px) {
  .table {
    display: block;
    overflow-x: auto;
    white-space: nowrap;
  }
  
  .table th,
  .table td {
    padding: var(--space-2) var(--space-3);
  }
}
```

## AI 使用说明

```
组件名: table
选择器: .table
依赖: /tokens/tokens.css
文件: /components/table/table.html
```
