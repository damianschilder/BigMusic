<template lang="pug">
.artist-wrapper
  Loader( v-if="artist.loading" )
  .content-wrapper( v-else )
    //- ArtistInfo
    Timeline
    //- AlbumSlider
</template>

<script>
import { useArtistStore } from '@/stores/artist'
const artist = useArtistStore()

export default {
  data: () => ({
    artist: artist,
    loading: false
  }),
}
</script>


<style lang="scss">
.artist-wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
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