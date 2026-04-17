<script setup>
import { computed } from 'vue'
const props = defineProps({
  html: { type: String, default: '' }
})
</script>
<template>
  <div v-html="html"></div>
</template>
