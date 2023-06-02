<template lang="pug">
.artist-wrapper
  Loader( v-if="checkLoading" )
  .content-wrapper( v-else )
    ArtistInfo
    AlbumSlider( v-if="currentView === 'album'"
    @changeComponent="handler"
    )
    Timeline(
      v-if="currentView === 'timeline'" 
      @changeComponent="handler"
    )
    //- h1( v-if="currentView === 'album'") hahahaha
    //- //- Timeline( v-if="!artistStore.currentAlbum" )
</template>

<script>
import { useArtistStore } from '~/stores/artist'
const artistStore = useArtistStore()

export default {
  data: () => ({
    artistStore: artistStore,
    loading: false,
    currentView: "timeline"
  }),
  methods: {
    handler(event) {
      this.currentView = event
    },
    getSurroundingAlbums() {
      if (artistStore.currentAlbumIndex !== 0) {
        console.log("Previous Album: ", artistStore.currentArtist.albums[artistStore.currentAlbumIndex - 1])  
        const previousAlbumId = artistStore.currentArtist.albums[artistStore.currentAlbumIndex - 1].spotify_uri
        const previousAlbumIndex = artistStore.currentAlbumIndex - 1
        artistStore.getAlbums(previousAlbumId, previousAlbumIndex)
      }
      if ((artistStore.currentAlbumIndex + 1) !== artistStore.currentArtist.albums.length) {
        console.log("Next Album: ", artistStore.currentArtist.albums[artistStore.currentAlbumIndex + 1])  
        const nextAlbumId = artistStore.currentArtist.albums[artistStore.currentAlbumIndex + 1].spotify_uri
        const nextAlbumIndex = artistStore.currentAlbumIndex + 1
        artistStore.getAlbums(nextAlbumId, nextAlbumIndex)
      }
    }
  },
  computed: {
    checkLoading() {
      if ( 'name' in artistStore.currentArtist ) {
        return false
      }
      return true
    }
  },
  watch: {
  'artistStore.currentAlbumIndex': {
    handler(val){
      this.getSurroundingAlbums()
    },
    deep: true
    }
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