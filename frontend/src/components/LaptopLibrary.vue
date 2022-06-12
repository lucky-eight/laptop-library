<template>
  <div>
    <Header />
    <ApplicationForm/>
    <Footer />
  </div>
</template>

<script>
import Header from "./Header.vue"
import ApplicationForm from "./ApplicationForm.vue";
import Footer from "./Footer.vue"
export default {
  name: "LaptopLibrary",
  components: {
    Header,
    ApplicationForm,
    Footer,
  },

  data() {
    return {
      submitted: false,
      result: {
      },
    };
  },
  methods: {
    updateState(laptopAvailability) {
      this.result = laptopAvailability
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
