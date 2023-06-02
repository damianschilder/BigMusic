<template lang="pug">
.albumsliderwrapper
  swiper.main( 
    :initialSlide="initialSlide"
    class="primarySwiper"
    :modules="modules")
    swiper-slide( v-for="album in artistStore.currentArtist.albums")
      AlbumSlide( 
        :album="album"
        @changeComponent="handler" )
</template>

<script>
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css';


// import required modules
import { EffectCards } from 'swiper';
import { useArtistStore } from '@/stores/artist'
const artistStore = useArtistStore()

export default {
  data: () => ({
    modules: [],
    artistStore: artistStore,
  }),
  components: {
      Swiper,
      SwiperSlide,
  },
  props: {
    initialSlide: {
      type: Number
    }
  },
  methods: {
    handler(event) {
      this.$emit('changeComponent', event)
    },
    changeAlbum(direction) {
      const swiper = document.querySelector(".primarySwiper").swiper
      if (direction === 'back') {
        swiper.slidePrev()
      }
      if (direction === 'next') {
        swiper.slideNext()
      }
    },
    setAlbum( slideIndex ) {
      const swiper = document.querySelector(".primarySwiper").swiper
      swiper.slideTo( slideIndex )
    },
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

<style lang="scss" scoped>
.main {
  /* height: 600px; */
  background: rgba(217, 217, 217, 0.05);
  border-radius: 20px;
  padding-bottom: 32px;
}

.secondarywrapper {
  display: flex;
  align-items: center;
  background: rgba(217, 217, 217, 0.05);
  border-radius: 20px;
  margin-top: 32px;
  border-radius: 20px;
  padding: 12px 32px;
  & .swiper-slide {
    display: flex;
    justify-content: center;
    width: 140px;
  }
  & .nuxt-icon svg {
    width: 50px;
    height: 50px;
  }
}
</style>
