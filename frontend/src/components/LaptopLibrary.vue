<template>
  <div>
    <Header />
    <ApplicationForm v-if="!submitted" />
    <Result v-else />
    <Footer />
  </div>
</template>

<script>
import Header from "./Header.vue"
import ApplicationForm from "./ApplicationForm.vue";
import Result from "./Result.vue";
import Footer from "./Footer.vue"
export default {
  name: "LaptopLibrary",
  components: {
    Header,
    ApplicationForm,
    Result,
    Footer,
  
  },

  data() {
    return {
      submitted: false,
      result: {
        isSuccess: null,
        deliveryDate: "",
      },
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
