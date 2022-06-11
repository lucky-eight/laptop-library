<template>
  <form id="application-form" @submit.prevent="handleSubmit">
    <div id="full-name-group">
      <input
        id="first-name-field"
        type="text"
        name="first-name"
        placeholder="First Name"
        v-model="first_name"
        required
      />
      <input id="surname-field" type="text" name="last-name" placeholder="Last Name" v-model="last_name" required />
    </div>
    <input id="email-field" type="text" name="email" placeholder="Email" v-model="email" required />
    <input
      id="address-line1-field"
      type="text"
      name="address-line1"
      placeholder="Address Line 1"
      v-model="address.line_1"
      required
    />
    <input id="address-line2" type="text" name="address-line2" placeholder="Address Line 2" v-model="address.line_2" />
    <input id="city-field" type="text" name="city" placeholder="City" v-model="address.city" required />
    <input id="postcode-code" type="text" name="postcode" placeholder="postcode" v-model="address.postcode" required />
    <button id="submit-form" type="submit" :disabled="isPending">Submit</button>
  </form>
</template>

<script>
import axios from "axios";
export default {
  name: "ApplicationForm",

  data() {
    return {
      first_name: "",
      last_name: "",
      email: "",
      address: {
        line_1: "",
        line_2: "",
        city: "",
        postcode: "",
      },
      isPending: false,
    };
  },

  methods: {
    handleSubmit() {
      this.isPending = true;
      axios
        .post("/submit-form", {
          firstName: this.first_name,
          lastName: this.last_name,
          email: this.email,
          address: {
            line_1: this.address.line_1 + this.address.line_2,
            city: this.address.city,
            postcode: this.address.postcode,
          },
        })
        .then(function (response) {
          console.log(response);
          this.isPending = false;
        })
        .catch(function (error) {
          console.log(error);
          this.isPending = false;
        });
    },
  },
  mounted() {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
