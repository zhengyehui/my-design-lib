---
layout: page
title: 页面灵感画廊
description: 80 个完整页面设计展示 — 像 Awwwards 一样浏览和获取灵感
sidebar: false
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
    category: 'app',
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
    id: 'tech-blog',
    title: 'DevChronicle 技术博客',
    category: 'content',
    tags: ['博客', '编辑设计', '文章列表', 'Newsletter'],
    colors: ['#ffffff', '#6366f1', '#f59e0b'],
    rating: 9.4,
    description: '现代技术博客页面，灵感来自 Stripe/Vercel 博客，包含 Featured 文章、卡片网格、侧边栏、Newsletter 订阅',
  },
  {
    id: 'analytics-dashboard',
    title: '数据分析仪表盘',
    category: 'app',
    tags: ['仪表盘', '数据分析', '暗色主题', '图表'],
    colors: ['#0f0f14', '#6366f1', '#10b981'],
    rating: 9.5,
    description: '暗色主题数据分析仪表盘，灵感来自 Mixpanel/Amplitude，包含统计卡片、SVG 图表、数据表格',
  },
  {
    id: 'product-showcase',
    title: 'Bloom 生活方式电商',
    category: 'ecommerce',
    tags: ['电商', '产品展示', '生活方式', '暖色'],
    colors: ['#2d6a4f', '#52b788', '#fefae0'],
    rating: 9.3,
    description: '现代生活方式品牌电商页，灵感来自 Happly，包含产品网格、特色产品展示、用户评价、Newsletter',
  },
  {
    id: 'coming-soon',
    title: 'Pulse 品牌上线预告',
    category: 'creative',
    tags: ['Coming Soon', '倒计时', '创意', '暗色'],
    colors: ['#0a0a0a', '#6366f1', '#ec4899'],
    rating: 9.4,
    description: '创意品牌上线预告页，动画渐变背景 + 倒计时器 + 浮动粒子 + 渐变文字效果',
  },
  {
    id: 'restaurant-ember',
    title: 'Ember Kitchen 餐厅落地页',
    category: 'landing',
    tags: ['餐厅', '暖色', '美食', '预约'],
    colors: ['#d97706', '#1a1a1a', '#faf8f5'],
    rating: 9.5,
    description: '高端餐厅落地页，灵感来自 Haven Coffee，暗色 Hero + 粒子动效 + 菜单展示 + 预约 CTA',
  },
  {
    id: 'pricing-page',
    title: 'CloudStack 定价页',
    category: 'landing',
    tags: ['定价', 'SaaS', '对比表', 'FAQ'],
    colors: ['#6366f1', '#7c3aed', '#eef2ff'],
    rating: 9.3,
    description: '现代 SaaS 定价页，灵感来自 Amie/Stripe，包含月付年付切换、三栏定价卡片、功能对比表、FAQ 手风琴',
  },
  {
    id: 'music-player',
    title: 'WaveSync 音乐播放器',
    category: 'creative',
    tags: ['音乐', '播放器', '暗色', '媒体'],
    colors: ['#0a0a0f', '#8b5cf6', '#ec4899'],
    rating: 9.5,
    description: '暗色系音乐流媒体播放器，三栏布局 + 环境光背景 + 播放队列 + 底部控制条',
  },
  {
    id: 'fitness-app',
    title: 'VitalFit 健身追踪',
    category: 'app',
    tags: ['健身', '健康', '运动', '数据'],
    colors: ['#f0f4f8', '#10b981', '#f97316'],
    rating: 9.4,
    description: '健身追踪应用仪表盘，SVG 环形图 + 运动数据统计 + 心率监测 + 打卡日历',
  },
  {
    id: 'case-study',
    title: 'Arclight 品牌重塑案例',
    category: 'portfolio',
    tags: ['案例研究', '品牌重塑', 'B2B SaaS', '暗色'],
    colors: ['#07070d', '#6366f1', '#ec4899'],
    rating: 9.6,
    description: 'B2B SaaS 品牌重塑案例研究，灵感来自 Evervault + Traffic Productions，包含项目概览、流程时间线、成果数据、作品展示',
  },
  {
    id: 'docs-portal',
    title: 'DevDocs 现代文档门户',
    category: 'content',
    tags: ['文档', '门户', '开发者体验', '代码高亮'],
    colors: ['#ffffff', '#6366f1', '#1e1e2e'],
    rating: 9.5,
    description: '现代技术文档门户，灵感来自 Stripe/Railway 文档，包含三栏布局、代码高亮、API 参数表、步骤引导、Callout 提示',
  },
  {
    id: 'job-board',
    title: 'TalentFlow 招聘平台',
    category: 'industry',
    tags: ['招聘', '求职', 'SaaS平台', '深色Hero'],
    colors: ['#0f172a', '#6366f1', '#10b981'],
    rating: 9.4,
    description: '现代招聘平台页面，灵感来自 levels.fyi/Notion Careers，包含搜索筛选、职位卡片、侧边栏热招公司、趋势排行',
  },
  {
    id: 'real-estate-luxury',
    title: 'Luxe Estates 奢华房产',
    category: 'industry',
    tags: ['房产', '奢华', '暗色主题', '大图展示'],
    colors: ['#0d0d0d', '#c9a96e', '#161616'],
    rating: 9.5,
    description: '奢华房产落地页，Playfair Display 衬线字体 + 金色强调 + 全屏 Hero + 房源网格 + 搜索筛选 + 经纪人团队',
  },
  {
    id: 'magazine-editorial',
    title: 'Mono Journal 杂志编辑',
    category: 'content',
    tags: ['杂志', '编辑设计', '报纸', '内容排版'],
    colors: ['#f8f6f1', '#c0392b', '#1a1a1a'],
    rating: 9.4,
    description: '现代杂志编辑页面，DM Serif Display 衬线字体 + 双线边框报刊风 + 特色文章网格 + 观点金句 + Newsletter 订阅',
  },
  {
    id: 'product-detail-premium',
    title: 'Lumina Pro 产品详情页',
    category: 'ecommerce',
    tags: ['产品详情', 'PDP', '暗色', '硬件'],
    colors: ['#0a0a0f', '#6366f1', '#8b5cf6'],
    rating: 9.4,
    description: '暗色系硬件产品详情页，灵感来自 Opal Camera，全屏 Hero + 特性网格 + 交替展示 + 对比表格 + 粘性购买栏',
  },
  {
    id: 'weather-dashboard',
    title: 'SkyPulse 天气仪表盘',
    category: 'app',
    tags: ['天气', '仪表盘', '暗色', '动效', '毛玻璃'],
    colors: ['#1a1a3e', '#0d1b2a', '#f59e0b'],
    rating: 9.5,
    description: '深蓝渐变天气仪表盘，毛玻璃卡片 + 动态 SVG 图标 + 浮动光球动画 + 日出日落弧线 + 空气质量指数',
  },
  {
    id: 'saas-changelog',
    title: 'FlowSync 更新日志',
    category: 'content',
    tags: ['更新日志', 'SaaS', '时间线', '标签筛选'],
    colors: ['#ffffff', '#6366f1', '#e2e8f0'],
    rating: 9.3,
    description: 'SaaS 产品更新日志，左侧时间线 + 标签筛选 + 搜索过滤 + 版本卡片展开折叠 + 彩色变更徽章',
  },
  {
    id: 'edu-platform',
    title: 'LearnHub 在线学习平台',
    category: 'industry',
    tags: ['在线教育', '课程', '学习路径', '讲师'],
    colors: ['#0d9488', '#6366f1', '#f0fdfa'],
    rating: 9.4,
    description: '现代在线学习平台，搜索栏 + 课程网格 + 学习路径 + 讲师展示 + 进度追踪',
  },
  {
    id: 'travel-booking',
    title: 'Voyager 旅行预订',
    category: 'industry',
    tags: ['旅行', '预订', '奢华', '目的地'],
    colors: ['#0c1445', '#e8614d', '#c9a96e'],
    rating: 9.5,
    description: '沉浸式旅行预订平台，星空动画 Hero + 毛玻璃搜索框 + 目的地网格 + 套餐定价',
  },
  {
    id: 'crypto-web3',
    title: 'NovaChain Web3 DeFi 落地页',
    category: 'industry',
    tags: ['Web3', 'DeFi', '暗色主题', '加密货币'],
    colors: ['#050510', '#06b6d4', '#8b5cf6'],
    rating: 9.5,
    description: 'Web3 DeFi 产品落地页，暗色太空底 + 霓虹光球动画 + Token 数据展示 + 路线图 + Marquee 合作伙伴',
  },
  {
    id: 'newsletter-landing',
    title: 'The Signal Newsletter 落地页',
    category: 'content',
    tags: ['Newsletter', '内容创作', '极简', '订阅'],
    colors: ['#fafaf9', '#6366f1', '#ec4899'],
    rating: 9.4,
    description: '现代 Newsletter 订阅落地页，渐变文字标题 + 邮箱表单 + 往期精选 + 读者评价 + 暗色 CTA',
  },
  {
    id: 'fashion-brand',
    title: 'Maison Élégance 时尚品牌',
    category: 'industry',
    tags: ['时尚', '奢侈品', '品牌', '衬线字体'],
    colors: ['#faf8f5', '#1a1a1a', '#b8956a'],
    rating: 9.4,
    description: '奢华时尚品牌官网，Playfair Display 衬线字体 + 暖色奶油底 + 产品横向滚动 + 匠心工艺分栏',
  },
  {
    id: 'podcast-show',
    title: 'SoundWave 播客频道',
    category: 'creative',
    tags: ['播客', '音频', '媒体', '暗色主题', '波形动画'],
    colors: ['#0a0a0f', '#ff6b35', '#8b5cf6'],
    rating: 9.4,
    description: '暗色系播客频道页，毛玻璃导航 + CSS 波形动画 + 集数网格 + 主持人介绍 + 听众评价 + Newsletter',
  },
  {
    id: 'fintech-app',
    title: 'NeoBank 数字银行',
    category: 'app',
    tags: ['金融科技', '银行', '数字支付', '明色主题'],
    colors: ['#ffffff', '#00c9a7', '#6366f1'],
    rating: 9.5,
    description: '现代数字银行产品页，CSS 手机模型 + 虚拟银行卡扇形展开 + 交易记录 + 安全特性 + 定价方案',
  },
  {
    id: 'health-ai',
    title: 'Lóvi Care AI 健康管理',
    category: 'industry',
    tags: ['健康', 'AI', '医疗', '护肤'],
    colors: ['#151581', '#5163FF', '#F6F6FA'],
    rating: 9.5,
    description: 'AI 皮肤管理应用落地页，灵感来自 Lóvi.care，手机模型扫描动画 + AI 对话演示 + 成分检测 + 用户评价',
  },
  {
    id: 'photography-portfolio',
    title: 'Atelier Lumière 摄影作品集',
    category: 'portfolio',
    tags: ['摄影', '作品集', '极简', '衬线字体'],
    colors: ['#faf9f7', '#1a1a1a', '#c4a35a'],
    rating: 9.4,
    description: '极简摄影作品集，Playfair Display 衬线字体 + 12 列不等宽网格 + mix-blend-mode 导航 + Marquee 滚动条',
  },
  {
    id: 'architecture-studio',
    title: 'Atelier Noir 建筑设计工作室',
    category: 'portfolio',
    tags: ['建筑设计', '暗色主题', '作品集', '奢华'],
    colors: ['#0a0a0a', '#c9a96e', '#f5f0eb'],
    rating: 9.5,
    description: '暗色系建筑设计工作室，衬线字体 + 宽字距 + 横向滚动画廊 + 交错项目展示',
  },
  {
    id: 'nonprofit-impact',
    title: 'Hope Forward 公益教育平台',
    category: 'industry',
    tags: ['公益', '非营利', '教育', '暗色Hero'],
    colors: ['#0c1d3a', '#e8614d', '#faf8f5'],
    rating: 9.4,
    description: '公益教育组织落地页，浮动粒子动画 + 影响力数据 + 项目网格 + 捐赠 CTA',
  },
  {
    id: 'game-studio',
    title: 'NexusForge 游戏工作室',
    category: 'creative',
    tags: ['游戏', '工作室', '暗色主题', '粒子动画', '招聘'],
    colors: ['#0a0a0f', '#ff4d00', '#ff8a00'],
    rating: 9.5,
    description: '暗色系游戏工作室落地页，Canvas 粒子连线 + 游戏展示网格 + 团队卡片 + 招聘列表 + Marquee 滚动',
  },
  {
    id: 'cloud-storage-app',
    title: 'NimbusDrive 云存储应用',
    category: 'app',
    tags: ['云存储', '文件管理', '协作', '明色主题'],
    colors: ['#f5f5f5', '#0077ff', '#ffffff'],
    rating: 9.3,
    description: '明色系云存储 SaaS 落地页，灵感来自 Shuttle.zip，CSS 文件管理器 UI + 协作光标 + 命令面板 + 存储提供商选择器',
  },
  {
    id: 'ai-music-studio',
    title: 'MuseFlow AI 音乐创作',
    category: 'creative',
    tags: ['AI', '音乐', '暗色主题', '创意工具'],
    colors: ['#0a0a0f', '#8b5cf6', '#ec4899'],
    rating: 9.5,
    description: '暗色极简 AI 音乐创作工具落地页，灵感来自 Haptic.app，CSS 音频波形动画 + 手机模型 + 哲学叙事 + 定价卡片',
  },
  {
    id: 'streetwear-store',
    title: 'KŌDA 运动潮牌商城',
    category: 'ecommerce',
    tags: ['电商', '潮牌', '暗色主题', '运动品牌', 'Marquee'],
    colors: ['#0a0a0a', '#ff4d00', '#00ff88'],
    rating: 9.5,
    description: '暗色系运动潮牌商城，灵感来自 Outfit/ASICS/Nike SNKRS，包含 Hero 网格背景 + Marquee 滚动 + 产品网格 + Quick Add 浮层 + 特色产品规格展示 + 品牌宣言',
  },
  {
    id: 'coffee-subscription',
    title: 'Terroir Coffee 精品咖啡电商',
    category: 'ecommerce',
    tags: ['电商', '咖啡', '订阅', '精品', '暖色'],
    colors: ['#FAF8F4', '#3C2415', '#C9A96E'],
    rating: 9.4,
    description: '精品咖啡品牌电商，灵感来自 WatchHouse，暗色 Hero + 胶片噪点 + Marquee 滚动 + 产品卡片 + 订阅方案 + 产地故事',
  },
  {
    id: 'luxury-candle',
    title: 'Maison Lumière 奢华香薰蜡烛',
    category: 'ecommerce',
    tags: ['电商', '香薰', '蜡烛', '奢华', '暗色'],
    colors: ['#08080d', '#C9A96E', '#C4722F'],
    rating: 9.5,
    description: '奢华香薰蜡烛品牌电商，暗色 Hero + 浮动光球动画 + CSS 蜡烛火焰 + 产品网格 + 品牌故事 + 用户评价',
  },
  {
    id: 'help-center',
    title: 'Pulse 帮助中心',
    category: 'content',
    tags: ['帮助中心', '知识库', 'FAQ', '搜索', '客服'],
    colors: ['#0f0f23', '#6366f1', '#f8fafc'],
    rating: 9.4,
    description: '现代 SaaS 帮助中心，暗色渐变搜索 Hero + 分类网格 + 热门文章 + 编辑推荐 + FAQ 手风琴 + 联系 CTA',
  },
  {
    id: 'wine-ecommerce',
    title: 'Cuvée Noir 葡萄酒电商',
    category: 'ecommerce',
    tags: ['电商', '葡萄酒', '奢华', '暗色主题'],
    colors: ['#08080d', '#C41E3A', '#C9A96E'],
    rating: 9.4,
    description: '暗色系奢华葡萄酒电商，灵感来自 Awwwards 精选电商，SVG 酒杯装饰 + 品鉴笔记风味轮 + 庄萄园故事 + 会员俱乐部定价',
  },
  {
    id: 'type-foundry',
    title: 'Mono Type Foundry 字体铸造厂',
    category: 'creative',
    tags: ['字体铸造厂', '排版', '暗色主题', 'Marquee'],
    colors: ['#0a0a0a', '#c9a96e', '#f5f0eb'],
    rating: 9.5,
    description: '暗色系字体铸造厂落地页，灵感来自 SILENCIO/monotype，超大排版 Hero + Marquee 滚动 + 字体展示网格 + 双向大字排版 + 服务列表',
  },
  {
    id: 'split-panel-portfolio',
    title: 'Studio Prism 创意总监作品集',
    category: 'portfolio',
    tags: ['作品集', '分屏布局', '衬线字体', '暗色主题', '创意总监'],
    colors: ['#0a0a0a', '#ffffff', '#333333'],
    rating: 9.5,
    description: '灵感来自 endless.design/andagain.uk 的分屏布局创意总监作品集，左侧固定边栏 + 右侧滚动画廊 + Playfair Display 衬线字体 + Marquee 滚动 + 数字计数器动画',
  },
  {
    id: 'knowledge-base',
    title: 'NexusBase 知识库中心',
    category: 'content',
    tags: ['知识库', 'Wiki', '技术文档', '阅读体验', '分类导航'],
    colors: ['#0f172a', '#6366f1', '#fafbfc'],
    rating: 9.4,
    description: '灵感来自 WikiWand 的现代知识库中心，深色侧边栏 + 精选文章渐变 Hero + 分类药丸筛选 + 文章卡片网格 + 热门排行 + 标签云 + 更新日志',
  },
  {
    id: 'beauty-skincare',
    title: 'AURA Beauty 美妆电商',
    category: 'ecommerce',
    tags: ['美妆', '护肤', '纯净美妆', '电商', '玫瑰金'],
    colors: ['#c9a087', '#faf8f5', '#1a1a1a'],
    rating: 9.4,
    description: '高端纯净美妆电商，Cormorant Garamond 衬线字体 + 玫瑰金配色 + 产品浮动动画 + 成分轨道旋转 + 护肤步骤流程 + Instagram 网格',
  },
  {
    id: 'canvas-generative-art',
    title: 'Canvas 创意编码工作室',
    category: 'creative',
    tags: ['生成艺术', '创意编码', '暗色主题', 'CSS动画', 'Shader'],
    colors: ['#05050a', '#00d4ff', '#6366f1'],
    rating: 9.5,
    description: '暗色系创意编码工作室落地页，CSS-only 生成艺术画廊 + 动态模糊光球背景 + 斐波那契螺旋 + 矩阵雨 + 无限滚动 Marquee',
  },
  {
    id: 'art-gallery',
    title: 'Galerie Noir 当代艺术画廊',
    category: 'portfolio',
    tags: ['艺术画廊', '极简', '衬线字体', 'Marquee', '展览'],
    colors: ['#faf9f7', '#1a1a1a', '#c9a96e'],
    rating: 9.5,
    description: '博物馆级当代艺术画廊，灵感来自 Goodman Gallery，Playfair Display 衬线字体 + 12 列不等宽作品网格 + CSS 抽象艺术装饰 + Marquee 滚动 + 展览日程',
  },
  {
    id: 'project-management',
    title: 'TaskPilot 项目管理仪表盘',
    category: 'app',
    tags: ['项目管理', '看板', '暗色主题', '仪表盘', '团队协作'],
    colors: ['#0a0a12', '#6366f1', '#10b981'],
    rating: 9.4,
    description: '暗色系项目管理仪表盘，毛玻璃侧边栏 + SVG 圆环进度图 + Kanban 看板 + 任务卡片 + 团队动态 + 截止日期追踪',
  },
  {
    id: 'sentinel-guard',
    title: 'SentinelGuard 零信任安全平台',
    category: 'landing',
    tags: ['零信任', '安全', 'SaaS', '暗色主题', '企业'],
    colors: ['#06060f', '#00d4ff', '#6366f1'],
    rating: 9.4,
    description: '零信任安全 SaaS 落地页，暗色科技风 + 电光青配色 + CSS 产品控制台 Demo + 六宫格特性 + 三栏定价',
  },
  {
    id: 'inkwell-editorial',
    title: 'InkWell 长文阅读体验',
    category: 'content',
    tags: ['长文阅读', '编辑设计', '排版', '字体', '沉浸式'],
    colors: ['#faf9f7', '#c9a96e', '#1a1a1a'],
    rating: 9.5,
    description: '沉浸式长文阅读体验，灵感来自 Medium/The Pudding，阅读进度条 + 浮动目录 + 首字下沉 + Pull Quote + CSS 几何插图 + Newsletter CTA',
  },
  {
    id: 'beverage-brand',
    title: 'Fizz & Folk 气泡饮品品牌',
    category: 'ecommerce',
    tags: ['电商', '气泡饮品', '品牌官网', '波浪设计', '欧洲风格'],
    colors: ['#FE3E29', '#F4F2EA', '#1A1A1A'],
    rating: 9.3,
    description: '西班牙手工气泡饮品品牌 — 波浪有机 Hero + 双色调撞色 + CSS 瓶身插画 + 无限 Marquee + 产品卡片网格 + Newsletter 订阅',
  },
  {
    id: 'courier-app',
    title: 'Courier 暗色邮件客户端',
    category: 'app',
    tags: ['邮件客户端', '暗色主题', '极简设计', '应用界面'],
    colors: ['#0A0A0A', '#5890E7', '#141414'],
    rating: 9.4,
    description: '暗色极简邮件客户端 — 三栏邮件 UI mockup + Serif Hero + 毛玻璃按钮 + 速度对比动画 + 键盘快捷键网格 + 安全特性展示',
  },
  {
    id: 'motion-studio',
    title: 'Kinetic Studio 动态设计工作室',
    category: 'creative',
    tags: ['动态设计', '视频制作', '暗色主题', 'Bento Grid', 'Marquee'],
    colors: ['#06060c', '#6366f1', '#ec4899'],
    rating: 9.4,
    description: '暗色系动态设计工作室落地页，浮动光球背景 + 渐变文字 Hero + Showreel 视频区 + CSS 时间线进度条 + Bento Grid 服务网格 + 作品展示 + Marquee 客户滚动',
  },
  {
    id: 'voltara-ev',
    title: 'Voltara Electric 电动汽车',
    category: 'industry',
    tags: ['电动汽车', '品牌落地页', '暗色主题', '科技', '汽车'],
    colors: ['#050508', '#00d4ff', '#ffffff'],
    rating: 9.5,
    description: '暗色科技风电动汽车品牌落地页，CSS 汽车剪影 + 电光青发光动效 + 车型矩阵卡片 + 续航环形进度条 + 轨道粒子动画',
  },
  {
    id: 'fintech-payment-landing',
    title: 'WeroPay 支付平台落地页',
    category: 'landing',
    tags: ['金融科技', '支付平台', 'B2B', '暖色调', 'Scrollytelling'],
    colors: ['#F9E9A9', '#FF678B', '#0d0d1a'],
    rating: 9.3,
    description: '暖色调金融科技支付平台落地页，淡黄 Hero + 深浅区块交替 + CSS 支付流转动画 + 智能仪表盘可视化 + 盾牌安全动效 + 三栏定价 + FAQ 手风琴',
  },
  {
    id: 'customer-stories',
    title: 'CaseFlow 客户故事集',
    category: 'content',
    tags: ['客户故事', '案例研究', '暗色主题', 'Grid 布局'],
    colors: ['#010314', '#6366f1', '#8b5cf6'],
    rating: 9.4,
    description: '暗色科技风客户故事集，3 列网格十字分隔线 + 半透明卡片叠加 + 紫色辉光 Hero + 数据统计条 + 推荐引言 + 脉冲发光 CTA',
  },
  {
    id: 'dev-portfolio',
    title: 'DevForge 创意开发者作品集',
    category: 'portfolio',
    tags: ['开发者', '作品集', '终端美学', '暗色主题'],
    colors: ['#08080d', '#00d4ff', '#a855f7'],
    rating: 9.5,
    description: '暗色系创意开发者作品集，终端风格 Hero + 打字机动画 + 项目网格渐变预览 + 技能进度条 + 时间线经历 + CSS 网格线背景',
  },
  {
    id: 'logistics-hero',
    title: 'FleetPulse 物流运输平台',
    category: 'industry',
    tags: ['物流运输', '工业风', '暗色主题', '行业垂直', '车队展示'],
    colors: ['#111111', '#2563eb', '#fafafa'],
    rating: 9.4,
    description: '工业风物流运输平台落地页，Barlow Condensed 超粗体标题 + 三步服务卡片 + 滚动字幕 + 浅色车队展示 + 时间线流程 + CSS 地图脉冲点',
  },
  {
    id: 'event-studio',
    title: 'Luminary 活动策划工作室',
    category: 'landing',
    tags: ['活动策划', '品牌活动', '沉浸式体验', '暗色主题', '企业'],
    colors: ['#131313', '#352CDB', '#E8E6E2'],
    rating: 9.4,
    description: '企业活动策划工作室落地页，灵感来自 Truck\'N Roll，超粗体大写标题 + 深浅区块交替 + 编号流程 + 作品画廊 + 客户评价',
  },
  {
    id: 'jewelry-luxe',
    title: 'LUMIÈRE 奢华珠宝商城',
    category: 'ecommerce',
    tags: ['珠宝', '奢华', '电商', '深色Hero', 'Marquee'],
    colors: ['#0a1628', '#c9a96e', '#faf8f5'],
    rating: 9.5,
    description: '奢华珠宝品牌电商，灵感来自 Tamannaah Fine Jewellery，深海军蓝 Hero + 菱形浮动动画 + 粒子闪烁 + Marquee 滚动 + 产品网格 + 品牌传承分栏 + 客户评价',
  },
  {
    id: 'lux-audio-studio',
    title: 'Lux Audio 音效工作室',
    category: 'creative',
    tags: ['音效设计', '暗色主题', '创意工作室', '波形动画', '横滚画廊'],
    colors: ['#06060c', '#ff6b35', '#06b6d4'],
    rating: 9.4,
    description: '暗色系音效设计工作室落地页，CSS 音频波形条动画 + 脉冲环形装饰 + 横向滚动画廊 + 毛玻璃导航 + 噪点纹理 + 四栏流程网格 + 客户评价',
  },
  {
    id: 'calendar-app',
    title: 'Chronos 日历与事件规划器',
    category: 'app',
    tags: ['日历', '事件管理', '暗色主题', '应用界面', '数据可视化'],
    colors: ['#0a0a12', '#6366f1', '#818cf8'],
    rating: 9.4,
    description: '暗色系日历与事件规划器，三栏应用布局 + 月视图网格 + 彩色事件标签 + 环形进度图 + 迷你日历 + 每周活动柱状图 + 新建事件弹窗',
  },
  {
    id: 'freelance-portfolio',
    title: 'Lena Voss 独立电影人作品集',
    category: 'portfolio',
    tags: ['电影', '作品集', '暗色主题', '衬线字体', '横向滚动'],
    colors: ['#0a0a0f', '#c9a96e', '#1a1a1a'],
    rating: 9.5,
    description: '暗色系独立电影人作品集，Playfair Display 衬线字体 + 胶片噪点纹理 + 横向滚动画廊 + 交错项目展示 + 毛玻璃导航',
  },
  {
    id: 'recipe-blog',
    title: 'TasteNote 美食食谱博客',
    category: 'content',
    tags: ['食谱', '美食博客', '编辑设计', '暖色调', '衬线字体'],
    colors: ['#faf8f4', '#3C2415', '#C9705B'],
    rating: 9.4,
    description: '暖色调美食食谱博客，DM Serif Display 衬线字体 + CSS 渐变食物插画 + 食谱网格 + 分类筛选 + Newsletter 订阅',
  },
  {
    id: 'design-marketplace',
    title: 'GridWork 设计素材商城',
    category: 'ecommerce',
    tags: ['设计素材', '电商', '瑞士风格', 'Mockup商城', '产品网格'],
    colors: ['#fafafa', '#1a1a1a', '#6366f1'],
    rating: 9.3,
    description: '瑞士风格设计素材商城，Space Mono 等宽字体编号系统 + 1px 网格布局 + 产品卡片 Hover 扫描线动画 + Tab 分类筛选 + Newsletter 订阅',
  },
  {
    id: 'luxury-hotel',
    title: 'Aurelio Resort 奢华度假酒店',
    category: 'industry',
    tags: ['奢华酒店', '意大利', '度假', '衬线字体', '暖色调'],
    colors: ['#f8f6f3', '#c4a882', '#1a1a1a'],
    rating: 9.5,
    description: '灵感来自 Relais Rossar 的奢华度假酒店，Playfair Display 衬线字体 + 暖色奶油底 + CSS 渐变客房画廊 + 暗色设施网格 + 编号体验列表 + 预订栏',
  },
  {
    id: 'vc-investment-landing',
    title: 'Meridian Capital 投资机构落地页',
    category: 'landing',
    tags: ['投资机构', '私募股权', '企业落地页', '编辑排版', '地图'],
    colors: ['#ffffff', '#C41E3A', '#0A0A0A'],
    rating: 9.4,
    description: '灵感来自 Tresmares Capital 的另类投资机构落地页，不对称大标题 Hero + 深色统计栏 + 投资方案卡片网格 + 欧洲地图脉冲动画 + 团队成员展示',
  },
  {
    id: 'saas-onboarding',
    title: 'Pulse SaaS 引导向导',
    category: 'app',
    tags: ['SaaS', 'Onboarding', '多步表单', '暗色主题', '向导'],
    colors: ['#0a0a12', '#6366f1', '#06b6d4'],
    rating: 9.4,
    description: 'SaaS 多步骤引导向导，灵感来自现代 SaaS 首次使用流程，步骤进度条 + 毛玻璃卡片 + 角色选择器 + 团队邀请 + 完成庆祝动画',
  },
  {
    id: 'sound-studio',
    title: 'Sonora Sound 音效设计工作室',
    category: 'creative',
    tags: ['音效设计', '创意工作室', '分屏布局', 'Marquee'],
    colors: ['#E8E4E0', '#0a0a0a', '#E85D4A'],
    rating: 9.4,
    description: '暖色调音效设计工作室，灵感来自 Field Day Sound，分屏 Hero + 品牌 Marquee + CSS 波形动画作品展示 + 客户评价',
  },
  {
    id: 'design-resources',
    title: 'DesignMint 设计资源目录',
    category: 'content',
    tags: ['资源目录', '设计工具', '内容策展', 'Marquee'],
    colors: ['#0d9488', '#06b6d4', '#fafbfc'],
    rating: 9.4,
    description: '精选设计资源目录，毛玻璃导航 + 渐变 Hero + 分类筛选 + 编辑精选 + 横向滚动热门 + 资源卡片网格 + Newsletter',
  },
  {
    id: 'space-tourism',
    title: 'Cosmos Express 太空旅行',
    category: 'industry',
    tags: ['太空旅游', '暗色主题', '科技', 'CSS动画', '沉浸式'],
    colors: ['#050510', '#00d4ff', '#8b5cf6'],
    rating: 9.5,
    description: '沉浸式太空旅游落地页，CSS 星空粒子背景 + 轨道环装饰 + CSS-only 行星插画 + 旅程时间线 + 定价三栏 + FAQ 手风琴',
  },
  {
    id: 'atelier-brand',
    title: 'MONO&CO 品牌设计工作室',
    category: 'portfolio',
    tags: ['品牌设计', '视觉识别', '作品集', '衬线字体', 'Marquee'],
    colors: ['#faf9f7', '#0f0f0f', '#c41e3a'],
    rating: 9.5,
    description: '品牌设计工作室作品集，灵感来自 Pentagram/Moving Brands，Playfair Display 衬线字体 + 深浅区块交替 + CSS 品牌视觉 + Marquee 客户滚动 + 案例详情 + 服务网格',
  },
  {
    id: 'sprout-ai',
    title: 'Sprout AI 可爱机器人伙伴',
    category: 'landing',
    tags: ['AI', '机器人', '落地页', '插画风格', '动画'],
    colors: ['#D1E3FF', '#4ade80', '#22d3ee'],
    rating: 9.4,
    description: 'AI 机器人伙伴落地页，灵感来自 Fauna Robotics，CSS 纯手绘机器人角色 + Blob 渐变背景动画 + 功能网格 + 使用步骤 + 用户评价',
  },
  {
    id: 'cinema-noir',
    title: 'FRAME 黑色电影数字体验',
    category: 'creative',
    tags: ['黑色电影', '暗色主题', 'CSS动画', '水平滚动', '电影'],
    colors: ['#08080d', '#c9a96e', '#faf8f5'],
    rating: 9.5,
    description: '暗色电影体验页，灵感来自 Awwwards 黑色电影美学，CSS-only 电影场景画廊 + 胶片齿孔 + 同心圆取景器 + 霓虹闪烁 + 雨中剪影 + 导演语录 + 档案网格',
  },
]

const categories = [
  { id: 'all', label: '全部', icon: '🎨' },
  { id: 'landing', label: 'SaaS 落地页', icon: '🚀' },
  { id: 'portfolio', label: '作品集 & 机构', icon: '💼' },
  { id: 'app', label: '应用 & 仪表盘', icon: '📊' },
  { id: 'ecommerce', label: '电商', icon: '🛒' },
  { id: 'creative', label: '创意页面', icon: '✨' },
  { id: 'content', label: '内容 & 编辑', icon: '📝' },
  { id: 'industry', label: '行业垂直', icon: '🌍' },
]

const activeCategory = ref('all')
const searchQuery = ref('')

// 过滤逻辑：支持分类 + 搜索
const filteredPages = computed(() => {
  let result = pages
  if (activeCategory.value !== 'all') {
    result = result.filter(p => p.category === activeCategory.value)
  }
  if (searchQuery.value.trim()) {
    const q = searchQuery.value.toLowerCase()
    result = result.filter(p =>
      p.title.toLowerCase().includes(q) ||
      p.description.toLowerCase().includes(q) ||
      p.tags.some(t => t.toLowerCase().includes(q))
    )
  }
  return result
})

// 分组视图："全部"且无搜索时，按分类分组展示
const groupedPages = computed(() => {
  if (activeCategory.value !== 'all' || searchQuery.value.trim()) return null
  const groups = []
  for (const cat of categories) {
    if (cat.id === 'all') continue
    const catPages = pages.filter(p => p.category === cat.id).sort((a, b) => b.rating - a.rating)
    if (catPages.length > 0) {
      groups.push({ ...cat, pages: catPages })
    }
  }
  return groups
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
    <meta name="description" content="My Design Lib 页面灵感画廊 — 80 个完整页面设计展示，包含 SaaS 落地页、作品集、仪表盘、电商、创意页面、行业模板等。可预览、看源码、学设计。">
  <meta name="keywords" content="页面模板, 前端设计, SaaS模板, 作品集模板, 仪表盘模板, 电商模板, 404页面, 设计灵感">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="website">
  <meta property="og:title" content="🎨 页面灵感画廊 — My Design Lib">
    <meta property="og:description" content="80 个完整页面设计展示，像 Awwwards 一样浏览。SaaS 落地页、作品集、仪表盘等高质量页面模板。">
  <meta property="og:url" content="http://101.37.166.208:11930/pages/">
  <link rel="canonical" href="http://101.37.166.208:11930/pages/">

  <!-- Hero -->
  <div class="gallery-hero">
    <h1>🎨 页面灵感画廊</h1>
    <p>完整的页面设计展示，点击即可预览实时效果，查看源码</p>
    <div class="hero-stats">
      <span>📦 80 个完整页面</span>
      <span>🏷️ 7 个分类</span>
      <span>🔄 每日自动更新</span>
    </div>
  </div>

  <!-- Toolbar: Search + Filter -->
  <div class="gallery-toolbar">
    <div class="search-box">
      <svg class="search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      <input
        v-model="searchQuery"
        type="text"
        placeholder="搜索页面名称、描述或标签..."
        class="search-input"
      />
      <button v-if="searchQuery" @click="searchQuery = ''" class="search-clear" title="清除搜索">✕</button>
    </div>
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
  </div>

  <!-- Search result hint -->
  <div v-if="searchQuery.trim()" class="search-result-hint">
    🔍 找到 <strong>{{ filteredPages.length }}</strong> 个匹配页面
  </div>

  <!-- ===== 分组视图（"全部" + 无搜索） ===== -->
  <template v-if="groupedPages">
    <div v-for="group in groupedPages" :key="group.id" class="gallery-section">
      <div class="section-header">
        <span class="section-icon">{{ group.icon }}</span>
        <span class="section-title">{{ group.label }}</span>
        <span class="section-count">{{ group.pages.length }}</span>
      </div>
      <div class="gallery-grid">
        <a
          v-for="page in group.pages"
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
            <div class="card-title-row">
              <h3>{{ page.title }}</h3>
              <span class="card-score" :style="{ color: getScoreColor(page.rating) }">{{ page.rating }}</span>
            </div>
            <p>{{ page.description }}</p>
            <div class="card-tags">
              <span v-for="tag in page.tags" :key="tag" class="tag">{{ tag }}</span>
            </div>
          </div>
        </a>
      </div>
    </div>
  </template>

  <!-- ===== 扁平视图（分类筛选 / 搜索） ===== -->
  <template v-else>
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
          <div class="card-title-row">
            <h3>{{ page.title }}</h3>
            <span class="card-score" :style="{ color: getScoreColor(page.rating) }">{{ page.rating }}</span>
          </div>
          <p>{{ page.description }}</p>
          <div class="card-tags">
            <span v-for="tag in page.tags" :key="tag" class="tag">{{ tag }}</span>
          </div>
        </div>
      </a>
    </div>
    <div v-if="filteredPages.length === 0" class="gallery-empty">
      没有找到匹配的页面 😅<br/>
      <button class="reset-btn" @click="searchQuery = ''; activeCategory = 'all'">重置筛选</button>
    </div>
  </template>

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
body:has(.gallery-page) main {
  max-width: none !important;
  width: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
}

/* 页面容器 */
.gallery-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 2rem 2rem;
}

/* Hero */
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

/* ===== Toolbar: Search + Filter ===== */
.gallery-toolbar {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin: 1.5rem 0;
}

.search-box {
  position: relative;
  display: flex;
  align-items: center;
  max-width: 480px;
  margin: 0 auto;
  width: 100%;
}
.search-icon {
  position: absolute;
  left: 14px;
  color: #999;
  pointer-events: none;
}
.search-input {
  width: 100%;
  padding: 0.7rem 2.5rem 0.7rem 2.8rem;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  font-size: 0.95rem;
  color: #333;
  background: #fff;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.search-input:focus {
  border-color: #6366f1;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}
.search-input::placeholder { color: #aaa; }
.search-clear {
  position: absolute;
  right: 10px;
  background: none;
  border: none;
  font-size: 1rem;
  color: #999;
  cursor: pointer;
  padding: 4px 6px;
  border-radius: 50%;
  line-height: 1;
}
.search-clear:hover { background: #f3f4f6; color: #333; }

.search-result-hint {
  text-align: center;
  color: #888;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

/* Filter */
.gallery-filter {
  display: flex;
  gap: 0.5rem;
  justify-content: center;
  flex-wrap: wrap;
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

/* ===== Section Headers (Grouped View) ===== */
.gallery-section {
  margin-top: 2.5rem;
}
.gallery-section:first-child {
  margin-top: 1rem;
}
.section-header {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding-bottom: 0.8rem;
  border-bottom: 2px solid #f0f0f0;
  margin-bottom: 1.2rem;
}
.section-icon {
  font-size: 1.3rem;
}
.section-title {
  font-size: 1.2rem;
  font-weight: 700;
  color: #1a1a1a;
}
.section-count {
  font-size: 0.8rem;
  color: #999;
  background: #f3f4f6;
  padding: 2px 10px;
  border-radius: 100px;
}

/* Grid */
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 2rem;
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

/* Info */
.card-info { padding: 1.2rem; background: #fff; }
.card-title-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.3rem;
}
.card-title-row h3 { font-size: 1.1rem; font-weight: 700; margin: 0; }
.card-score {
  font-size: 1rem;
  font-weight: 800;
  flex-shrink: 0;
  margin-left: 0.5rem;
}
.card-info p { font-size: 0.85rem; color: #666; line-height: 1.5; margin-bottom: 0.8rem; }
.card-tags { display: flex; gap: 0.4rem; flex-wrap: wrap; }
.tag {
  padding: 0.2rem 0.6rem;
  background: #f3f4f6;
  border-radius: 6px;
  font-size: 0.75rem;
  color: #666;
}

/* Empty state */
.gallery-empty {
  text-align: center;
  padding: 4rem 2rem;
  color: #999;
  font-size: 1.1rem;
  line-height: 2;
}
.reset-btn {
  margin-top: 0.5rem;
  padding: 0.5rem 1.5rem;
  border: 1px solid #e5e7eb;
  border-radius: 100px;
  background: #fff;
  cursor: pointer;
  font-size: 0.9rem;
  color: #6366f1;
  transition: all 0.2s;
}
.reset-btn:hover {
  background: #6366f1;
  color: #fff;
  border-color: #6366f1;
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

/* Responsive */
@media (max-width: 640px) {
  .gallery-grid { grid-template-columns: 1fr; }
  .gallery-hero h1 { font-size: 1.8rem; }
  .hero-stats { flex-direction: column; gap: 0.5rem; }
  .gallery-filter { gap: 0.35rem; }
  .filter-btn { padding: 0.4rem 0.9rem; font-size: 0.8rem; }
  .section-title { font-size: 1rem; }
}
</style>
