<script setup>
import Summary from './components/Summary.vue'
import ArticleFeed from './components/ArticleFeed.vue'
import FilterBar from './components/FilterBar.vue';
import { ref } from 'vue';
import json from "../../tag_map.json"
import word_map from "../../word_to_tag_map.json"


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
  <!-- <div class="header">
    <FilterBar/>
  </div> -->
  <main >
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
    </div>
    </div>
  </main>
</template>

<style scoped>
main {
  line-height: 1.5;
  padding-left: 10%;
  padding-right: 10%;
  padding-top: 4%;
  height: 100%;
  background-color: rgb(195, 195, 195);
}

/* Create two equal columns that floats next to each other */
.column {
  float: left;
  width: 48%;
  padding: 10px;
  margin: 1%;
  box-sizing: border-box;
  background-color: rgb(220, 220, 220);
  height: 100vh;
  overflow-y:auto;
}

.row {
  box-sizing: border-box;
  display: table;
  clear: both;
  height: 100vh;
  width: 100%;
}
</style>
