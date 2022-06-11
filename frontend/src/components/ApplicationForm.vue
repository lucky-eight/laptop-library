<template>
  <form>
    <!-- Create form here -->
  </form>
</template>

<script>
export default {
  name: "ApplicationForm",

  data() {
    return {
      user: {
        name: "",
        email: "",
        address: {
          street: "",
          city: "",
          postcode: "",
        },
      },
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
