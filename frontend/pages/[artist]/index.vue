<template lang="pug">
.artist-wrapper
  .content-wrapper
    ArtistInfo
    Timeline
</template>

<script>
export default {
  data:() => {
    
  }
}
</script>


<style lang="scss">
.artist-wrapper {
  display: flex;
  flex-direction: column;
  .content-wrapper {
    display: grid;
    grid-template-columns: 100%;
    grid-template-rows: auto;
    gap: 60px;
    align-self: center;
    width: 1040px;
  }
}
</style>