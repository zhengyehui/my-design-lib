import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import './custom.css'
import SponsorCard from './SponsorCard.vue'
import PageDetail from './components/PageDetail.vue'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      // 在每篇文章底部插入赞助区
      'doc-after': () => h(SponsorCard),
    })
  },
  enhanceApp({ app }) {
    // Register PageDetail globally so all .md files can use <PageDetail>
    app.component('PageDetail', PageDetail)
  }
}
