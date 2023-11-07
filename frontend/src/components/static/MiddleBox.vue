<template>
  <div class="box">
    <slot />
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
  .box {
    height: auto;
    min-height:80px;
		width:48%;
    margin: 0 auto;
    padding: 1% ;
    border-radius: 15px;
    background: white;
  }

  @media (max-width: 1100px) {
    .box {
      width: 95%;
    }
  }
</style>
