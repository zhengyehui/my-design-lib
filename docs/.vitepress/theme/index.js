import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      // 在每篇文章底部插入赞助区
      'doc-after': () => h('div', { class: 'sponsors-section' }, [
        h('div', { class: 'sponsor-card' }, [
          h('div', { class: 'sponsor-card__icon sponsor-card__icon--placeholder' }, '✦'),
          h('div', { class: 'sponsor-card__body' }, [
            h('div', { class: 'sponsor-card__label' }, '组件赞助'),
            h('div', { class: 'sponsor-card__name' }, '成为此组件的赞助商'),
            h('div', { class: 'sponsor-card__desc' }, '你的品牌将展示在此处，被所有使用此组件的开发者和 AI 看到'),
          ]),
          h('a', { class: 'sponsor-card__link', href: 'mailto:hello@design-lib.dev' }, '合作洽谈 →'),
        ]),
      ]),
    })
  }
}
