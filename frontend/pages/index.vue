<template lang="pug">
.wrapper
  //- Searchbar
  Timeline
</template>

<script>
import { useSearchStore } from '@/stores/search'
const store = useSearchStore()


export default {
  data: () => ({
    store: store
  }),
}
</script>

<style lang="scss" scoped>
.wrapper {
  padding-top: 80px;
  display: flex;
  justify-content: center;
  flex-direction: column;
  // height: calc(100vh - 75px)
}
</style>
