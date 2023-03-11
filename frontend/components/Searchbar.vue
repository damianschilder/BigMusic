<template lang="pug">
.search-wrapper
  .search-title 
    span Search an artist to take a journey through their discography.
  .search-input
    input( 
      v-model="query"
      v-on:keyup="getResults( query )"
      placeholder="...Search" )
  .search-results
    .results-grid( v-if="query" )
      NuxtLink.result( 
        v-for="artist in store.results" 
        :to="artist.name"
        @click="setArtist( artist )")
        img( 
          v-if="artist.imageLarge"
          :src="artist.imageLarge")
        span {{ artist.name }}
</template>

<script>
import { useSearchStore } from '@/stores/search'
const store = useSearchStore()

import { useArtistStore } from '@/stores/artist'
const currentArtist = useArtistStore()


export default {
  data: () => ({
    store: store,
    currentArtist: currentArtist,
    query: "",
  }),
  methods: {
    getResults( query ) {
      if (query == "") {
        return
      } else {
        this.store.getResults( query )
      }
    },
    setArtist( artist ) {
      this.currentArtist.setCurrentArtist( artist ) 
    }
  }
}
</script>

<style lang="scss" scoped>
.search-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  > .search-title {
    display: flex;
    justify-content: center;
    margin-bottom: 40px;
    align-self: center;
    width: 860px;
    > span {
      font: 700 40px/40px "Georgia";
      // color: #EDEDED;
      color: #E5E3D4;
    }
  }
  > .search-input {
    display: flex;
    justify-content: center;
    z-index: 10;
    margin-bottom: 20px;
    > input {
      all: unset;
      text-align: left;
      border-bottom: 1px solid #E5E3D4;
      padding: 5px;
      color: #EE9B80;
      width: 700px;
      font: normal 26px/326px "Lato";
      box-sizing: border-box;
      height: 40px;
      &:focus {
        box-shadow: 0px 1.5px #EE9B80;
        border-bottom: 1px solid #EE9B80;
      }
    }
  }
  > .search-results {
    padding: 100px 0 70px 0;
    position: relative;
    transform: translateY(-70px);
    align-self: center;
    // background: linear-gradient(180deg, #231A24 0%, rgba(47, 47, 55, 0.8) 100%);
    border-top: none;
    // border-bottom: 5px solid rgba(0, 0, 0, 0.25);
    // border-right: 5px solid rgba(0, 0, 0, 0.25);
    // border-left: 5px solid rgba(0, 0, 0, 0.25);
    // width: 70vw;
    min-width: 860px;
    > .results-grid {
      margin: 0 auto;
      width: 700px;
      display: grid;
      grid-template-columns: repeat(9, 1fr);
      grid-gap: 20px;
      > .result {
        display: flex;
        grid-row: auto;
        padding: 8px;
        grid-column:  span 3;
        background: rgb(238, 155, 128, 0.5);
        border-radius: 5px;
        text-decoration: none;
        &:hover {
          background: rgb(238, 155, 128, 0.8);
          cursor: pointer;
        }
        > img {
          border-radius: 5px;
          height: 43.5px;
          width: 43.5px;
          object-fit: cover;
        }
        > span {
          padding-left: 8px;
          align-self: center;
          color: white;
          font: normal 14px/14px "Lato";
        }
      }
    }
  }
}
</style>