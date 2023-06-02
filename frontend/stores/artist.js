import { defineStore } from 'pinia'
import {Buffer} from 'buffer';

export const useArtistStore = defineStore('artist', {
  state: () => ({ 
    loading: false,
    currentArtist: {},
    currentAlbum: null,
    backupAlbum: null,
    currentAlbumIndex: 0
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
    },
    async getAlbums( album, index ) {
      this.loading = true
      const { data } = await useFetch(
        `http://127.0.0.1:5000/album/${ album }`, { 
          method: 'GET',       
        })
        let response = data
        this.setCurrentAlbum(response['_rawValue'].songs, index)
        this.loading = false
    },
    setCurrentArtist( artist ) {
      this.currentArtist = artist
    },
    setCurrentAlbum( songs, index ) {
      this.currentArtist.albums[index].songs = songs
    }
  },
})