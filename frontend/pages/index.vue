<template lang="pug">
.wrapper
  Search
</template>

<script>
import Search from '~/components/search/Search'

export default {
  components: { Search },
  name: 'index',
  layout: 'default',
  data: () => ({
  }),
}
</script>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  // background: green;
  flex-direction: column;
  justify-content: center;
}
</style>