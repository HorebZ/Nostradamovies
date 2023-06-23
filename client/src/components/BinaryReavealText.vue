<script setup lang="ts">
  import { defineProps, ref, onMounted, onUnmounted } from "vue";


  const props = defineProps({
    text: { type: String, required: true },
  });

  let finalText = ref(props.text)

  onMounted(() => {
    applyEffect()
  })

  function applyEffect() {
    const alphabets = '01'
    let i = 0

    const interval = setInterval(() => {
      finalText.value = finalText.value
        .split("")
        .map((c, idx) => {
          if (idx < i) return props.text[idx]
          if (c === ' ') return ' '
          return alphabets[Math.floor(Math.random() * alphabets.length)]
        })
        .join("")

      if (i>=props.text.length) {
        clearInterval(interval)
      }
      i += 1/4
    }, 1)
  }
</script>

<template>
  <span>{{ finalText }}</span>
</template>