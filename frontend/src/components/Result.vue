<template>
  <div class="result-wrapper">
    <div v-if="isSuccess && deliveryDate" class="success-wrapper">
      <p>We've found a match!</p>
      <p>You can expect to receive a laptop by {{ deliveryDate }}</p>
    </div>
    <div v-else class="unsuccess-wrapper">
      <p>Unfortunately there are no laptops currently available</p>
      <p>We will be in touch when we've found a match</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Result",
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

<style scoped></style>
