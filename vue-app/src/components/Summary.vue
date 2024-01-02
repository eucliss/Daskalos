<script setup>
import Button from './Button.vue'

defineProps({
  title: {
    type: String,
    required: true
  },
  author: {
    type: String,
    required: true
  },
  category: {
    type: String,
    required: true
  },
  summary: {
    type: String,
    required: true
  },
  html_link: {
    type: String,
    required: true
  }
})
</script>

<template>
  <div class="summary">
    <h1>{{ title }}</h1>
    <h4>{{ author }}</h4>
    <h4>{{ category }}</h4>
    <Button text="Read Now" :link_to_open="html_link"/>

    <h2>Summary</h2>
    <p>{{ summary }}</p>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.summary h1,
.summary h3,
.summary p,
.summary h4 {
  text-align: center;
}
</style>
