<script setup>
import Article from './Article.vue'
import json from "../../../database.json"
import update from "../App.vue"
import { ref, onMounted } from 'vue'


const props = defineProps({
  category: {
    type: String,
    required: true
  },
  key: {
    type: Number,
    required: true
  }
})

var articles = ref(updateArticles());

onMounted(() => {
  updateArticles()
})

function getFirstFiveElements(obj) {
    // Get the keys of the object
    const keys = Object.keys(obj);    
    // Take the first 5 keys and map them to their corresponding values
    const result = keys.slice(0, 10).map(key => obj[key]);
    return result;
}

const emit = defineEmits(['changeSummary'])

function updateArticles() {
  articles = json[props.category]
  articles = getFirstFiveElements(articles)
  console.log(articles)
  return articles
}

function prop(item) {
  update(item)
}

</script>

<template>
  <div v-for="item in articles">
    <Article @click="$emit('changeSummary', item)" :title="item.title" :date_updated="item.published" />
  </div>
</template>
