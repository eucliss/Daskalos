<script setup>
defineProps({
  text: {
    type: String,
    required: true
  },
  link_to_open: {
    type: String,
    required: true
  }
})

// var link = {{ link_to_open }}

function openLinkInNewTab(link) {
    // Open the link in a new tab
    window.open(link);
}

</script>

<template>
    <div>
      <button @click="openLinkInNewTab(link_to_open)">Read Now</button>
    </div>
</template>
  
  
<style scoped>

button {
  background-color: #4CAF50; /* Green */
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  padding: 10px 25px;
  text-align: center;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
/* Add your component styles here */
</style>
  