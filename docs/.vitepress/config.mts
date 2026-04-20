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
    ['meta', { name: 'description', content: 'My Design Lib — 为 AI 编程助手优化的前端设计库。25 个纯 HTML+CSS 组件，5 个完整页面灵感，Design Tokens，零框架依赖，复制即用。' }],
    ['meta', { name: 'keywords', content: '前端组件库, AI设计库, HTML CSS组件, 页面模板, 设计系统, Design Tokens, 免费组件, SaaS模板' }],
    ['meta', { name: 'author', content: 'My Design Lib' }],
    ['meta', { name: 'robots', content: 'index, follow, max-image-preview:large' }],

    // Open Graph（社交分享）
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'My Design Lib — 你的设计，AI 来加速' }],
    ['meta', { property: 'og:description', content: '为 AI 编程助手优化的前端设计库。25 个组件 + 5 个完整页面，纯 HTML+CSS，零依赖。' }],
    ['meta', { property: 'og:url', content: 'http://101.37.166.208:11930' }],
    ['meta', { property: 'og:site_name', content: 'My Design Lib' }],
    ['meta', { property: 'og:locale', content: 'zh_CN' }],

    // Twitter Card
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:title', content: 'My Design Lib — 你的设计，AI 来加速' }],
    ['meta', { name: 'twitter:description', content: '为 AI 编程助手优化的前端设计库。25 个组件 + 5 个完整页面，纯 HTML+CSS，零依赖。' }],

    // Schema.org 结构化数据
    ['script', { type: 'application/ld+json' }, JSON.stringify({
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "My Design Lib",
      "description": "为 AI 编程助手优化的前端设计库，包含 25 个组件和 5 个完整页面",
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
    ['meta', { name: 'ai-description', content: '前端设计库：25个HTML+CSS组件，5个完整页面模板，Design Tokens。可直接复制使用。' }],

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
          text: '🚀 落地页',
          collapsed: true,
          items: [
            { text: 'NovaPay SaaS', link: '/pages/saas-landing' },
            { text: 'TechConf 科技大会', link: '/pages/conference-landing' },
            { text: 'NexusAI 智能平台', link: '/pages/ai-saas-landing' },
            { text: 'FlowDesk 极简产品', link: '/pages/product-minimal' }
          ]
        },
        {
          text: '💼 作品集',
          collapsed: true,
          items: [
            { text: '创意作品集', link: '/pages/portfolio' },
            { text: 'Studio Creative 设计机构', link: '/pages/agency-portfolio' },
            { text: 'VOID 创意工作室', link: '/pages/studio-creative' }
          ]
        },
        {
          text: '📊 仪表盘与数据',
          collapsed: true,
          items: [
            { text: 'Nexus 数据仪表盘', link: '/pages/dashboard-dark' }
          ]
        },
        {
          text: '🛒 电商与应用',
          collapsed: true,
          items: [
            { text: 'ShopFlow 结账页', link: '/pages/checkout' },
            { text: 'AuthKit 现代认证页', link: '/pages/auth-modern' }
          ]
        },
        {
          text: '✨ 创意页面',
          collapsed: true,
          items: [
            { text: '太空主题 404', link: '/pages/404-creative' }
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
