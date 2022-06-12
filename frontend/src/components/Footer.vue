<template>
  <footer>
    <ul>

      <!-- <li><a id="link" href="#">Home</a></li> -->
      <li><a id="link" href="#">About Us</a></li>
      <li><a id="link" href="#">My Account</a></li>
      <!-- <li><a id="link" href="#">Business Account</a></li> !-->

    </ul>
  </footer>
</template>

<script>
export default {
  name: "GlobalFooter",
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
footer {
  height: fit-content;
  width: 100%;
  background-color: #c8dda4;
  bottom: 0;
  position: absolute;
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

#links{
  color: black;
}

a{
  color: black;
}


</style>
