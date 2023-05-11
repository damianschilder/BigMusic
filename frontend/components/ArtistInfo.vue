<template lang="pug">
.artistinfo-wrapper 
  img( v-if="artist.imageLarge" :src="artist.imageLarge" )
  img( v-else src="~/assets/svg/person.svg")
  .info
    .genres-container
      .genres
        span( v-for="genre in artist.genres" ) {{ genre }}
      img( src="~/assets/svg/readmore.svg")

    .icons
      .icons-pair
        img( src="~/assets/svg/popularity.svg")
        span {{ artist.popularity }}
    .name
      span {{artist.name}}
    .description 
      span  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent non elit purus. Nullam efficitur leo convallis facilisis fringilla. Aliquam mauris turpis, convallis sed elit at, fringilla consequat ipsum. Nullam ultricies ac ipsum sed iaculis. Ut laoreet nibh et suscipit varius. Vestibulum fermentum sem eu eros sagittis mattis. Integer leo dolor, blandit ac diam in, ultricies ultricies nulla.
    
</template>

<script>
import { useArtistStore } from '@/stores/artist'
const artist = useArtistStore()


export default {
  data: () => ({
    artist: artist.currentArtist,
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
  margin-top: 50px;
  > img {
    width: 230px;
    height: 230px;
    object-fit: cover;
    border-radius: 10px;
  }
  > .info {
    display: grid;
    grid-template-areas: 
    'genre genre'
    'name icons'
    'description description';
    grid-template-rows: min-content;
    grid-template-columns: auto 51px;
    width: 100%;
    > .genres-container {
      display: flex;
      // justify-content: space-between;
      grid-area: genre;
      // margin-bottom: 16px;
      margin-top: 10px;
      > .genres {
        width: fit-content;
        align-self: center;
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
    }
    > .icons {
      display: flex;
      grid-area: icons;
      justify-content: flex-end;
      width: fit-content;
      > .icons-pair {
        display: flex;
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
    > .name {
      grid-area: name;
      > span {
        font: 300 60px/60px "Georgia";
        color: white;
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