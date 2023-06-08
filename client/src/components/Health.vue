<template>
  <div class="h-full items-center flex justify-center">
    <p class="uppercase text-l">{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Health',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = "http://localhost:5001/api/v1/sanity";

      axios.get(path).then((res) => {this.msg = res.data;}).catch((error) => {console.error(error);});
    },
  },
  created() {
    this.getMessage();
  },
};
</script>