---
layout: page
title: 页面灵感画廊
description: 完整页面设计展示 — 像 Awwwards 一样浏览和获取灵感
---

<script setup>
import { ref, computed, onMounted, nextTick } from 'vue'

// iframesReady 控制所有 iframe 的 src 赋值时机
// 初始 false → iframe 不加载 → 页面以最终高度完整渲染 → 刷新时浏览器不会滚到底
const iframesReady = ref(false)

onMounted(() => {
  if (typeof window === 'undefined') return

  // 禁用浏览器滚动位置恢复
  if ('scrollRestoration' in window.history) {
    window.history.scrollRestoration = 'manual'
  }
  window.scrollTo(0, 0)

  // 延迟加载 iframe
  nextTick(() => {
    requestAnimationFrame(() => {
      iframesReady.value = true
    })
  })

  // 滚动守卫：iframe 加载过程中的非用户滚动都拦住，1 秒后或用户主动交互后解除
  let guarding = true
  const release = () => { guarding = false }
  const guard = () => {
    if (guarding && window.scrollY > 0) window.scrollTo(0, 0)
  }
  window.addEventListener('scroll', guard, { passive: true })
  // 用户一旦主动滚动/触摸/按方向键，立刻解除守卫
  window.addEventListener('wheel', release, { passive: true, once: true })
  window.addEventListener('touchstart', release, { passive: true, once: true })
  window.addEventListener('keydown', release, { once: true })
  setTimeout(() => {
    guarding = false
    window.removeEventListener('scroll', guard)
  }, 1000)
})

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
  },
  {
    id: 'ai-saas-landing',
    title: 'NexusAI 智能平台',
    category: 'landing',
    tags: ['AI', 'SaaS', '产品展示', '登录框'],
    colors: ['#fafbfc', '#6366f1', '#4f46e5'],
    rating: 9.4,
    description: 'AI SaaS 产品落地页，灵感来自 AuthKit/Amie，包含产品窗口展示、特性网格、客户评价',
  },
  {
    id: 'studio-creative',
    title: 'VOID 创意工作室',
    category: 'portfolio',
    tags: ['暗色', '设计机构', '作品集', 'Marquee'],
    colors: ['#0a0a0a', '#ff4d00', '#141414'],
    rating: 9.5,
    description: '暗色系创意工作室落地页，灵感来自 Locomotive，包含作品网格、服务介绍、无限滚动 Marquee',
  },
  {
    id: 'auth-modern',
    title: 'AuthKit 现代认证页',
    category: 'app',
    tags: ['认证', '登录', '社交登录', '明暗主题'],
    colors: ['#0f0f14', '#6366f1', '#ffffff'],
    rating: 9.4,
    description: '现代认证登录页面，灵感来自 AuthKit/WorkOS，包含登录表单、社交登录、明暗主题切换',
  },
  {
    id: 'product-minimal',
    title: 'FlowDesk 极简产品页',
    category: 'landing',
    tags: ['产品页', '极简', 'SaaS', '产品预览'],
    colors: ['#ffffff', '#0f172a', '#f8fafc'],
    rating: 9.3,
    description: '极简产品落地页，灵感来自 Tatem/Amie，包含产品预览窗口、特性网格、分栏展示',
  },
  {
    id: '3d-interactive-landing',
    title: '3D 互动落地页',
    category: 'landing',
    tags: ['3D', '互动', '沉浸式', '创意工作室'],
    colors: ['#000000', '#6366f1', '#8b5cf6'],
    rating: 9.5,
    description: '受 Lusion.co 启发的 3D 互动落地页，沉浸式数字体验，3D 动画背景 + 作品展示',
  },
  {
    id: 'auth-modern',
    title: '现代认证页面',
    category: 'app',
    tags: ['认证', '登录', '社交登录', '深色模式'],
    colors: ['#fafafa', '#6366f1', '#111827'],
    rating: 9.3,
    description: '受 AuthKit 启发的现代认证页面，登录表单 + 社交登录 + 功能特性展示 + 深色模式切换',
  },
  {
    id: 'tech-blog',
    title: 'DevChronicle 技术博客',
    category: 'blog',
    tags: ['博客', '编辑设计', '文章列表', 'Newsletter'],
    colors: ['#ffffff', '#6366f1', '#f59e0b'],
    rating: 9.4,
    description: '现代技术博客页面，灵感来自 Stripe/Vercel 博客，包含 Featured 文章、卡片网格、侧边栏、Newsletter 订阅',
  },
  {
    id: 'analytics-dashboard',
    title: '数据分析仪表盘',
    category: 'dashboard',
    tags: ['仪表盘', '数据分析', '暗色主题', '图表'],
    colors: ['#0f0f14', '#6366f1', '#10b981'],
    rating: 9.5,
    description: '暗色主题数据分析仪表盘，灵感来自 Mixpanel/Amplitude，包含统计卡片、SVG 图表、数据表格',
  }
]

const categories = [
  { id: 'all', label: '全部', icon: '🎨' },
  { id: 'landing', label: '落地页', icon: '🚀' },
  { id: 'portfolio', label: '作品集', icon: '💼' },
  { id: 'dashboard', label: '仪表盘', icon: '📊' },
  { id: 'ecommerce', label: '电商', icon: '🛒' },
  { id: 'creative', label: '创意', icon: '✨' },
  { id: 'blog', label: '博客', icon: '📝' },
  { id: 'app', label: '应用', icon: '📱' }
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
      <div class="card-preview">
        <iframe
          v-if="iframesReady"
          :src="`/pages/${page.id}/index.html`"
          scrolling="no"
          loading="lazy"
          tabindex="-1"
          sandbox=""
          :title="page.title"
          class="card-iframe"
        ></iframe>
        <div class="card-overlay"></div>
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

/* ⚠️ 以下 VitePress 覆盖样式仅在画廊页生效（通过 :has() 限定） */
body:has(.gallery-page) .VPSidebar,
body:has(.gallery-page) .VPDocOutlineDropdown,
body:has(.gallery-page) .VPDocFooter,
body:has(.gallery-page) .VPDocAside,
body:has(.gallery-page) .aside {
  display: none !important;
}

body:has(.gallery-page) .VPContent {
  padding: 0 !important;
  margin: 0 !important;
  max-width: none !important;
  width: 100% !important;
}

body:has(.gallery-page) .VPDoc {
  padding: 0 !important;
  margin: 0 !important;
  max-width: none !important;
  width: 100% !important;
}

body:has(.gallery-page) .VPDoc .container,
body:has(.gallery-page) .VPDoc .content,
body:has(.gallery-page) .VPDoc .content-container,
body:has(.gallery-page) .VPDoc main {
  max-width: none !important;
  width: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
}

/* 页面容器和空间调整 - 为全局导航栏预留空间 */
.gallery-page {
  margin-top: 0;
  padding-top: 0;
}

/* Hero */
.gallery-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 2rem 2rem;
}
.gallery-hero {
  text-align: center;
  padding: 5rem 0 2rem;
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

/* Preview — 真实 iframe 截图 */
.card-preview {
  position: relative;
  aspect-ratio: 16/10;
  overflow: hidden;
  background: #fafafa;
}
.card-iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 1440px;
  height: 900px;
  border: 0;
  transform: scale(0.28);
  transform-origin: top left;
  pointer-events: none;
  background: #fff;
}
.card-overlay {
  position: absolute;
  inset: 0;
  background: transparent;
  transition: background 0.25s ease;
  z-index: 2;
}
.gallery-card:hover .card-overlay {
  background: rgba(99, 102, 241, 0.05);
}

.card-score {
  position: absolute;
  top: 12px;
  right: 12px;
  font-size: 1.1rem;
  font-weight: 800;
  padding: 4px 10px;
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(6px);
  border-radius: 999px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  z-index: 3;
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
