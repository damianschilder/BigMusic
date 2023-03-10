<template>
  <p>{{ $route.params.artist }} - {{ $route.params.album }}</p>
</template>

<script>
  export default {
    async asyncData({ params }) {
      const book = params.book
      const slug = params.slug
      return { book, slug }
    }
  }
</script>
