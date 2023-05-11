import { defineStore } from 'pinia'
import {Buffer} from 'buffer';

export const useArtistStore = defineStore('artist', {
  state: () => ({ 
    loading: false,
    currentArtist: {}
  }),
  
  actions: {
    async getArtist( artist ) {
      this.loading = true
      const { data } = await useFetch(
        `http://127.0.0.1:5000/artist/${ artist }`, { 
          method: 'GET',       
        })
        let response = data
        this.setCurrentArtist(response['_rawValue'])
        this.loading = false
        console.log(response['_rawValue'])
    },
    setCurrentArtist( artist ) {
      this.currentArtist = artist
    }
  },
})