<script lang="ts" >
import axios from "axios";

import Card from "@/components/Card.vue";

export default {
  data() {
    return {
      images: [],
    };
  },
  components: {
    Card,
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

  <Card/>

  <div class="px-72">
    <div class="grid gap-8 grid-cols-4">
      <div v-for="(image, index) in images" :key="index" class="w-full h-full flex flex-col justify-between">
        <img :src="image.src" :alt="image.alt" class="sw-full h-auto"/>
        <div class="dd mt-3 p-1 h-10 w-full flex-col uppercase">
          <p class="text-white text-xs">{{ image.alt }}</p>
        </div>
      </div>
    </div>
  </div>


<!--  <div class="px-72">-->
<!--    <div class="grid gap-8 grid-cols-4">-->
<!--      <div v-for="(image, index) in images" :key="index" class="w-full h-full flex flex-col justify-between">-->
<!--        <img :src="image.src" :alt="image.alt" class="sw-full h-auto"/>-->
<!--        <div class="dd mt-3 p-1 h-10 w-full flex-col uppercase">-->
<!--          <p class="text-white text-xs">{{ image.alt }}</p>-->
<!--        </div>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->
</template>

<style scoped >
.dd {
  @apply relative before:origin-[center_right] before:top-0 hover:before:origin-[center_left] hover:before:scale-x-100 after:origin-[center_left] after:bottom-0 hover:after:origin-[center_right] hover:after:scale-x-100;
}
.dd::before,
.dd::after {
  @apply content-[''] absolute h-px bg-white transition-transform duration-[0.5s] ease-[ease] scale-x-0 inset-x-0;
}

.bb {
  @apply z-[100] relative overflow-hidden text-[inherit] text-[white] cursor-pointer px-[1em] py-[0.5em] border-[none] after:content-[''] after:z-[-1] after:bg-[hsla(0,0%,100%,0.2)] after:absolute after:w-[1.25em] after:-inset-y-2/4 hover:after:transition-transform hover:after:duration-[0.45s] hover:after:ease-[ease-in-out];
  font-family: inherit;
  outline: none;
}
.bb::after {
  transform: translate3d(-525%, 0, 0) rotate(35deg);
}
.bb:hover::after {
  transform: translate3d(200%, 0, 0) rotate(35deg);
}
</style>
