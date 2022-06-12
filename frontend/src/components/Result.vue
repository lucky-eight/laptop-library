<template>
  <div class="result-wrapper"> {{reponse}}
    <div v-if="isSuccess && deliveryDate" class="success-wrapper">
        <h2>We've found you a laptop!</h2>
        <img src="../assets/match_success.png">
        <p>APPLE MacBook Air 13.3" (2020) - M1, 256 GB SSD, Silver <br>
        We'll be in touch soon with delivery or pick up instructions</p>
    </div>
    <div v-else class="unsuccess-wrapper">
        <h2>Unfortunately there are no laptops currently available</h2>
        <img src="../assets/match_failure.png">
        <p>You are on the waiting list; we will be in touch when we've found a match</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "ResultSection",
  props: {
    response : {
      type: Object,
      default: () => ({})
    }
  },
};
</script>

<style scoped>
    body{
        text-align: center;
        font-family: 'Jost', sans-serif;
    }
    .success-wrapper{
        padding-top: 50px;
    }
    .unsuccess-wrapper{
        padding-top: 50px;
    }

    h2{
      padding: 15px;
    }

    img{
        height: 100px;
        width: 100px;
    }
</style>