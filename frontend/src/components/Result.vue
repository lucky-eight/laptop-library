<template>
  <div class="result-wrapper">
    <div v-if="isSuccess && deliveryDate" class="success-wrapper">
      <h2>We've found a match!</h2>
      <p>You can expect to receive a laptop by {{ deliveryDate }}</p>
    </div>
    <div v-else class="unsuccess-wrapper">
      <h2>Unfortunately there are no laptops currently available</h2>
      <p>We will be in touch when we've found a match</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "ResultSection",
  props: {
    isSuccess: {
      type: Boolean,
      default: false,
    },
    deliveryDate: {
      type: String,
      default: "",
    },
  },
};
</script>

<style scoped>
  .success-wrapper{
    text-align: center;
  }
  .unsuccess-wrapper{
    text-align: center;
  }

  h2{
    padding: 15px;
  }
</style>
