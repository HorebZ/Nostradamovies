<template>
    <!--Top Col-->
  <div class="flex-row mt-20 px-72">

    <div class="flex flex-col w-full justify-center lg:items-start overflow-y-hidden">
      <h1 class="my-2 text-5xl text-white opacity-75 font-bold leading-tight text-center md:text-left">
        Movie genre
        <span class="bg-clip-text text-5xl font-bold text-transparent bg-gradient-to-r from-green-400 via-pink-500 to-purple-500">prediction</span>
      </h1>
      <p class="uppercase leading-normal text-base text-xl mb-8 text-center md:text-left w-1/2">
        With I.A & statFrom uploading movies poster get informations in second
      </p>


<!--      <UploadFile class="w-1/3"/>-->
    </div>
  </div>
  <video src="src/assets/mp4/header-animation.mp4" preload="auto" autoplay="" loop="" playsinline="" webkit-playsinline="" x5-playsinline="" class="my-2"></video>

  <div class="h-full px-72">
        <!--Main-->
        <div class="container pt-24 md:pt-36 mx-auto flex flex-wrap flex-col md:flex-row items-center">
            <!--Right Col-->
            <div class="xl:w-3/5 p-12">

                <div id="controls-carousel" class="relative" data-carousel="static">
                    <!-- Carousel wrapper -->
                    <div class="relative h-96 rounded-lg md:h-96">
                        <!-- Item 1 -->
                        <div class="hiden duration-700 ease-in-out" data-carousel-item>
                            <img src='../assets/img/default.jpg'
                                class="shadow-lg shadow-indigo-500/50 h-96 mx-auto transform -rotate-6 transition hover:scale-105 duration-700 ease-in-out hover:rotate-6"
                                alt="..." />
                        </div>
                        <!-- Item 2 -->
                        <div class="hidden duration-700 ease-in-out" data-carousel-item="active">
                            <img src='../assets/img/default.jpg'
                                class="shadow-lg shadow-indigo-500/50 h-96 mx-auto transform -rotate-6 transition hover:scale-105 duration-700 ease-in-out hover:rotate-6"
                                alt="..." />
                        </div>
                        <!-- Item 3 -->
                        <div class="hidden duration-700 ease-in-out" data-carousel-item>
                            <img src='../assets/img/default.jpg'
                                class="shadow-lg shadow-indigo-500/50 h-96 mx-auto transform -rotate-6 transition hover:scale-105 duration-700 ease-in-out hover:rotate-6"
                                alt="..." />
                        </div>
                        <!-- Item 4 -->
                        <div class="hidden duration-700 ease-in-out" data-carousel-item>
                            <img src='../assets/img/default.jpg'
                                class="shadow-lg shadow-indigo-500/50 h-96 mx-auto transform -rotate-6 transition hover:scale-105 duration-700 ease-in-out hover:rotate-6"
                                alt="..." />
                        </div>
                        <!-- Item 5 -->
                        <div class="hidden duration-700 ease-in-out" data-carousel-item>
                            <img src='../assets/img/default.jpg'
                                class="shadow-lg shadow-indigo-500/50 h-96 mx-auto transform -rotate-6 transition hover:scale-105 duration-700 ease-in-out hover:rotate-6"
                                alt="..." />
                        </div>
                    </div>
                    <!-- Slider controls -->
                    <button type="button"
                        class="absolute top-0 left-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none"
                        data-carousel-prev>
                        <span
                            class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 group-hover:bg-white/50 group-focus:ring-4 group-focus:ring-white group-focus:outline-none">
                            <svg aria-hidden="true" class="w-6 h-6 text-white" fill="none" stroke="currentColor"
                                viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M15 19l-7-7 7-7">
                                </path>
                            </svg>
                            <span class="sr-only">Previous</span>
                        </span>
                    </button>
                    <button type="button"
                        class="absolute top-0 right-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none"
                        data-carousel-next>
                        <span
                            class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 group-hover:bg-white/50 group-focus:ring-4 group-focus:ring-white group-focus:outline-none">
                            <svg aria-hidden="true" class="w-6 h-6 text-white" fill="none" stroke="currentColor"
                                viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7">
                                </path>
                            </svg>
                            <span class="sr-only">Next</span>
                        </span>
                    </button>
                </div>
            </div>

        </div>
    </div>

</template>
<script setup lang="ts">
</script>