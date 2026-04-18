---
layout: false
title: 页面灵感画廊
description: 完整页面设计展示 — 像 Awwwards 一样浏览和获取灵感
---

<script setup>
import { ref, computed } from 'vue'

const pages = [
  {
    id: 'saas-landing',
    title: 'NovaPay SaaS 落地页',
    category: 'landing',
    tags: ['SaaS', '支付', '渐变'],
    colors: ['#6366f1', '#7c3aed', '#eef2ff'],
    rating: 9.2,
    description: '现代 SaaS 产品落地页，渐变 Hero + 特性卡片 + CTA 区域',
  },
  {
    id: 'portfolio',
    title: '创意作品集',
    category: 'portfolio',
    tags: ['暗色', '作品集', '动效'],
    colors: ['#0a0a0a', '#6366f1', '#ec4899'],
    rating: 9.5,
    description: '暗色系个人作品集，渐变背景 + 作品网格 + 技能展示',
  },
  {
    id: 'dashboard-dark',
    title: 'Nexus 数据仪表盘',
    category: 'dashboard',
    tags: ['暗色', '数据', '管理后台'],
    colors: ['#0f0f14', '#6366f1', '#1a1a24'],
    rating: 9.0,
    description: '暗色模式数据分析仪表盘，侧边栏 + 统计卡片 + 图表 + 表格',
  },
  {
    id: 'checkout',
    title: 'ShopFlow 结账页',
    category: 'ecommerce',
    tags: ['电商', '表单', '支付'],
    colors: ['#f8f9fb', '#6366f1', '#fff'],
    rating: 8.8,
    description: '电商结账流程，步骤指示器 + 表单 + 订单摘要侧栏',
  },
  {
    id: '404-creative',
    title: '太空主题 404',
    category: 'creative',
    tags: ['404', '动效', '创意'],
    colors: ['#0a0a0a', '#6366f1', '#a855f7'],
    rating: 9.3,
    description: '太空主题创意 404 页面，星空动画 + 渐变数字 + 漂浮元素',
  },
  {
    id: 'agency-portfolio',
    title: 'Studio Creative 设计机构',
    category: 'portfolio',
    tags: ['设计机构', '作品集', '品牌设计'],
    colors: ['#1a1a1a', '#f8f7f4', '#e63946'],
    rating: 9.4,
    description: '现代设计机构作品集，灵感来自 Locomotive，包含作品展示、服务介绍、客户评价',
  },
  {
    id: 'conference-landing',
    title: 'TechConf 科技大会',
    category: 'landing',
    tags: ['科技大会', '会议网站', '活动页面'],
    colors: ['#0a2540', '#635bff', '#00d4ff'],
    rating: 9.6,
    description: '专业科技大会落地页，灵感来自 Stripe Sessions，包含议程、演讲者、门票定价',
  }
]

const categories = [
  { id: 'all', label: '全部', icon: '🎨' },
  { id: 'landing', label: '落地页', icon: '🚀' },
  { id: 'portfolio', label: '作品集', icon: '💼' },
  { id: 'dashboard', label: '仪表盘', icon: '📊' },
  { id: 'ecommerce', label: '电商', icon: '🛒' },
  { id: 'creative', label: '创意', icon: '✨' }
]

const activeCategory = ref('all')
const filteredPages = computed(() => {
  if (activeCategory.value === 'all') return pages
  return pages.filter(p => p.category === activeCategory.value)
})

function getScoreColor(score) {
  if (score >= 9.5) return '#22c55e'
  if (score >= 9.0) return '#6366f1'
  if (score >= 8.5) return '#f59e0b'
  return '#888'
}
</script>

<div class="gallery-page">
  <!-- Nav -->
  <nav class="gallery-nav">
    <div class="nav-left">
      <a href="/" class="nav-logo">◆ My Design Lib</a>
    </div>
    <div class="nav-links">
      <a href="/">首页</a>
      <a href="/components/button.html">组件</a>
      <a href="/tokens/colors.html">设计变量</a>
      <a href="/pages/" class="active">🎨 页面画廊</a>
      <a href="/sponsor.html">赞助</a>
    </div>
  </nav>

  <!-- SEO Meta -->
  <meta name="description" content="My Design Lib 页面灵感画廊 — 5 个完整页面设计展示，包含 SaaS 落地页、作品集、仪表盘、电商结账、404 创意页。可预览、看源码、学设计。">
  <meta name="keywords" content="页面模板, 前端设计, SaaS模板, 作品集模板, 仪表盘模板, 电商模板, 404页面, 设计灵感">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="website">
  <meta property="og:title" content="🎨 页面灵感画廊 — My Design Lib">
  <meta property="og:description" content="完整页面设计展示，像 Awwwards 一样浏览。SaaS 落地页、作品集、仪表盘等 5 个高质量页面模板。">
  <meta property="og:url" content="http://101.37.166.208:11930/pages/">
  <link rel="canonical" href="http://101.37.166.208:11930/pages/">


  <!-- Hero -->
  <div class="gallery-hero">
    <h1>🎨 页面灵感画廊</h1>
    <p>完整的页面设计展示，点击即可预览实时效果，查看源码</p>
    <div class="hero-stats">
      <span>📦 {{ pages.length }} 个完整页面</span>
      <span>🏷️ {{ categories.length - 1 }} 个分类</span>
      <span>🔄 每日自动更新</span>
    </div>
  </div>

  <!-- Filter -->
  <div class="gallery-filter">
    <button
      v-for="cat in categories"
      :key="cat.id"
      :class="['filter-btn', { active: activeCategory === cat.id }]"
      @click="activeCategory = cat.id"
    >
      {{ cat.icon }} {{ cat.label }}
    </button>
  </div>

  <!-- Grid -->
  <div class="gallery-grid">
    <a
      v-for="page in filteredPages"
      :key="page.id"
      :href="`/pages/${page.id}.html`"
      class="gallery-card"
    >
      <div class="card-preview" :style="{ background: page.colors[0] }">
        <div class="card-gradient" :style="{
          background: `linear-gradient(135deg, ${page.colors[1]}33, ${page.colors[2]}33)`
        }"></div>
        <div class="card-mockup">
          <div class="mockup-bar">
            <span class="dot" style="background:#ff5f57"></span>
            <span class="dot" style="background:#febc2e"></span>
            <span class="dot" style="background:#28c840"></span>
          </div>
          <div class="mockup-content" :style="{ background: page.colors[0] }">
            <div class="mockup-line" :style="{ background: page.colors[1] + '44', width: '70%' }"></div>
            <div class="mockup-line short" :style="{ background: page.colors[2] + '33' }"></div>
            <div class="mockup-blocks">
              <div class="mockup-block" :style="{ background: page.colors[1] + '22' }"></div>
              <div class="mockup-block" :style="{ background: page.colors[2] + '22' }"></div>
              <div class="mockup-block" :style="{ background: page.colors[1] + '22' }"></div>
            </div>
          </div>
        </div>
        <div class="card-score" :style="{ color: getScoreColor(page.rating) }">
          {{ page.rating }}
        </div>
      </div>
      <div class="card-info">
        <h3>{{ page.title }}</h3>
        <p>{{ page.description }}</p>
        <div class="card-tags">
          <span v-for="tag in page.tags" :key="tag" class="tag">{{ tag }}</span>
        </div>
      </div>
    </a>
  </div>

  <!-- Footer -->
  <div class="gallery-footer">
    <p>© 2026 My Design Lib — 为 AI 编程助手优化的设计库</p>
    <p>📧 weta_zheng@qq.com &nbsp;|&nbsp; 💬 微信 weta010730</p>
  </div>
</div>

<style>
* { margin: 0; padding: 0; box-sizing: border-box; }

/* Nav */
.gallery-nav {
  position: sticky;
  top: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.8rem 2rem;
  background: rgba(255,255,255,0.9);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid #e5e7eb;
}
[data-theme="dark"] .gallery-nav {
  background: rgba(15,15,20,0.9);
  border-color: #1e1e2a;
}
.nav-logo {
  font-size: 1.1rem;
  font-weight: 800;
  color: #6366f1;
  text-decoration: none;
}
.nav-links {
  display: flex;
  gap: 1.5rem;
  align-items: center;
}
.nav-links a {
  text-decoration: none;
  color: #666;
  font-size: 0.9rem;
  font-weight: 500;
  transition: color 0.2s;
}
.nav-links a:hover, .nav-links a.active {
  color: #6366f1;
}

/* Hero */
.gallery-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem 2rem;
}
.gallery-hero {
  text-align: center;
  padding: 3rem 0 1.5rem;
}
.gallery-hero h1 {
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 0.5rem;
}
.gallery-hero p {
  color: #666;
  font-size: 1.1rem;
}
.hero-stats {
  display: flex;
  gap: 2rem;
  justify-content: center;
  margin-top: 1rem;
  font-size: 0.9rem;
  color: #888;
}

/* Filter */
.gallery-filter {
  display: flex;
  gap: 0.5rem;
  justify-content: center;
  flex-wrap: wrap;
  margin: 1.5rem 0;
}
.filter-btn {
  padding: 0.5rem 1.2rem;
  border: 1px solid #e5e7eb;
  border-radius: 100px;
  background: none;
  cursor: pointer;
  font-size: 0.9rem;
  color: #666;
  transition: all 0.2s;
}
.filter-btn:hover { border-color: #6366f1; color: #6366f1; }
.filter-btn.active { background: #6366f1; border-color: #6366f1; color: #fff; }

/* Grid */
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}
.gallery-card {
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid #e5e7eb;
  text-decoration: none;
  color: inherit;
  transition: all 0.3s;
  display: block;
}
.gallery-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 20px 60px rgba(0,0,0,0.1);
  border-color: #6366f1;
}

/* Preview */
.card-preview {
  position: relative;
  aspect-ratio: 16/10;
  overflow: hidden;
}
.card-gradient { position: absolute; inset: 0; }
.card-mockup {
  position: absolute;
  inset: 15%;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.mockup-bar {
  height: 20px;
  background: rgba(0,0,0,0.3);
  display: flex;
  align-items: center;
  gap: 5px;
  padding: 0 8px;
}
.dot { width: 6px; height: 6px; border-radius: 50%; }
.mockup-content { padding: 12px; height: calc(100% - 20px); }
.mockup-line { height: 6px; border-radius: 3px; margin-bottom: 8px; }
.mockup-line.short { width: 40%; height: 4px; }
.mockup-blocks { display: flex; gap: 6px; margin-top: 12px; }
.mockup-block { flex: 1; height: 30px; border-radius: 4px; }

.card-score {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 1.4rem;
  font-weight: 900;
  text-shadow: 0 2px 8px rgba(0,0,0,0.5);
}

/* Info */
.card-info { padding: 1.2rem; background: #fff; }
.card-info h3 { font-size: 1.1rem; font-weight: 700; margin-bottom: 0.3rem; }
.card-info p { font-size: 0.85rem; color: #666; line-height: 1.5; margin-bottom: 0.8rem; }
.card-tags { display: flex; gap: 0.4rem; flex-wrap: wrap; }
.tag {
  padding: 0.2rem 0.6rem;
  background: #f3f4f6;
  border-radius: 6px;
  font-size: 0.75rem;
  color: #666;
}

/* Footer */
.gallery-footer {
  text-align: center;
  padding: 3rem 0 1rem;
  margin-top: 3rem;
  border-top: 1px solid #e5e7eb;
  color: #999;
  font-size: 0.85rem;
  line-height: 1.8;
}

.gallery-empty { text-align: center; padding: 4rem; color: #999; font-size: 1.1rem; }

@media (max-width: 640px) {
  .gallery-grid { grid-template-columns: 1fr; }
  .gallery-hero h1 { font-size: 1.8rem; }
  .nav-links { gap: 0.8rem; font-size: 0.8rem; }
  .hero-stats { flex-direction: column; gap: 0.5rem; }
}
</style>
