<template>
  <form id="user-form" action="#" method="POST">
    <input id="name-field" type="text" name="name" placeholder="Full Name" required />
    <input id="email-field" type="text" name="email" placeholder="Email" required />
    <div id="address-line1">
      <input id="house-number-field" type="text" name="house-number" placeholder="House Number" />
      <input id="street-field" type="text" name="street-address" placeholder="Street" />
    </div>
    <input id="city-field" type="text" name="city" placeholder="City" />
    <input id="postcode-code" type="text" name="postcode" placeholder="postcode" />
    <button id="submit-form" type="submit" form="user-form"></button> 
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
