<template lang="pug">
.layout-wrapper
  Navbar
  router-view
</template>

<script>
import { useSearchStore } from '@/stores/search'
const store = useSearchStore()

export default {
  data: () => ({
    store: store,
    // timer: null
  }),

  mounted() {
    this.store.getAccessToken()
    // this.timer = setInterval(() => {
    //   this.store.getAccessToken()
    // }, 3600000)
  },
  // beforeDestroy() {
  //   clearInterval(this.timer)
  // }
}
</script>
<style lang="scss" scoped>
.layout-wrapper {
  min-height: 100vh;
}
</style>
