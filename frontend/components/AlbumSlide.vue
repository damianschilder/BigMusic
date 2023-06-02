<template lang="pug">
.slidewrapper
  .breadcrumbs 
    nuxt-icon(name="back" @click="backToTimeline") 
    span {{ artistStore.currentArtist.name }} ● 
    span  &nbsp{{ album.name }}
  .content
    .image
      img( v-if="album.image" :src="album.image.url")
    .description 
      span {{album.name}}
    .tracks
      .header 
        span.index #
        span.name Name
        span.duration Length
      .track( v-for="track, index in album.songs")
        span.index {{index}} 
        span.name {{track.name}} 
        span.duration {{millisToMinutesAndSeconds(track.length)}} 
    
      
</template>

<script>
import { useArtistStore } from '~/stores/artist';
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
    currentAlbum() {
      return artistStore.currentArtist.albums[artistStore.currentAlbumIndex]
      // if (this.album.image.url ) {
      //   return this.album.image.url
      // }
      // return false
    }
  },
  methods: {
    backToTimeline() {
      this.$emit('changeComponent', 'timeline')
    },
    millisToMinutesAndSeconds(millis) {
      var minutes = Math.floor(millis / 60000);
      var seconds = ((millis % 60000) / 1000).toFixed(0);
      return minutes + ":" + (seconds < 10 ? '0' : '') + seconds;
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
  padding: 1.5rem 2rem;
  row-gap: 0.75rem;
  > .breadcrumbs {
    display: flex;
    align-items: center;
    > .nuxt-icon svg {
      height: 20px;
      width: 20px;
      cursor: pointer;
      &:hover {
        color: grey;
      }
    }
    > span {
      font: normal 10px/10px "Lato";
      letter-spacing: 0.2rem;
      text-transform: uppercase;
      transition: color 0.5s;
      &:last-child {
        color: #EE9B80;
      }
    }
  }
  > .content {
    display: grid;
    grid-template-columns: 260px auto 373px;
    grid-template-rows: 260px;
    column-gap: 32px;
    margin-top: 8px;
    > .image {
      display: flex;
      column-gap: 40px;
      > img {
        width: 260px;
        height: 260px;
        border-radius: 10px;
        overflow: hidden;
        // filter: drop-shadow(0 0 0.25rem black);
      }
    }
    > .description {
      font: 300 60px "Lato"
    }
    > .tracks {
      display: flex;
      flex-direction: column;
      overflow-y: scroll;
      scroll-snap-type: y mandatory;
      > .header {
        display: grid;
        grid-template-columns: min-content auto min-content;
        column-gap: 12%;
        padding: 8px 22px;
        background-color: #231A24;
        border-radius: 10px;
        font-weight: bold;
      }
      > .track {
        display: grid;
        grid-template-columns: min-content auto min-content;
        column-gap: 12%;
        padding: 8px 22px;
        border-radius: 10px;
        font-size: 14px;
        cursor: pointer;
        transition: font-weight 0.1s, color 0.1s;
        &:nth-child(odd) {
          background-color: #231A24;
        }
        &:hover {
          color: #EE9B80;
          font-weight: bold;
        }
      }
    }
  }
  > .name {
    display: flex;
    flex-direction: column;
  }
}
</style>