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
    min-height:80px;
		width:100%;
		float:left;
    margin-bottom: 1%;
    padding: 1%;
    border-radius: 15px;
    background: white;

  }

</style>
