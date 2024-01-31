<script setup>
import { ref } from 'vue';

const isModalOpen = ref(false);

function openModal() {
    isModalOpen.value = true;
}

function closeModal() {
    isModalOpen.value = false;
}

</script>

<template>
    <div>
        <!-- Button to open the modal -->
        <button @click="openModal" class="btn btn-primary">Open Modal</button>

        <!-- Modal component -->
        <div class="modal" v-if="isModalOpen">
        <div class="modal-dialog">
            <div class="modal-content">
            <!-- Modal header -->
                <div class="modal-header">
                    <button type="button" class="close" @click="closeModal"></button>
                    <h2 class="modal-title">Upload Article</h2>
                    <span>&times;</span>
                </div>

                <!-- Modal body -->
                <div class="modal-body">
                    <!-- Your modal content goes here -->
                    <p>This is the modal content.</p>
                </div>

                <!-- Modal footer -->
                <div class="modal-footer">
                    <button class="btn btn-secondary" @click="closeModal">Close</button>
                </div>
            </div>
        </div>
        </div>
    </div>
</template>
  
<style>
.modal-header {
}
.modal-title {
    color: #202020;
    text-align: center;
}

.modal-content {
    background-color: #FFF4E2;
    color: #FFF4E2;
    border: 2px solid #8B8885;
    box-shadow: #8B8885 0px 0px 10px;
    min-width: 100%;
}
/* Add your custom CSS styles here */
.modal-dialog {
    background-color: black;
    border-radius: 6px;
    max-width: 100%;
    margin: 7%;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    height: 80%;
    display: flex;
    position: fixed;
    z-index: 100000;
}
</style>