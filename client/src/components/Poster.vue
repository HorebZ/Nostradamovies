<template>
  <div
      @mouseenter="onMouseEnter"
      @mouseleave="onMouseLeave"
      :style="{ backgroundImage: 'url(' + src + ')', backgroundPosition: isHovered ? 'left center ' : 'center center', backgroundSize: isHovered ? '400px ' : '300px'}"
      class="group poster h-[350px] w-[250px] transition-[background] duration-[0.8s] overflow-hidden shadow-[0_70px_63px_-60px_#000] flex justify-center items-center relative rounded-[10px]"
  >
    <div class="group-hover:bg-black h-full w-full absolute opacity-50" />
    <div class="h-[340px] w-[240px] transition-[border] duration-[1s] relative rounded-[10px] bg-transparent border border-transparent hover:border-solid hover:border-white">
      <h2>{{ alt }}</h2>
      <div class="icons">
        <i class="fa" aria-hidden="true">noir</i>
        <i class="fa" aria-hidden="true">blue</i>
        <i class="fa" aria-hidden="true">vert</i>
        <i class="fa" aria-hidden="true">rouge</i>
        <i class="fa" aria-hidden="true">gris</i>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  name: 'Poster',
  props: ['src', 'alt'],
  data() {
    return {
      isHovered: false,
      src: this.src,
      alt: this.alt,
    }
  },
  methods: {
    onMouseEnter() {
      this.isHovered = true;
    },
    onMouseLeave() {
      this.isHovered = false;
    }
  }
}
</script>

<style scoped>

.poster:hover h2, .poster:hover .fa {
  opacity: 1;
}

h2 {
  @apply text-white opacity-0 transition-opacity duration-[1s] m-5;
}
.fa {
  @apply opacity-0 transition-opacity duration-[1s];
}
.icons {
  @apply absolute fill-white text-white h-[130px] w-[50px] flex flex-col items-start justify-around bottom-[10px] left-[10px];
}

</style>