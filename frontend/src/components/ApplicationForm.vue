<template>

  <form id="application-form" @submit.prevent="handleSubmit">
    <br>
    <h3 id="form-explanation">In need of a laptop? Fill in this form and we could send one to you</h3>

    <div id="full-name-group" class="form-field-container">
      <input
        id="first-name-field"
        type="text"
        name="first-name"
        placeholder="First Name"
        v-model="first_name"
        required
      />
      <input
      id="surname-field"
      type="text" name="last-name"
      placeholder="Last Name"
      v-model="last_name"
      required
      />
    </div>

    <div class="form-field-container">
      <input
      id="email-field"
      type="text"
      name="email"
      placeholder="Email"
      v-model="email"
      required
      />
    </div>

    <div class="form-field-container">
      <input
        id="address-line1-field"
        type="text"
        name="address-line1"
        placeholder="Address Line 1"
        v-model="address.line_1"
        required
      />
    </div>

    <div class="form-field-container">
      <input
      id="address-line2"
      type="text"
      name="address-line2"
      placeholder="Address Line 2"
      v-model="address.line_2"
      />
    </div>

    <div class="form-field-container">
      <input
      id="city-field"
      type="text"
      name="city"
      placeholder="City"
      v-model="address.city"
      required
      />
    </div>

    <div class="form-field-container">
      <input
      id="postcode-code"
      type="text"
      name="postcode"
      placeholder="Postcode"
      v-model="address.postcode"
      required
      />
    </div>

    <div class="form-field-container-button">
       <button id="submit-form" type="submit" :disabled="isPending">Submit</button>
    </div>

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
      const instance = axios.create({baseURL: 'http://localhost:5000'})
      instance
        .post("/request-laptop/", {
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

<!-- Add "scoped" attribute to limit CSS to this component only

FORM HEIGHT -->
<style scoped>


form {
  display: flex;
  align-items: center;
  justify-items: center;
  flex-wrap: wrap;
  height: fit-content;
  flex-direction: column;
  padding: 25px;
}

h3{
  padding: 10px;
  padding-bottom: 40px;
}

 form input {
  height: 40px;
  width: 100%;
  margin-left: 10px;
  margin-right: 10px;
  margin-top: 5px;
  margin-bottom: 5px;
 }

 .form-field-container{
  width: 300px;
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
  flex-direction: row;
  text-align: center;
 }

 .form-field-container-button{
  width: 300px;
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
  flex-direction: row;
  text-align: center;
  padding-left: 58px;
  padding-top: 15px;
 }

 button {
  margin-left: 10px;
  margin-right: 10px;
  background-color: #c8dda4;
  border-radius: 5px;
  border: none;
  height: 40px;
  width: 70%;
 }

 #form_explanation{
  padding-top: 20px;
  text-align: center;
 }


</style>
