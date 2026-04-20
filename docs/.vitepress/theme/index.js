import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import './navbar.css'
import './custom.css'
import SponsorCard from './SponsorCard.vue'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      // 在每篇文章底部插入赞助区
      'doc-after': () => h(SponsorCard),
    })
  }
}
