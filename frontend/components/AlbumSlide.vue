<template lang="pug">
.slidewrapper
  .breadcrumbs 
    nuxt-icon(name="back" @click="deleteCurrentAlbum") 
    span {{ artistStore.currentArtist.name }} ● {{ artistStore.currentAlbum.name }}
  .content
    .image
    
      
</template>

<script>
import { useArtistStore } from '~~/stores/artist';
const artistStore = useArtistStore()

export default {
  data: () => ({
    artistStore: artistStore
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
  },
  methods: {
    deleteCurrentAlbum() {
      artistStore.currentAlbum = null
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
    display: flex;
    align-items: center;
    > .nuxt-icon svg {
      height: 20px;
      width: 20px;
      cursor: pointer;
      &:hover {
        color: #EE9B80;
      }
    }
    > span {
      font: normal 10px/10px "Lato";
      letter-spacing: 0.2rem;
      text-transform: uppercase;
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