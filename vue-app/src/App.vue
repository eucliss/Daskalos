<script setup>
import Summary from './components/Summary.vue'
import ArticleFeed from './components/ArticleFeed.vue'
import FilterBar from './components/FilterBar.vue';
import { ref } from 'vue';
import json from "../../objects/tag_map.json"
import word_map from "../../objects/word_to_tag_map.json"
import book from "./assets/book.svg"
import HeaderBar from './components/HeaderBar.vue'


var title = "no title"
var author = "no author"
var category = "no category"
var summary = "no summary"
var html_link = "no link"
var loaded = false
var category = ref("cs.AI")
var local_category = ref("cs.AI")

var componentKey = ref(0)
var componentKey2 = ref(0)


const forceRerender2 = () => {
  componentKey2.value += 1;
};

const forceRerender = () => {
  componentKey.value += 1;
};

function updateCategory(new_category){
  console.log("clicked category!")
  console.log(new_category)
  this.category = word_map[new_category]
  console.log(this.category)
  forceRerender2()
}

function update(item) {
  console.log("clicked!")
  title = item.title;
  summary = item.summary;
  html_link = item.html_link;
  author = item.authors;
  local_category = item.primary_category["@term"];
  local_category = json[category];
  loaded = true;
  forceRerender()
}

</script>

<template>
  <HeaderBar/>
    <main >
      <img src = "./assets/Network.svg"/>
      <FilterBar @changeCategory="
            (category) => {
              updateCategory(category)
            }"
          />
      <div class="row">
        <div class="column">
        <ArticleFeed :key="componentKey2" :category="category" @changeSummary="
            (item) => {
              update(item)
            }
          "/>
        </div>
        <div class="column">
          <Summary v-show="loaded" :key="componentKey" :title="title" :author="author" :category="local_category" :summary="summary" :html_link="html_link"/>
          <h2 v-show="!loaded">Select an article to read the summary!</h2>
        </div>
      </div>
    </main>
</template>

<style scoped>

* {
  border-radius: 8px;
}

h2 {
  padding-top: 20%;
  text-align: center;
  font-size: 1.6rem;
  font-weight: 500;
}

.sidebar {
  height: 100%;
  width: 10%;
  background-color: #8B8885;
  float: left;
  width: 10%;
  height: 100vh;
}

img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 5%;
  height: 5%;
  padding-top: 2%;
  padding-bottom: 2%;
}

main {
  display: auto;
  line-height: 1.5;
  padding-left: 10%;
  padding-right: 10%;
  height: 100%;
  background-color: #FFF4E2;
  border: 2px solid #8B8885;
}

.row {
  box-sizing: border-box;
  display: table;
  clear: both;
  height: 100vh;
  width: 100%;
  border-radius: 6px;
}

/* Create two equal columns that floats next to each other */
.column {
  float: left;
  width: 48%;
  padding: 10px;
  margin: 1%;
  box-sizing: border-box;
  background-color: #FFF4E2;
  height: 100vh;
  overflow:auto;
  border: 2px solid #8B8885;
  border-radius: 6px;
}
</style>
