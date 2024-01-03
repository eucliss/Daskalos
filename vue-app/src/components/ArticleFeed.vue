<script setup>
import Article from './Article.vue'
import json from "../../../database.json"
import update from "../App.vue"
import { ref, onMounted } from 'vue'
import axios from 'axios'

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

var loaded = false
const componentKey = ref(0)
const forceRerender = async () => {
  componentKey.value += 1;
  await updateArticles()
};



// const data = await fetch(`http://localhost:5000/cs.AI`).then((r) => console.log(r))
// console.log(data)

// var articles = ref([])
// function updateArticles() {
//   var self = this
//   var res;
//   fetch(`http://localhost:5000/cs.AI`)
//   .then((r) => r.json()
//   .then((dataObject) =>
//     this.res = dataObject.data,
//   ))
//   console.log("------------------")
//   console.log(res)
//   return res
// }
// var articles = ref(updateArticles());
// articles = tis.updateArticles()



const articles = ref([])
// articles = await updateArticles()
// articles.value = await fetch(`http://localhost:5000/cs.AI`).then((r) => r.json())
forceRerender()
// console.log(articles.value.data)

// onMounted(() => {
  // axios.defaults.headers.get['Content-Type'] ='application/json;charset=utf-8';
  // axios.defaults.headers.get['Access-Control-Allow-Origin'] = '*';
  // updateArticles()
  
// })

async function getArticles(category) {
  const url = 'http://localhost:5000/' + category
  const response = await axios.get(url)
  return response.data
}

function getFirstFiveElements(obj) {
    // Get the keys of the object
    const keys = Object.keys(obj);    
    // Take the first 5 keys and map them to their corresponding values
    const result = keys.slice(0, 10).map(key => obj[key]);
    return result;
}

const emit = defineEmits(['changeSummary'])

async function updateArticles() {
  var url = 'http://localhost:5000/' + props.category
  articles.value = await fetch(url).then((r) => r.json())
  var new_articles = Array()
  for (var i = 0; i < articles.value.data.length; i++) {
    new_articles.push(JSON.parse(articles.value.data[i]))
  }
  articles.value = new_articles
  // return articles
}

function prop(item) {
  update(item)
}
</script>

<template>
  <div v-for="item in articles">
    <Article :key="componentKey" @click="$emit('changeSummary', item)" :title="item.title" :date_updated="item.published" />
  </div>
</template>
