import { defineStore } from 'pinia'
import {Buffer} from 'buffer';

export const useArtistStore = defineStore('artist', {
  state: () => ({ 
    currentArtist: {}
  }),
  actions: {
    async getArtist() {
      const { data } = await useFetch(
        `https://api.spotify.com/v1/search?q=${ query }&type=artist&limit=12`, { 
        method: 'GET',       
        headers: { 
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${ this.accessToken }`
       },
      })
      let response = data['_rawValue']['artists']['items']
      this.setResults( response )

    },
    setCurrentArtist( artist ) {
      this.currentArtist = artist
    }
  },
})