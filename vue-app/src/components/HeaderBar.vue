<script setup>
console.log("hello")
</script>

<template>
    <div class="row">
        <div class="column"></div>
        <div class="column-center">
            <h1>Nexus Times Beta</h1>
        </div>
        <div class="column">
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

.row {
  box-sizing: border-box;
  display: table;
  clear: both;
  width: 100%;
}

/* Create two equal columns that floats next to each other */
.column {
  float: left;
  width: 23%;
  padding: 10px;
  margin: 1%;
  box-sizing: border-box;
}


.column-center {
  float: left;
  width: 48%;
  padding: 10px;
  margin: 1%;
  box-sizing: border-box;
}
</style>
