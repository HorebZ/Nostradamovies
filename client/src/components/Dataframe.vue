<script lang="ts">
import axios from "axios";
import Poster from "@/components/Poster.vue";


export default {
  data() {
    return {
      images: [],
    };
  },
  components: {
    Poster
  },
  mounted() {
    this.getImages();
  },
  methods: {
    getImages() {
      const apiUrl = 'http://localhost:5001/api/v1/images';

      axios.get(apiUrl).then(response => {
        if (response.data.length > 0) {
          this.images = response.data.slice(0, 50).map((image, rank) => ({
            src: image,
            alt: `Top ${rank + 1}`
          }));
        }
      }).catch(error => {
        console.error(error);
      })
    }
  },
};
</script>

<template>
  <div class="flex-row mt-20 px-72">
    <div class="flex flex-col w-full justify-center lg:items-start overflow-y-hidden">
      <h1 class="my-2 text-5xl text-white opacity-75 font-bold leading-tight text-center md:text-left">
        Imdb top movies
        <span class="bg-clip-text text-5xl font-bold text-transparent bg-gradient-to-r from-green-400 via-pink-500 to-purple-500">prediction</span>
      </h1>
      <p class="uppercase leading-normal text-base text-xl mb-8 text-center md:text-left w-1/2">
        We use the top 100 films from Imdb to train our models. See the results of your favorite films.
      </p>
    </div>
  </div>

  <video src="src/assets/mp4/trigger.mp4" preload="auto" autoplay loop class="my-2"></video>

  <div class="px-72">
    <div class="grid gap-8 grid-cols-4">
      <div v-for="(image, index) in images" :key="index" class="w-full h-full flex flex-col justify-between">
        <Poster :src="image.src" :alt="image.alt"/>
      </div>
    </div>
  </div>
</template>
