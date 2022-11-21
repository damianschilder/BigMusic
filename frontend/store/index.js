import axios from 'axios';
import vuex from 'vuex';

export const state = () => ({
  searchResults: [],
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