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
  }),

  mounted() {
    this.store.getAccessToken()
  },
}
</script>
<style lang="scss" scoped>
.layout-wrapper {
  min-height: 100vh;
}
</style>
