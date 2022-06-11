<template>
  <header>
    <div id="logo"><p>Laptop Library</p></div>
    <nav>
      <a href="#">Get a Laptop</a>
      <a href="#">Register Laptop</a>
      <a href="#"><img src="../assets/account.svg" /></a>
      <a href="#"><img src="../assets/help.svg" /></a>
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
  height: 50px;
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
  align-items: baseline;
}

header nav a {
  padding-right: 10px;
  padding-left: 10px;
  align-self: end;
}
</style>
