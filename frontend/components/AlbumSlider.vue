<template lang="pug">
.albumsliderwrapper
  //- h1 {{ artist }}
  swiper.mySwiper( :modules="modules")
    swiper-slide( v-for="album in artist.currentArtist.albums")
      AlbumSlide( :album="album")
</template>

<script>
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css';


// import required modules
import { EffectCards } from 'swiper';
import { useArtistStore } from '@/stores/artist'
const artist = useArtistStore()

export default {
  data: () => ({
    modules: [],
    artist: artist,
  }),
  components: {
      Swiper,
      SwiperSlide,
  },
}
</script>

<style>
.swiper {
  height: 600px;
  background: rgba(217, 217, 217, 0.05);
  border-radius: 20px;
}

</style>
