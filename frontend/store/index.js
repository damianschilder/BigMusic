import axios from 'axios';
import vuex from 'vuex';

export const state = () => ({
  searchResults: [],
  artist: {
    spotifyId: '6liAMWkVf5LH7YR9yfFy1Y',
    musicbrainzId: '40d758a4-b7c2-40f3-b439-5efbd2a3b038',
    name: 'Portishead',
    images: [
      {'height': 680, 
      'url': 'https://i.scdn.co/image/05d3721739aee511a898081ab140daa7890a0120', 
      'width': 1000
      }, 
      {'height': 435, 
      'url': 'https://i.scdn.co/image/27802710b01453435de93d71bab2c9988a841ace', 
      'width': 640
      }, 
      {'height': 136, 
      'url': 'https://i.scdn.co/image/333ac38e3c8ab5fcdc238cc46535a4abb802eccc', 
      'width': 200
      }, 
      {'height': 44, 
      'url': 'https://i.scdn.co/image/10052054c06626f6a900e687b20886e462f75568', 
      'width': 64
      }],
    area: {
      country: 'United Kingdom',
      area: 'Bristol'
    },
    lifeSpan: {
      begin: 1991,
      end: false
    },
    genres: ['dark pop', 'electronica', 'laboratorio', 'trip hop'],
    popularity: 60,
  }
})

export const mutations = {
  setResults (state, results) {
    console.log(results)
    let searchResults = []
    results.forEach(function (result, index) {
      searchResults.push({
        'id': result.id,
        'name': result.name        
      })
    });
    state.searchResults = searchResults
    // this.state.artistResults.push({
    //   'id': artist.id, 
    //   'name': artist.name, 
    //   'imageLarge': artist.images[0].url, 
    //   'imageMedium': artist.images[1].url, 
    //   'imageSmall': artist.images[2].url, 
    //   'pageRank': pageRank, 
    //   'popularity': artist.popularity, 
    //   'index': i, 'elo': 1000})
  },
}

export const actions = {
  getResults ({ commit }, query) {
		const config = {
			method: 'get',
			url: `http://127.0.0.1:5000/search/${ query }`,
		}
    return axios(config)
    .then(function (response) {
      commit('setResults', response.data)
      // console.log(response.data);
    })
    .catch(function (error) {
      console.log(error)
    })
	},
}

export const getters = {

}