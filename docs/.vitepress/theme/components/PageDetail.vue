<template>
  <div class="page-detail">
    <div class="detail-header">
      <a href="/pages/" class="back-link">← 返回画廊</a>
      <div class="detail-meta">
        <h1>{{ frontmatter.title }}</h1>
        <div class="detail-tags">
          <span v-for="tag in pageData.tags" :key="tag" class="tag">{{ tag }}</span>
          <span class="score">⭐ {{ pageData.rating }}</span>
        </div>
      </div>
      <div class="detail-actions">
        <button class="action-btn" :class="{ active: show === 'preview' }" @click="show = 'preview'">👁 预览</button>
        <button class="action-btn" :class="{ active: show === 'code' }" @click="loadCode(); show = 'code'">📝 源码</button>
        <a :href="pageData.openUrl" target="_blank" class="action-btn">↗ 新窗口打开</a>
      </div>
    </div>

    <div class="detail-body">
      <div v-show="show === 'preview'" class="panel">
        <iframe :src="pageData.iframeSrc" sandbox="allow-scripts" loading="lazy"></iframe>
      </div>
      <div v-show="show === 'code'" class="panel">
        <button class="copy-btn" @click="copyCode">📋 复制源码</button>
        <pre><code>{{ codeContent }}</code></pre>
      </div>
    </div>

    <div class="design-tips">
      <h2>💡 设计分析</h2>
      <div class="tips-grid">
        <div v-for="tip in pageData.tips" :key="tip.title" class="tip">
          <h3>{{ tip.title }}</h3>
          <p v-html="tip.content"></p>
        </div>
      </div>
    </div>

    <div class="detail-footer">
      <a href="/pages/" class="back-btn">← 返回画廊</a>
      <div class="nav-prevnext">
        <a v-if="pageData.prev" :href="pageData.prev.link">← {{ pageData.prev.text }}</a>
        <a v-if="pageData.next" :href="pageData.next.link">{{ pageData.next.text }} →</a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useData } from 'vitepress'

const { frontmatter } = useData()
const pageData = frontmatter.value.pageDetail || {}

const show = ref('preview')
const codeContent = ref('加载中...')

async function loadCode() {
  if (codeContent.value !== '加载中...') return
  try {
    const res = await fetch(pageData.iframeSrc)
    codeContent.value = await res.text()
  } catch (e) {
    codeContent.value = '加载源码失败: ' + e.message
  }
}

function copyCode() {
  navigator.clipboard.writeText(codeContent.value)
}
</script>

<style scoped>
.page-detail { max-width: 1200px; margin: 0 auto; padding: 0 2rem 2rem; color: #1e293b; }
.detail-header { padding: 1rem 0; }
.back-link { color: #6366f1; text-decoration: none; font-size: .9rem; display: inline-block; margin-bottom: 1rem; }
.back-link:hover { text-decoration: underline; }
.detail-meta h1 { font-size: 1.8rem; font-weight: 800; margin-bottom: .5rem; }
.detail-tags { display: flex; gap: .5rem; align-items: center; flex-wrap: wrap; }
.tag { padding: .3rem .8rem; background: #f1f5f9; border-radius: 8px; font-size: .8rem; color: #64748b; }
.score { font-size: .9rem; font-weight: 700; margin-left: .5rem; }
.detail-actions { display: flex; gap: .5rem; margin-top: 1rem; flex-wrap: wrap; }
.action-btn { padding: .5rem 1.2rem; border: 1px solid #e2e8f0; border-radius: 8px; background: #fff; cursor: pointer; font-size: .85rem; color: #64748b; text-decoration: none; transition: all .2s; }
.action-btn:hover, .action-btn.active { border-color: #6366f1; color: #6366f1; background: #eef2ff; }
.detail-body { margin: 1.5rem 0; border: 1px solid #e2e8f0; border-radius: 12px; overflow: hidden; background: #fff; }
.panel iframe { width: 100%; height: 70vh; border: none; }
.panel pre { padding: 1.5rem; overflow: auto; max-height: 70vh; background: #1e1e2e; color: #cdd6f4; font-size: .85rem; line-height: 1.6; margin: 0; }
.panel code { font-family: monospace; white-space: pre; }
.copy-btn { position: sticky; top: 0; float: right; padding: .4rem .8rem; border: 1px solid #444; border-radius: 6px; background: #2a2a3a; color: #cdd6f4; cursor: pointer; font-size: .8rem; z-index: 10; }
.copy-btn:hover { background: #6366f1; color: #fff; }
.design-tips { margin: 2rem 0; }
.design-tips h2 { font-size: 1.3rem; font-weight: 700; margin-bottom: 1rem; }
.tips-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; }
.tip { padding: 1.2rem; border: 1px solid #e2e8f0; border-radius: 12px; background: #fff; }
.tip h3 { font-size: .95rem; font-weight: 700; margin-bottom: .5rem; color: #6366f1; }
.tip p { font-size: .85rem; color: #64748b; line-height: 1.6; }
.detail-footer { display: flex; justify-content: space-between; align-items: center; padding: 2rem 0; margin-top: 2rem; border-top: 1px solid #e2e8f0; }
.back-btn { color: #6366f1; text-decoration: none; font-weight: 600; }
.nav-prevnext { display: flex; gap: 2rem; }
.nav-prevnext a { color: #64748b; text-decoration: none; font-size: .9rem; }
.nav-prevnext a:hover { color: #6366f1; }
</style>
