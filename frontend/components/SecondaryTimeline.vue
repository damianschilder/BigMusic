<template lang="pug">
.secondarytimelinewrapper 
  nuxt-icon( name="back" @click="changeAlbum('previous')")
  swiper.secondary(
    :initialSlide="artistStore.currentAlbumIndex"
    :slidesPerView="3"
    :spaceBetween="30"
    :centeredSlides="true"
    :modules="modules"
    class="mySwiper")
    swiper-slide( v-for="album in artistStore.currentArtist.albums" )
      AlbumSecondarySlide( :album="album")
  nuxt-icon( name="back" @click="changeAlbum('next')")
</template>

<script>
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css';


// import required modules
import { EffectCards } from 'swiper';
import { useArtistStore } from '@/stores/artist'
const artistStore = useArtistStore()
const swiper = document.querySelector('.swiper').swiper;

export default {
  data: () => ({
    modules: [],
    artistStore: artistStore,
  }),
  components: {
      Swiper,
      SwiperSlide,
  },
  methods: {
    handler(event) {
      this.$emit('changeComponent', event)
    },
    changeAlbum(direction) {
      if ('back') {
        artistStore.currentAlbumIndex =+ 1
        // swiper.slidePrevious() 
      }
      if ('next') {
        const test = artistStore.currentAlbumIndex
        artistStore.currentAlbumIndex = test + 1
        // swiper.slideNext()
      }
    }
  //   getSurroundingAlbums() {
  //     if (artistStore.currentAlbumIndex !== 0) {
  //       console.log("Previous Album: ", artistStore.currentArtist.albums[artistStore.currentAlbumIndex - 1])  
  //       const previousAlbumId = artistStore.currentArtist.albums[artistStore.currentAlbumIndex - 1].spotify_uri
  //       const previousAlbumIndex = artistStore.currentAlbumIndex - 1
  //       artistStore.getAlbums(previousAlbumId, previousAlbumIndex)
  //     }
  //     if ((artistStore.currentAlbumIndex + 1) !== artistStore.currentArtist.albums.length) {
  //       console.log("Next Album: ", artistStore.currentArtist.albums[artistStore.currentAlbumIndex + 1])  
  //       const nextAlbumId = artistStore.currentArtist.albums[artistStore.currentAlbumIndex + 1].spotify_uri
  //       const nextAlbumIndex = artistStore.currentAlbumIndex + 1
  //       artistStore.getAlbums(nextAlbumId, nextAlbumIndex)
  //     }
  //   }
  // },
  // // mounted() {
  // //   this.getSurroundingAlbums()
  // // },
  // watch: {
  // 'artistStore.currentAlbumIndex': {
  //   handler(val){
  //     console.log("test")
  //     this.getSurroundingAlbums()
  //   },
  //   deep: true
  //   }
  }
}
</script>