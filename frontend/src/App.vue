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

  @import url('https://fonts.googleapis.com/css2?family=Jost:wght@100;200;300;400&display=swap');

  html * {
    color: black;
    font-family: 'Jost', sans-serif;
  }

  #app {
      margin: 0;
      padding: 0;
  }

  body {
    margin: 0;
    padding: 0;
    height: 100vh;
  }

  body div, body div div {
    height: 100%;
  }

  header {
    height: 50px; 
    width: 100%; 
    background-color: #C8DDA4;
    display: flex;
    flex-wrap: nowrap;
    justify-content: space-between;
    

  }

  header #logo {
    width: fit-content;
  }

  header nav a {
    padding-right: 10px;
    padding-left: 10px; 
    height: 100%;
  }

  form {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    height: 100%;
  }

  footer{
    height: fit-content;
    width: 100%;
    background-color: #C8DDA4;
    bottom: 0;
  }

  footer ul li {
    display: block;
    padding-top: 2px;
    padding-bottom: 2px;
  }

  footer ul li a {
    text-decoration: none;
  }

  footer ul li :hover {
    font-weight: bold;
  }
 
</style>
