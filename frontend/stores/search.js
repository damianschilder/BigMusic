import { defineStore } from 'pinia'
import {Buffer} from 'buffer';

export const useSearchStore = defineStore('search', {
  state: () => ({ 
    results: [], 
    accessToken: ''
  }),
  // getters: {
  //   doubleCount: (state) => state.count * 2,
  // },
  actions: {
    async getAccessToken() {
      const client_id = "5079c4f5a0a744cea9ad93dd277d7fd6";
      const client_secret = '5beac193cee4460094d0b4cf639f28d0';
      const { data } = await useFetch(
        'https://accounts.spotify.com/api/token', { 
        method: 'POST',       
        headers: { 
        'Authorization': 'Basic ' + (Buffer.from(client_id + ':' + client_secret).toString('base64')),
        'Content-Type': 'application/x-www-form-urlencoded'
       },
       body: 'grant_type=client_credentials',
      })
      let access_token = data['_rawValue']['access_token']
      this.setAccessToken( access_token )
    },
    setAccessToken( access_token ) {
      this.accessToken = access_token
    },

    async getResults( query ) {
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
    setResults( artists ) {
      this.results = []
      for (var i=0, artist; artist = artists[i]; i++) {
        var pageRank = ( i + 1 ) / ( artist.popularity / 100 )
        let object = {
          'id': artist.id, 
          'name': artist.name,
          'genres': artist.genres, 
          'pageRank': pageRank, 
          'popularity': artist.popularity, 
          'index': i }
          if ( artist.images[0] ) object.imageLarge = artist.images[0].url;
          if ( artist.images[1] ) object.imageMedium = artist.images[1].url;
          if ( artist.images[2] ) object.imageSmall = artist.images[2].url;
          this.results.push( object )
        }
      this.results.sort((a, b) => (a.pageRank > b.pageRank) ? 1 : (a.pageRank === b.pageRank) ? 1 : -1 )
    },
    clearResults() {
      this.results = []
    }
  },
})