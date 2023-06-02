<template lang="pug">
.artistinfo-wrapper 
  img( v-if="artist.image" :src="artist.image.url" )
  img( v-else src="~/assets/icons/person.svg")
  .info
    .genres
      span( v-for="genre in artist.genres" ) {{ genre }}
    .name
      span {{artist.name}}
      .icon
        img( src="~/assets/icons/popularity.svg")
        span {{ artist.popularity }}
</template>

<script>
import { useArtistStore } from '@/stores/artist'
const artistStore = useArtistStore()


export default {
  data: () => ({
    artist: artistStore.currentArtist,
  }),
  // computed: {
  //   genres() {
  //     let length = this.artist.genres.join("").length
  //     if (length <= 50) {
  //       return this.artist.genres
  //     }
  //     let genres = this.artist.genres.slice(0, 3)
  //     genres[2] = this.artist.genres.slice(0, 3)[2] + "..."
  //     return genres
  //   }
  // }
}
</script>

<style lang="scss">
.artistinfo-wrapper {
  display: grid;
  grid-template-columns: 220px auto;
  column-gap: 40px;
  margin-bottom: 24px;
  > img {
    width: 230px;
    height: 230px;
    object-fit: cover;
    border-radius: 10px;
  }
  > .info {
    height: 230px;
    > .genres {
      display: flex;
      grid-area: genre;
      margin: 10px 0 16px 0;
      > span {
        font: normal 18px "Lato";
        text-transform: uppercase;
        color: #AEAEAE;
        &::after {
          content: ", ";
        }
        &:last-child::after {
          content: "";
        }
      }
    }
    > img {
      margin-left: 8px;
      width: 30px;
      height: 30px;
    }
    > .name {
      display: flex;
      height: 150px;
      align-items: center;
      > span {
        font: 300 60px/60px "Georgia";
        color: white;
      }
      > .icon {
        display: flex;
        margin-left: 10px;
        height: fit-content;
        > img {
          width: 30px;
        }
        > span {
          margin-left: 4px;
          font: normal 14px/14px "Lato";
          color: white;
          align-self: center;
        }
      }
    }
    > .description {
      grid-area: description;
      > span {
        font: 300 16px/16px "Lato";
        color: white;
      }
    }
  }
}
</style>