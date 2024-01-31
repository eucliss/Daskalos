<script setup>

import UploadButton from './UploadButton.vue'

function uploadDocument(){
  // Build out little modal to upload a document or something
  console.log("uploading!!")
}
</script>

<template>
    <div class="row">
        <div class="column">
        </div>
        <div class="column-center">
            <h1>Nexus Times Beta</h1>
        </div>
        <div class="column">
          <upload-button></upload-button>
          <button class="create-button"
            @upload="() => {
              uploadDocument()
            }"
          >Upload Article</button>
        </div>
    </div>
</template>

<style scoped>
h1 {
  margin: 0%;
  text-align: center;
  font-size: 3rem;
  font-weight: 500;
  color: #FFF4E2;
  background-color: #202020;
}

div {
    max-height: 75px;
}

.create-button {
  background-color: #FFF4E2;
  width: 30%;
  height: 75%;
  float: right;
  margin-top: 5px;
  border-radius: 10px;
  border-color: #8B8885;
}

.row {
  box-sizing: border-box;
  display: table;
  clear: both;
  width: 100%;
}

/* Create two equal columns that floats next to each other */
.column {
  float: left;
  width: 30%;
  height: 75px;
  padding: 10px;
  margin: 1%;
  box-sizing: border-box;
}


.column-center {
  float: left;
  width: 30%;
  padding: 10px;
  margin: 1%;
  box-sizing: border-box;
}
</style>
