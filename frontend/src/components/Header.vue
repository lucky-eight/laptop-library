<template>
  <header>
    <div id="logo"><p>Laptop Library</p></div>
    <nav>
      <a id="home" href="#">Home</a>
      <a id="links" href="#">Get a Laptop</a>
      <a id="links" href="#">Donate Laptops</a>
      <a id="text" href="#"><img src="../assets/account.svg" /></a>
      <a id="text" href="#"><img src="../assets/help.svg" /></a>
    </nav>
  </header>
</template>

<script>
export default {
  name: "GlobalHeader",
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
header {
  height: 55px;
  width: 100%;
  background-color: #c8dda4;
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
}

header #logo {
  width: fit-content;
}

header nav {
  display: flex;
  align-items: center;
  justify-content: center;
}

header nav a {
  padding-right: 10px;
  padding-left: 10px;
  align-self: end;
}

a{
  color: black;
  /* padding-bottom: 15px; */
  text-decoration: none;
}

#home{
  text-decoration: underline;
}

#logo{
  font-size: 35px;
}

</style>
