<template>
  <div class="flex-row mt-20 px-72">

    <div class="flex flex-col w-full justify-center lg:items-start overflow-y-hidden">
      <h1 class="my-2 text-5xl text-white opacity-75 font-bold leading-tight text-center md:text-left">
        Movie genre
        <span class="bg-clip-text text-5xl font-bold text-transparent bg-gradient-to-r from-green-400 via-pink-500 to-purple-500">prediction</span>
      </h1>

      <p class="uppercase leading-normal text-base text-xl mb-8 text-center md:text-left w-1/2">
        With I.A & statFrom uploading movies poster get informations in second
      </p>
    </div>
  </div>

  <video src="src/assets/mp4/header-animation.mp4" preload="auto" autoplay="" loop="" playsinline="" webkit-playsinline="" x5-playsinline="" class="my-2"></video>

  <UploadFile class="w-1/3"/>

</template>

<script setup lang="ts">
</script>