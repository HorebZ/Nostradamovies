<script setup lang="ts">
  import { ref } from "vue";

  const props = defineProps({
    src: { type: String, required: true },
    kpis: { type: Array, required: true },
  });

  const isHovered = ref<boolean>(false);

  const onMouseEnter = () => {
    isHovered.value = true;
  };

  const onMouseLeave = () => {
    isHovered.value = false;
  };
</script>

<template>
  <div
      @mouseenter="onMouseEnter"
      @mouseleave="onMouseLeave"
      :style="{ backgroundImage: 'url(' + src + ')', backgroundPosition: isHovered ? 'left center ' : 'center center', backgroundSize: isHovered ? '500px ' : '400px'}"
      class="group poster h-[450px] w-[350px] transition-[background] duration-[0.8s] overflow-hidden flex justify-center items-center relative rounded-[10px]"
  >
    <div class="group-hover:bg-black h-full w-full absolute opacity-50" />
    <div class="h-[440px] w-[340px] transition-[border] duration-[1s] relative rounded-[10px] bg-transparent border border-transparent hover:border-solid hover:border-white">
      <div class="absolute fill-white text-white h-[130px] w-[50px] flex flex-col items-start justify-around bottom-[10px] left-[10px]">
        <i
            class="group-hover:opacity-100 whitespace-nowrap text-xs opacity-0 transition-opacity duration-[1s]"
            aria-hidden="true"
            v-for="kpi in kpis"
            :key="kpi.code"
        >
          {{ kpi.code }}: {{ kpi.value.join(', ') }}
        </i>
      </div>
    </div>
  </div>
</template>