<template lang="pug">
.wrapper
  .element-wrapper
    span Big Music
</template>

<style lang="scss" scoped>
.wrapper {
  .element-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 75px;
    background: #33273B;
    > span {
      font: bold 30px/30px "Brawler";
      color: white;
    }
  }
}
</style>