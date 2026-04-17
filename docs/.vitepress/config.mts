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
          text: '基础组件',
          items: [
            { text: 'Button 按钮', link: '/components/button' },
            { text: 'Badge 徽章', link: '/components/badge' },
            { text: 'Avatar 头像', link: '/components/avatar' },
            { text: 'Toggle 开关', link: '/components/toggle' }
          ]
        },
        {
          text: '表单组件',
          items: [
            { text: 'Input 输入框', link: '/components/input' },
            { text: 'Dropdown 下拉菜单', link: '/components/dropdown' }
          ]
        },
        {
          text: '布局组件',
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
          text: '反馈组件',
          items: [
            { text: 'Modal 对话框', link: '/components/modal' },
            { text: 'Alert 提示', link: '/components/alert' },
            { text: 'Toast 通知', link: '/components/toast' },
            { text: 'Tooltip 工具提示', link: '/components/tooltip' },
            { text: 'Progress 进度条', link: '/components/progress' }
          ]
        },
        {
          text: '✨ 炫酷组件',
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
          text: '设计变量',
          items: [
            { text: 'Colors 颜色', link: '/tokens/colors' },
            { text: 'Typography 字体', link: '/tokens/typography' },
            { text: 'Spacing 间距', link: '/tokens/spacing' }
          ]
        }
      ],
      '/patterns/': [
        {
          text: '布局模式',
          items: [
            { text: 'Landing Page 落地页', link: '/patterns/landing' },
            { text: 'Dashboard 仪表盘', link: '/patterns/dashboard' }
          ]
        }
      ],
      '/pages/': [
        {
          text: '🎨 页面画廊',
          items: [
            { text: '全部页面', link: '/pages/' },
            { text: 'SaaS 落地页', link: '/pages/saas-landing' },
            { text: '创意作品集', link: '/pages/portfolio' },
            { text: '数据仪表盘', link: '/pages/dashboard-dark' },
            { text: '电商结账页', link: '/pages/checkout' },
            { text: '404 创意页', link: '/pages/404-creative' }
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
