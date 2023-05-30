import Vue from 'vue'

export default defineNuxtConfig({
  pages: true,
  css: [
    "@/assets/styles/app.scss", 
    "@/assets/styles/breakpoints.scss" ],
  modules: [
    '@pinia/nuxt',
    'nuxt-icons'
  ],
})