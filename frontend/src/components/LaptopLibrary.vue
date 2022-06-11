<template>
  <div>
    <ApplicationForm v-if="!submitted" />
    <Result v-else />
  </div>
</template>

<script>
import ApplicationForm from "./ApplicationForm.vue";
import Result from "./Result.vue";
export default {
  name: "LaptopLibrary",
  components: {
    Result,
    ApplicationForm,
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
