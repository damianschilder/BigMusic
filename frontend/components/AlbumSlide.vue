<template lang="pug">
.slidewrapper
  .breadcrumbs 
    span PORTISHEAD > DUMMY > MYSTERONS
  .content
    .header
      AlbumDetails
    //-   img( v-if="album && album.image && album.image.url" :src="album.image.url")
    //-   .name 
    //-     span {{ album.name }}
</template>

<script>
export default {
  data: () => ({
  }),
  props: {
    album: {
      type: Object
    }
  },
  computed: {
    background() {
      // if (this.album.image.url ) {
      //   return this.album.image.url
      // }
      // return false
    }
  }
}
</script>

<style lang="scss">
.slidewrapper {
  display: flex;
  flex-direction: column;
  color: white;
  font-size: 1rem;
  padding: 0.75rem 2rem;
  row-gap: 0.75rem;
  > .breadcrumbs {
    > span {
      font: normal 10px/10px "Lato";
      letter-spacing: 0.2rem;
    }
  }
  > .content {
    > .header {
      display: flex;
      column-gap: 40px;
    }
  }
  img {
    width: 260px;
    height: 260px;
  }
  > .name {
    display: flex;
    flex-direction: column;
  }
}
</style>