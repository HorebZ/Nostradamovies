<script setup lang="ts">
import {RouterLink, RouterView} from 'vue-router'
import UploadFile from "@/components/UploadFile.vue";
</script>

<template>
  <!--Nav-->
  <header class="px-14 text-s fixed w-full z-40 py-5 left-0 top-0">
    <div class="container flex justify-between text-s relative w-full">
      <a class="flex items-center no-underline hover:no-underline font-bold text-s" href="#">
        Lethal Data/<span class="bg-clip-text text-transparent bg-gradient-to-r from-green-400 via-pink-500 to-purple-500">Nostradamovies</span>
      </a>
      <ul class="uppercase flex translate-y-0 m-0">
        <li class="mx-5" style="opacity: 1;">
          <RouterLink class="ro text-xs" to="/">&lt;/N&gt; Home</RouterLink>
        </li>
        <li class="mx-5" style="opacity: 1;">
          <RouterLink class="ro text-xs" to="/dataframe">&lt;/N&gt; Dataframe</RouterLink>
        </li>
        <li class="mx-5" style="opacity: 1;">
          <RouterLink class="ro text-xs" to="/health">&lt;/N&gt; Health</RouterLink>
        </li>
      </ul>
    </div>
    <div class="header-blur"></div>
  </header>

  <div class="mt-36">
    <RouterView class=""/>
  </div>

  <!--Footer-->
  <div class="px-14 py-6 text-sm text-center md:text-left fade-in">
      <a class="text-gray-500 no-underline hover:no-underline" href="#">&copy; Lethal Corp 2023 </a>
      - Lethal Data/Nostradamovies
  </div>

</template>

<style scoped >

.header-blur {
  @apply z-[-1] h-[150%] absolute w-full left-0 top-0;
  background: linear-gradient(
    180deg,
    rgba(0, 0, 0, 1) 0%,
    rgba(0, 0, 0, 0) 100%
  );
}

.ro {
  @apply relative before:content-[''] before:absolute before:h-px before:bg-white before:origin-bottom-right before:transition-transform before:duration-[0.5s] before:ease-[ease] before:scale-x-0 before:bottom-0 before:inset-x-1 hover:before:origin-bottom-left hover:before:scale-x-100;
}

</style>