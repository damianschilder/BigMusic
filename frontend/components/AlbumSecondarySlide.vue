<template lang="pug">
.albumsecondaryslidewrapper
  img( v-if="album.image" :src="album.image.url")
  span {{album.name}}

</template>

<script>
export default {
  data: () => ({
    // artistStore: artistStore
  }),
  props: {
    album: {
      type: Object
    }
  },
}
</script>

<style lang="scss" scoped>
.albumsecondaryslidewrapper {
  display: flex;
  align-items: center;
  font-size: 14px;
  column-gap: 8px;
  width: max-content;
  min-height: 30px;
  background-color: #7C7E83;
  border-radius: 5px;
  padding: 8px 32px 8px 12px;
}
img {
  width: 30px;
  height: 30px;
  border-radius: 5px;
}
</style>