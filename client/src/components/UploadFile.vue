<script setup lang="ts">
  import { ref } from "vue";
  import axios from 'axios';


  const apiUrl = 'http://localhost:5001/api/v1/process'
  const response = ref(null)

  const onFileChange = async (ev: Event) => {
    const file = (ev.target as HTMLInputElement).files?.[0];

    if (file) {
      // Use FormData to build a form data object
      const formData = new FormData();
      formData.append('file', file);

      try {
        // Replace '/upload' with the actual URL of your Flask endpoint
        const res = await axios.post(apiUrl, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          },
        });

        console.log(res.data);

        response.value = res.data;
        response.image = res.data.file;
      } catch (error) {
        console.error(error);
      }
    }
  };
</script>

<template>
  <div class="flex-col w-full h-auto">
    <div class="opacity-75 w-full shadow-lg p-8">
      <div class="flex items-center justify-center w-full">
        <!-- UPLOAD FILE -->
        <div class="flex flex-col items-center justify-center pt-5 pb-6">
          <label
              for="dropzone-file"
              class="flex flex-col items-center justify-center w-full h-32 border-2 border-dashed rounded-lg cursor-pointer border-white hover:border-gray-300 hover:bg-gray-800"
          >
            <svg
                class="w-8 h-8 text-gray-400 animate-bounce"
                stroke="currentColor"
                viewBox="0 0 24 24"
            >
              <path
                  stroke-width="1"
                  d="M18.125,15.804l-4.038-4.037c0.675-1.079,1.012-2.308,1.01-3.534C15.089,4.62,12.199,1.75,8.584,1.75C4.815,1.75,1.982,4.726,2,8.286c0.021,3.577,2.908,6.549,6.578,6.549c1.241,0,2.417-0.347,3.44-0.985l4.032,4.026c0.167,0.166,0.43,0.166,0.596,0l1.479-1.478C18.292,16.234,18.292,15.968,18.125,15.804 M8.578,13.99c-3.198,0-5.716-2.593-5.733-5.71c-0.017-3.084,2.438-5.686,5.74-5.686c3.197,0,5.625,2.493,5.64,5.624C14.242,11.548,11.621,13.99,8.578,13.99 M16.349,16.981l-3.637-3.635c0.131-0.11,0.721-0.695,0.876-0.884l3.642,3.639L16.349,16.981z"
              />
            </svg>

            <span class="m-2 text-sm text-gray-500 dark:text-gray-400">
              <span class="font-semibold">Click to predict movies poster</span>
            </span>

            <p class="text-xs text-gray-500 dark:text-gray-400">PNG or JPG</p>
          </label>

          <input id="dropzone-file" type="file" class="hidden" @change="onFileChange"/>
        </div>
      </div>
    </div>

    <div v-if="response" class="flex">
      <img :src="'data:image/png;base64,' + response.file" alt="Processed image" class="w-1/2"/>
      <div class="w-1/2 p-5">
        <h2>{{ response.name }}</h2>
        <ul>
          <li v-for="kpi in response.kpis" :key="kpi.code">
            {{ kpi.code }}: {{ kpi.value.join(', ') }}
          </li>
        </ul>
      </div>
    </div>
  </div>

</template>