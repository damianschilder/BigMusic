<template lang="pug">
.secondarytimelinewrapper 
  nuxt-icon( name="back" @click="changeAlbum('back')")
  swiper.secondary(
    :initialSlide="initialSlide"
    :centeredSlides="true"
    :slidesPerView="3"
    :modules="modules"
    @slideChange="onSlideChange"
    ref="secondaryTimeline"
    class="secondarySwiper")
    swiper-slide( v-for="album in artistStore.currentArtist.albums" )
      AlbumSecondarySlide( :album="album")
  nuxt-icon.test( name="back" @click="changeAlbum('next')")
</template>

<script>
import { Swiper, SwiperSlide } from 'swiper/vue';
import { useSwiper } from 'swiper/vue';
import 'swiper/css';
// const swiper = useSwiper();

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
      const swiper = document.querySelector(".secondarySwiper").swiper
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
    onSlideChange() {
      const swiper = document.querySelector(".secondarySwiper").swiper
      this.$emit('slideChange', swiper.activeIndex)
    }
  }
}
</script>

<style lang="scss" scoped>
.secondarytimelinewrapper {
  display: flex;
}

.swiper-slide {
  display: flex;
  justify-content: center;
}

:deep( .nuxt-icon ) {
  display: flex;
  align-items: center;
  cursor: pointer;
  &:hover {
    color: grey;
  }
}
:deep( svg ) {
  width: 30px;
  height: 30px;
}
:deep( .test ) {
  transform: rotate(180deg);
}
</style>