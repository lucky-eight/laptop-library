<template>
  <div>
    <ApplicationForm v-if="!submitted" />
    <Result v-else :is-success="result.isSuccess" />
  </div>
</template>

<script>
import ApplicationForm from "application-form.vue";
import Result from "result.vue";
export default {
  name: "Home",

  data() {
    return {
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
