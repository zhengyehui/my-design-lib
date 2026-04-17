<template>
  <div class="sponsors-section" v-if="sponsor">
    <div class="sponsor-card" :class="{ 'sponsor-card--active': sponsor.active }">
      <div class="sponsor-card__icon" :class="sponsor.active ? '' : 'sponsor-card__icon--placeholder'">
        {{ sponsor.logo || '✦' }}
      </div>
      <div class="sponsor-card__body">
        <div class="sponsor-card__label">组件赞助</div>
        <div class="sponsor-card__name">{{ sponsor.name }}</div>
        <div class="sponsor-card__desc">{{ sponsor.description }}</div>
      </div>
      <a class="sponsor-card__link" :href="sponsor.url" target="_blank" rel="noopener">
        {{ sponsor.active ? '访问官网 →' : '合作洽谈 →' }}
      </a>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return { sponsor: null }
  },
  async mounted() {
    try {
      const resp = await fetch('/sponsors.json')
      const data = await resp.json()
      const activeKey = data.featured?.[0] || null
      if (activeKey && data.sponsors[activeKey]?.active) {
        this.sponsor = data.sponsors[activeKey]
      } else {
        // 显示默认占位
        this.sponsor = data.sponsors.default || {
          name: '成为赞助商',
          description: '你的品牌将展示在此处，被所有使用此组件的开发者和 AI 看到',
          logo: '✦',
          url: 'mailto:weta_zheng@qq.com',
          active: false
        }
      }
    } catch {
      this.sponsor = {
        name: '成为赞助商',
        description: '你的品牌将展示在此处',
        logo: '✦',
        url: 'mailto:weta_zheng@qq.com',
        active: false
      }
    }
  }
}
</script>
