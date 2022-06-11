<template>
  <div>
    <LaptopLibrary />
  </div>
</template>

<script>
import LaptopLibrary from "./components/LaptopLibrary.vue";

export default {
  name: "App",
  components: {
    LaptopLibrary,
  },
};
</script>

<style>
@import "~/src/assets/main.css";
</style>
