<template lang="pug">
.wrapper
  .search
    span Search artists, albums or songs to get started
    input(
      type="text"
      v-model="query"
      v-on:keyup="searchQuery( query )"
      placeholder="...Search" )

  .results(v-show="this.query")
    .results__result( 
      v-for="result,i in this.$store.state.searchResults"
      :result="result"
      :key="i" )
      span {{ result.name }}
</template>

<script>
export default {
  layout: 'default',
  data: () => ({
    query: "",
  }),
  methods: {
    searchQuery( query ) {
      this.$store.dispatch("getResults", query)
    },
  }
}
</script>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  width: max-content;
  margin: 0 auto;
  > .search {
    display: flex;
    flex-direction: column;
    justify-content: center;
    > span {
      font-size: 35px;
      font-weight: 700;
      // color: #E5E3D4;
      color: #DFD1AE;
      margin-bottom: 30px;
    }
    > input {
      all: unset;
      width: 90%;
      margin: auto;
      text-align: left;
      border-bottom: 1px solid #E5E3D4;
      padding: 5px;
      color: #EE9B80;
      // color: #E4B19D;
      font-size: 20px;
      font-weight: 200;
      box-sizing: border-box;
      height: 40px;
      z-index: 5;
      &:focus {
        // box-shadow: 0px 1.5px #EE9B80;
        box-shadow: 0px 1.5px #E4B19D;
      }
    }
  }
  > .results {
    height: 300px;
    // width: 85%;
    // transform: translateY(0px);
    background-color: rgb(255,255,255);
    background: linear-gradient(180deg, rgb(30, 30, 39) 0%, rgba(47, 47, 55, 0.8) 100%); 
    border: 1px solid rgba(0, 0, 0, 0.25);
    border-top: none;
    border-bottom: 5px solid rgba(0, 0, 0, 0.25);
    // margin-left: auto;
    // margin-right: auto;
    z-index: 3;
    // padding: 0 32px;
    // left: 0;
    // right: 0;
    > .results__result {
      > span {
        color: white;
      }
    }
  }
}
</style>