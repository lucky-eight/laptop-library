<template>
  <form id="user-form" action="#" method="POST">
    <div id="full-name-group">
      <input id="first-name-field" type="text" name="first-name" placeholder="First Name" required />
      <input id="surname-field" type="text" name="surname" placeholder="Surname" required />
    </div>
      <input id="email-field" type="text" name="email" placeholder="Email" required />
      <input id="address-line1-field" type="text" name="address-line1" placeholder="Address Line 1" />
      <input id="address-line2" type="text" name="address-line2" placeholder="Address Line 2" />
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
