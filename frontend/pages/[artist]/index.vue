<template lang="pug">
.artist-wrapper
  Loader( v-if="checkLoading" )
  .content-wrapper( v-else )
    NuxtLink(to="/") 
      nuxt-icon( name="back")
      span Back to search
    ArtistInfo
    AlbumSlider( 
    ref="AlbumSlider"
    v-if="currentView === 'album'"
    :initialSlide="initialSlideIndex"
    @changeComponent="handler"
    )
    SecondaryTimeline(
    ref="SecondaryTimeline"
      :initialSlide="initialSlideIndex"
      @slideChange="slideChange"
      v-if="currentView === 'album'"
    )
    Timeline(
      v-if="currentView === 'timeline'" 
      @clickedIndex="setSlideIndex"
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
    currentView: "timeline",
    initialSlideIndex: 0
  }),
  methods: {
    handler(event) {
      this.currentView = event
    },
    slideChange(slideIndex) {
      console.log("haha")
      var AlbumSlider = this.$refs.AlbumSlider;
      // var SecondaryTimeline = this.$refs.SecondaryTimeline;
      AlbumSlider.setAlbum(slideIndex);
      this.getSurroundingAlbums(slideIndex)
    },
    setSlideIndex(slideIndex) {
      this.initialSlideIndex = slideIndex
    },
    getSurroundingAlbums( currentSlideIndex ) {
      console.log("test")
      if ( currentSlideIndex !== 0 ) {
        const previousAlbumIndex = currentSlideIndex - 1
        console.log("Previous Album: ", artistStore.currentArtist.albums[previousAlbumIndex])  
        const previousAlbumId = artistStore.currentArtist.albums[previousAlbumIndex].spotify_uri
        artistStore.getAlbums(previousAlbumId, previousAlbumIndex)
      }
      if ( currentSlideIndex !== artistStore.currentArtist.albums.length ) {
        const nextAlbumIndex = currentSlideIndex + 1
        console.log("Next Album: ", artistStore.currentArtist.albums[nextAlbumIndex])  
        const nextAlbumId = artistStore.currentArtist.albums[nextAlbumIndex].spotify_uri
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
  // watch: {
  // 'artistStore.currentAlbumIndex': {
  //   handler(val){
  //     this.getSurroundingAlbums()
  //   },
  //   deep: true
  //   }
  // }
}
</script>


<style lang="scss" scoped>
.artist-wrapper {
  display: flex;
  flex-direction: column;
  padding-top: 50px;

  .content-wrapper {
    display: grid;
    grid-template-columns: 100%;
    grid-template-rows: auto;
    align-self: center;
    row-gap: 32px;
    width: 1040px;
  }
}
a {
  width: fit-content;
  color: #E5E3D4;
  text-decoration: none;
  font: normal 16px "Lato";
  &:hover {
    text-decoration: underline;
  }
}
</style>