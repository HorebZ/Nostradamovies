<script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import axios from 'axios';

  const msg = ref('NOT CHECK! (api down)');

  const getMessage = async () => {
    const path = "http://localhost:5001/api/v1/sanity";
    try {
      const res = await axios.get(path);
      msg.value = res.data;
    } catch (error) {
      console.error(error);
    }
  };

  onMounted(getMessage);
</script>


<template>
  <div class="h-96 items-center flex justify-center">
    <p class="uppercase text-2xl">{{ msg }}</p>
  </div>
</template>
