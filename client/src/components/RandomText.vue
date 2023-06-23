<script setup lang="ts">
  import { defineProps, ref, onMounted, onUnmounted } from "vue";


  const props = defineProps({
    text: { type: String, required: true },
  });
  let finalText = ref(props.text)

  function applyEffect() {
    const alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    let i = 0

    const interval = setInterval(() => {
        finalText.value = finalText.value
          .split("")
          .map((c, idx) => {
              if (idx < i) return props.text[idx]
              return alphabets[Math.floor(Math.random() * alphabets.length)]
          })
          .join("")

      if (i>=props.text.length) {
        clearInterval(interval)
      }
      i += 1/4
    }, 15)
  }
</script>

<template>
  <span class="relative">
    <span>{{ text }}</span>
    <span class="absolute -inset-0" @mouseover="applyEffect()">{{ finalText }}</span>
  </span>

</template>