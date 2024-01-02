<script setup>
import json from "../../../tag_map.json"

const emit = defineEmits(['changeCategory'])

var categories = json

function getFirstFiveElements(obj) {
    // Get the keys of the object
    const keys = Object.keys(obj);    
    // Take the first 5 keys and map them to their corresponding values
    const result = keys.slice(0, 7).map(key => obj[key]);
    return result;
}
categories = getFirstFiveElements(categories)
</script>

<template>
<div class="topnav" >
    <span @click="$emit('changeCategory', category)" v-for="category in categories" > {{category}} </span>
</div>

<!-- <div style="padding-left:16px">
</div> -->
</template>

<style scoped>
.topnav {
    margin-bottom: 1%;
    overflow: hidden;
    background-color: #202020;
    display: table;
    width: 100%;
    height: 50px;
}

.topnav span {
    color: #f2f2f2;
    text-align: center;
    font-size: 17px;
    display: table-cell;
    vertical-align: middle;
}

.topnav span:hover {
    background-color: #FFF4E2;
    border: #202020;
    color: black;
}

.topnav span.active {
    background-color: #FFF4E2;
    color: white;
}

</style>

