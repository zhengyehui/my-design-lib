import { defineConfig } from 'vitepress'

// All component CSS files
const componentCSS = [
  'button', 'badge', 'avatar', 'toggle',
  'input', 'dropdown',
  'card', 'hero', 'navbar', 'footer', 'table', 'tabs', 'accordion', 'breadcrumb',
  'modal', 'alert', 'toast', 'tooltip', 'progress',
  'glassmorphism', 'gradient-border', 'skeleton', '3d-tilt', 'aurora-bg', 'magnetic-btn'
]

// Vite plugin to escape HTML in markdown preview sections
function markdownHtmlEscape() {
  return {
    name: 'markdown-html-escape',
    transform(code, id) {
      if (!id.endsWith('.md')) return null
      // Replace raw HTML demo sections with escaped version wrapped in v-pre
      // This prevents Vue from compiling the HTML as Vue templates
      let result = code
      // Find HTML blocks that are NOT inside ``` code fences
      // and wrap them in <!-- v-pre --> markers
      const lines = result.split('\n')
      let inCodeBlock = false
      let inHtmlBlock = false
      let htmlBlockStart = -1
      const output = []
      
      for (let i = 0; i < lines.length; i++) {
        const line = lines[i]
        
        if (line.trim().startsWith('```')) {
          inCodeBlock = !inCodeBlock
          output.push(line)
          continue
        }
        
        if (!inCodeBlock && line.match(/^<[a-z]/)) {
          if (!inHtmlBlock) {
            inHtmlBlock = true
            htmlBlockStart = i
            output.push(line)
            continue
          }
        }
        
        if (inHtmlBlock && !line.match(/^\s/) && !line.match(/^<[a-z]/) && !line.match(/^<!--/) && line.trim() !== '') {
          inHtmlBlock = false
        }
        
        output.push(line)
      }
      
      return output.join('\n')
    }
  }
}

export default defineConfig({
  title: 'My Design Lib',
  description: '个人 AI-friendly 前端设计库',
  base: '/',

  head: [
    // SEO 基础 meta
    ['meta', { name: 'description', content: 'My Design Lib — 为 AI 编程助手优化的前端设计库。25 个纯 HTML+CSS 组件，126 个完整页面灵感，Design Tokens，零框架依赖，复制即用。' }],
    ['meta', { name: 'keywords', content: '前端组件库, AI设计库, HTML CSS组件, 页面模板, 设计系统, Design Tokens, 免费组件, SaaS模板' }],
    ['meta', { name: 'author', content: 'My Design Lib' }],
    ['meta', { name: 'robots', content: 'index, follow, max-image-preview:large' }],

    // Open Graph（社交分享）
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'My Design Lib — 你的设计，AI 来加速' }],
    ['meta', { property: 'og:description', content: '为 AI 编程助手优化的前端设计库。25 个组件 + 126 个完整页面，纯 HTML+CSS，零依赖。' }],
    ['meta', { property: 'og:url', content: 'http://101.37.166.208:11930' }],
    ['meta', { property: 'og:site_name', content: 'My Design Lib' }],
    ['meta', { property: 'og:locale', content: 'zh_CN' }],

    // Twitter Card
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:title', content: 'My Design Lib — 你的设计，AI 来加速' }],
    ['meta', { name: 'twitter:description', content: '为 AI 编程助手优化的前端设计库。25 个组件 + 126 个完整页面，纯 HTML+CSS，零依赖。' }],

    // Schema.org 结构化数据
    ['script', { type: 'application/ld+json' }, JSON.stringify({
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "My Design Lib",
      "description": "为 AI 编程助手优化的前端设计库，包含 25 个组件和 126 个完整页面",
      "url": "http://101.37.166.208:11930",
      "applicationCategory": "DeveloperApplication",
      "operatingSystem": "Web",
      "offers": { "@type": "Offer", "price": "0", "priceCurrency": "CNY" },
      "author": { "@type": "Organization", "name": "My Design Lib" },
      "hasPart": [
        { "@type": "SoftwareSourceCode", "name": "Button Component", "programmingLanguage": "CSS" },
        { "@type": "SoftwareSourceCode", "name": "Card Component", "programmingLanguage": "CSS" },
        { "@type": "SoftwareSourceCode", "name": "Modal Component", "programmingLanguage": "CSS" }
      ]
    })],

    // AI 爬虫友好
    ['meta', { name: 'ai-content-type', content: 'design-library' }],
    ['meta', { name: 'ai-description', content: '前端设计库：25个HTML+CSS组件，126个完整页面模板，Design Tokens。可直接复制使用。' }],

    ['link', { rel: 'stylesheet', href: '/tokens/tokens.css' }],
    ...componentCSS.map(name => [
      'link',
      { rel: 'stylesheet', href: `/components/${name}/${name}.css` }
    ])
  ],

  vue: {
    template: {
      compilerOptions: {
        // Tell Vue to treat all elements as native (no validation)
        isNativeTag: () => true,
        // Disable whitespace preservation issues
        whitespace: 'condense'
      }
    }
  },

  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '组件', link: '/components/button' },
      { text: '设计变量', link: '/tokens/colors' },
      { text: '布局模式', link: '/patterns/landing' },
      { text: '🎨 页面画廊', link: '/pages/' },
      { text: '🤝 赞助', link: '/sponsor' }
    ],

    sidebar: {
      '/components/': [
        {
          text: '📚 快速开始',
          collapsed: false,
          items: [
            { text: '组件库概览', link: '/components/button' }
          ]
        },
        {
          text: '🎯 核心基础',
          collapsed: false,
          items: [
            { text: 'Button 按钮', link: '/components/button' },
            { text: 'Badge 徽章', link: '/components/badge' },
            { text: 'Avatar 头像', link: '/components/avatar' },
            { text: 'Toggle 开关', link: '/components/toggle' }
          ]
        },
        {
          text: '📝 数据输入',
          collapsed: false,
          items: [
            { text: 'Input 输入框', link: '/components/input' },
            { text: 'Dropdown 下拉菜单', link: '/components/dropdown' }
          ]
        },
        {
          text: '📦 容器与布局',
          collapsed: false,
          items: [
            { text: 'Card 卡片', link: '/components/card' },
            { text: 'Hero 首屏', link: '/components/hero' },
            { text: 'Navbar 导航栏', link: '/components/navbar' },
            { text: 'Footer 页脚', link: '/components/footer' },
            { text: 'Table 表格', link: '/components/table' },
            { text: 'Tabs 标签页', link: '/components/tabs' },
            { text: 'Accordion 折叠面板', link: '/components/accordion' },
            { text: 'Breadcrumb 面包屑', link: '/components/breadcrumb' }
          ]
        },
        {
          text: '💬 用户反馈',
          collapsed: false,
          items: [
            { text: 'Modal 对话框', link: '/components/modal' },
            { text: 'Alert 提示', link: '/components/alert' },
            { text: 'Toast 通知', link: '/components/toast' },
            { text: 'Tooltip 工具提示', link: '/components/tooltip' },
            { text: 'Progress 进度条', link: '/components/progress' }
          ]
        },
        {
          text: '✨ 创意与炫彩',
          collapsed: false,
          items: [
            { text: 'Glassmorphism 毛玻璃', link: '/components/glassmorphism' },
            { text: 'Gradient Border 渐变边框', link: '/components/gradient-border' },
            { text: 'Skeleton 骨架屏', link: '/components/skeleton' },
            { text: '3D Tilt 倾斜卡片', link: '/components/3d-tilt' },
            { text: 'Aurora 极光背景', link: '/components/aurora-bg' },
            { text: 'Magnetic Button 磁性按钮', link: '/components/magnetic-btn' }
          ]
        }
      ],
      '/tokens/': [
        {
          text: '🎨 Design Tokens',
          collapsed: false,
          items: [
            { text: '系统概览', link: '/tokens/colors' },
            { text: 'Colors 颜色系统', link: '/tokens/colors' },
            { text: 'Typography 排版系统', link: '/tokens/typography' },
            { text: 'Spacing 间距系统', link: '/tokens/spacing' }
          ]
        }
      ],
      '/patterns/': [
        {
          text: '🏗️ 布局模式',
          collapsed: false,
          items: [
            { text: 'Landing Page 落地页', link: '/patterns/landing' },
            { text: 'Dashboard 仪表盘', link: '/patterns/dashboard' }
          ]
        }
      ],
      '/pages/': [
        {
          text: '🎨 页面画廊',
          collapsed: false,
          items: [
            { text: '全部页面', link: '/pages/' }
          ]
        },
        {
          text: '🚀 SaaS 落地页',
          collapsed: true,
          items: [
            { text: 'TechConf 科技大会', link: '/pages/conference-landing' },
            { text: '3D 互动落地页', link: '/pages/3d-interactive-landing' },
            { text: 'Ember Kitchen 餐厅', link: '/pages/restaurant-ember' },
            { text: 'NexusAI 智能平台', link: '/pages/ai-saas-landing' },
            { text: 'FlowDesk 极简产品', link: '/pages/product-minimal' },
            { text: 'CloudStack 定价页', link: '/pages/pricing-page' },
            { text: 'NovaPay SaaS', link: '/pages/saas-landing' },
            { text: 'SentinelGuard 安全', link: '/pages/sentinel-guard' },
            { text: 'WeroPay 支付平台', link: '/pages/fintech-payment-landing' },
            { text: 'Luminary 活动策划', link: '/pages/event-studio' },
            { text: 'Meridian Capital 投资机构', link: '/pages/vc-investment-landing' },
            { text: 'Sprout AI 可爱机器人伙伴', link: '/pages/sprout-ai' },
            { text: 'Pulse Board 任务管理', link: '/pages/pulse-board' },
            { text: 'NexusConnect 集成生态', link: '/pages/ecosystem-connect' },
            { text: 'InfraDocs 知识基础设施', link: '/pages/infradocs-platform' },
            { text: 'Interfere 编辑风格 SaaS', link: '/pages/interfere-saas' },
            { text: 'Nominal AI 财务自动化', link: '/pages/nominal-ai' },
            { text: 'SupportFlow AI 客户支持', link: '/pages/supportflow' },
            { text: 'CodeLens AI 代码审查', link: '/pages/codelens-review' }
          ]
        },
        {
          text: '💼 作品集 & 机构',
          collapsed: true,
          items: [
            { text: 'Arclight 品牌重塑', link: '/pages/case-study' },
            { text: '创意作品集', link: '/pages/portfolio' },
            { text: 'VOID 创意工作室', link: '/pages/studio-creative' },
            { text: 'Atelier Noir 建筑设计', link: '/pages/architecture-studio' },
            { text: 'Studio Creative 设计机构', link: '/pages/agency-portfolio' },
            { text: 'Atelier Lumière 摄影', link: '/pages/photography-portfolio' },
            { text: 'Studio Prism 创意总监', link: '/pages/split-panel-portfolio' },
            { text: 'Galerie Noir 艺术画廊', link: '/pages/art-gallery' },
            { text: 'DevForge 开发者作品集', link: '/pages/dev-portfolio' },
            { text: 'Lena Voss 电影人作品集', link: '/pages/freelance-portfolio' },
            { text: 'MONO&CO 品牌设计工作室', link: '/pages/atelier-brand' },
            { text: 'INDEX Studio 极简主义事务所', link: '/pages/brutalist-agency' },
            { text: 'Forma Studio 动态设计工作室', link: '/pages/forma-studio' },
            { text: 'Kinetic Visions 水平滚动', link: '/pages/h-scroll-portfolio' },
            { text: 'Displace OS 桌面风格', link: '/pages/displace-os' },
            { text: 'Obsidian Editorial 编辑设计', link: '/pages/obsidian-editorial' },
            { text: 'Mono Grid 编辑风作品集', link: '/pages/mono-grid' }
          ]
        },
        {
          text: '📊 应用 & 仪表盘',
          collapsed: true,
          items: [
            { text: '数据分析仪表盘', link: '/pages/analytics-dashboard' },
            { text: 'SkyPulse 天气仪表盘', link: '/pages/weather-dashboard' },
            { text: 'NeoBank 数字银行', link: '/pages/fintech-app' },
            { text: 'AuthKit 现代认证页', link: '/pages/auth-modern' },
            { text: 'VitalFit 健身追踪', link: '/pages/fitness-app' },
            { text: 'NimbusDrive 云存储', link: '/pages/cloud-storage-app' },
            { text: 'TaskPilot 项目管理', link: '/pages/project-management' },
            { text: 'Nexus 数据仪表盘', link: '/pages/dashboard-dark' },
            { text: 'Courier 暗色邮件客户端', link: '/pages/courier-app' },
            { text: 'Chronos 日历事件规划器', link: '/pages/calendar-app' },
            { text: 'Pulse SaaS 引导向导', link: '/pages/saas-onboarding' },
            { text: 'CodeScope AI 代码监控', link: '/pages/code-monitor' },
            { text: 'NexusChat 团队通讯', link: '/pages/chat-app' },
            { text: 'Pipeline CRM 客户管理', link: '/pages/crm-dashboard' },
            { text: 'ZenMind 冥想正念应用', link: '/pages/meditation-app' },
            { text: 'Ticky 时间追踪仪表盘', link: '/pages/time-tracker' },
            { text: 'ZenFlow 番茄钟计时器', link: '/pages/focus-timer' },
            { text: 'Meridian 证券交易终端', link: '/pages/trading-terminal' }
          ]
        },
        {
          text: '🛒 电商',
          collapsed: true,
          items: [
            { text: 'KŌDA 运动潮牌商城', link: '/pages/streetwear-store' },
            { text: 'Lumina Pro 产品详情', link: '/pages/product-detail-premium' },
            { text: 'Bloom 生活方式电商', link: '/pages/product-showcase' },
            { text: 'ShopFlow 结账页', link: '/pages/checkout' },
            { text: 'Terroir Coffee 精品咖啡', link: '/pages/coffee-subscription' },
            { text: 'Maison Lumière 奢华香薰', link: '/pages/luxury-candle' },
            { text: 'Cuvée Noir 葡萄酒电商', link: '/pages/wine-ecommerce' },
            { text: 'AURA Beauty 美妆电商', link: '/pages/beauty-skincare' },
            { text: 'Fizz & Folk 气泡饮品', link: '/pages/beverage-brand' },
            { text: 'LUMIÈRE 奢华珠宝', link: '/pages/jewelry-luxe' },
            { text: 'GridWork 设计素材商城', link: '/pages/design-marketplace' },
            { text: 'Groove Vault 黑胶唱片', link: '/pages/vinyl-record-store' },
            { text: 'Terrain 户外探险装备', link: '/pages/terrain-outdoor' },
            { text: 'PETLUXE 奢华宠物家居', link: '/pages/pet-luxe' },
            { text: 'NOIR Parfum 奢华香水', link: '/pages/parfum-noir' },
            { text: 'Greenhouse 室内植物商店', link: '/pages/plant-shop' },
            { text: 'Meridian Horology 瑞士腕表', link: '/pages/meridian-horology' },
            { text: 'Wabi Ceramics 日式陶艺', link: '/pages/wabi-ceramics' },
            { text: 'ATELIER NOIR 极简时装', link: '/pages/brutalist-fashion' }
          ]
        },
        {
          text: '✨ 创意页面',
          collapsed: true,
          items: [
            { text: 'MuseFlow AI 音乐创作', link: '/pages/ai-music-studio' },
            { text: 'NexusForge 游戏工作室', link: '/pages/game-studio' },
            { text: 'WaveSync 音乐播放器', link: '/pages/music-player' },
            { text: 'SoundWave 播客频道', link: '/pages/podcast-show' },
            { text: '太空主题 404', link: '/pages/404-creative' },
            { text: 'Pulse 上线预告', link: '/pages/coming-soon' },
            { text: 'Mono 字体铸造厂', link: '/pages/type-foundry' },
            { text: 'Canvas 创意编码工作室', link: '/pages/canvas-generative-art' },
            { text: 'Kinetic 动态设计工作室', link: '/pages/motion-studio' },
            { text: 'Lux Audio 音效工作室', link: '/pages/lux-audio-studio' },
            { text: 'Sonora Sound 音效工作室', link: '/pages/sound-studio' },
            { text: 'FRAME 黑色电影数字体验', link: '/pages/cinema-noir' },
            { text: 'ECLAT 音乐节', link: '/pages/music-festival' },
            { text: 'LUMEN Awards 数字设计大奖', link: '/pages/lumen-awards' },
            { text: 'TYPE 排版宣言', link: '/pages/typo-manifesto' },
            { text: 'ReelCraft AI 视频创作', link: '/pages/reelcraft-ai' },
            { text: 'Lunar 21 沉浸太空体验', link: '/pages/lunar-21' },
            { text: 'Luminous Boundaries 虚拟展览', link: '/pages/virtual-exhibition' },
            { text: 'Lumière 策展电影放映', link: '/pages/film-screening' }
          ]
        },
        {
          text: '📝 内容 & 编辑',
          collapsed: true,
          items: [
            { text: 'InkWell 长文阅读', link: '/pages/inkwell-editorial' },
            { text: 'DevDocs 文档门户', link: '/pages/docs-portal' },
            { text: 'DevChronicle 技术博客', link: '/pages/tech-blog' },
            { text: 'Mono Journal 杂志', link: '/pages/magazine-editorial' },
            { text: 'FlowSync 更新日志', link: '/pages/saas-changelog' },
            { text: 'The Signal 订阅页', link: '/pages/newsletter-landing' },
            { text: 'Pulse 帮助中心', link: '/pages/help-center' },
            { text: 'NexusBase 知识库', link: '/pages/knowledge-base' },
            { text: 'CaseFlow 客户故事集', link: '/pages/customer-stories' },
            { text: 'TasteNote 美食食谱', link: '/pages/recipe-blog' },
            { text: 'DesignMint 设计资源目录', link: '/pages/design-resources' },
            { text: 'PulseWire 数字新闻杂志', link: '/pages/pulsewire-digest' },
            { text: 'ShipLog 开发者更新日志', link: '/pages/ship-log' },
            { text: 'PodWave 播客网络', link: '/pages/podcast-hub' },
            { text: 'StreamVault 沉浸式流媒体', link: '/pages/streamvault' },
            { text: 'Spectrum 设计系统文档', link: '/pages/design-system-docs' },
            { text: 'Schemas 学术期刊索引', link: '/pages/schemas-journal' },
            { text: 'Nexicon 设计术语参考', link: '/pages/design-glossary' }
          ]
        },
        {
          text: '🌍 行业垂直',
          collapsed: true,
          items: [
            { text: 'Luxe Estates 奢华房产', link: '/pages/real-estate-luxury' },
            { text: 'Voyager 旅行预订', link: '/pages/travel-booking' },
            { text: 'Lóvi Care AI 健康', link: '/pages/health-ai' },
            { text: 'NovaChain Web3 DeFi', link: '/pages/crypto-web3' },
            { text: 'Maison Élégance 时尚', link: '/pages/fashion-brand' },
            { text: 'LearnHub 在线学习', link: '/pages/edu-platform' },
            { text: 'TalentFlow 招聘平台', link: '/pages/job-board' },
            { text: 'Hope Forward 公益教育', link: '/pages/nonprofit-impact' },
            { text: 'Voltara Electric 电动汽车', link: '/pages/voltara-ev' },
            { text: 'FleetPulse 物流运输', link: '/pages/logistics-hero' },
            { text: 'Aurelio Resort 奢华酒店', link: '/pages/luxury-hotel' },
            { text: 'Cosmos Express 太空旅行', link: '/pages/space-tourism' },
            { text: 'Luum Workspace 共享办公', link: '/pages/coworking-space' },
            { text: 'Lex & Partners 现代律所', link: '/pages/lex-partners' },
            { text: 'FeastFlow 精选美食配送', link: '/pages/feastflow-delivery' },
            { text: 'Apex Motors 奢华超跑', link: '/pages/apex-motors' },
            { text: 'House of Honey 室内设计', link: '/pages/house-of-honey' },
            { text: 'Solace 水疗养生度假村', link: '/pages/solace-spa' }
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/zhengyehui/my-design-lib' }
    ],

    search: {
      provider: 'local'
    },

    footer: {
      message: '纯 HTML + CSS，零框架依赖，AI 友好',
      copyright: '联系方式：📧 weta_zheng@qq.com &nbsp;|&nbsp; 💬 微信 weta010730 &nbsp;|&nbsp; GitHub @zhengyehui'
    }
  }
})
