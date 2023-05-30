<template lang="pug">
.chartwrapper
  //- Button(@click="test()") test
  ClientOnly
    apexchart(
      type="scatter" 
      height="350" 
      :options="chartOptions" 
      @dataPointSelection="dataPointSelectionHandler"

      :series="series")
</template>

<script>
import { useArtistStore } from '~~/stores/artist';
const artistStore = useArtistStore()

export default ({
  data() {
    return {
    allAlbums: [],

    series: this.formatSeries(),
    chartOptions: {
      chart: {
        height: 350,
        type: 'scatter',
        zoom: {
          type: 'xy'
        },
        animations: {
        enabled: false,
        easing: 'easeinout',
        speed: 800,
        animateGradually: {
            enabled: false,
            delay: 150
        },
        dynamicAnimation: {
            enabled: false,
            speed: 350
        }
    }
      },
      dataLabels: {
        enabled: false,
        textAnchor: 'start',
        formatter: function(val, opt) {
            return artistStore.currentArtist.albums[opt.seriesIndex].name
        },
        offsetX: 0,
      },
      grid: {
        show: false,
      },
      xaxis: {
        type: 'datetime',
        labels: {
          style: {
            color: '#FFFFFF',
            cssClass: 'xaxislabel',
          }
        }
      },
      legend: {
        show: false
      },
      markers: {
        size: 30,
        // shape: 'circle',
        radius: 0
      },
      // fill: {
      //   type: 'image',
      //   opacity: 1,
      //   image: {
      //     src: this.gatherImages(),
      //     width: 60,
      //     height: 60
      //   }
      // },
      tooltip: {
        custom: function({series, seriesIndex, dataPointIndex, w}) {
          var data = w.globals.initialSeries[seriesIndex].data[dataPointIndex];
          return '<ul>' +
          '<span>'+ artistStore.currentArtist.albums[seriesIndex].name +'</span>' +
          '<br>'+'</br>' +
          '<span>'+ artistStore.currentArtist.albums[seriesIndex].release_date +'</span>' +
          // '<li><b>Number</b>: ' + data.y + '</li>' +
          // '<li><b>Product</b>: \'' + data.product + '\'</li>' +
          // '<li><b>Info</b>: \'' + data.info + '\'</li>' +
          // '<li><b>Site</b>: \'' + data.site + '\'</li>' +
          '</ul>';
        }
      }
    },
  }
},
  computed: {
  },
  methods: {
    test() {
      alert("haha")
    },
    formatSeries () {
      let albums = artistStore.currentArtist.albums
      let series = []
      for (const index in albums) {
        let album = albums[index]
        let serie = {
          name: album.name,
          data: [ [album.release_date * 1000, album.relevance_score] ]
        }
        series.push(serie)
      }
      return series
    },
    gatherImages () {
      let albums = artistStore.currentArtist.albums
      let images = []
      for (const index in albums) {
        let album = albums[index]
        if (album.image) {
          images.push(album.image.url)
        } else {
          images.push('https://i.ibb.co/xhMYYRD/Screen-Shot-2019-03-04-at-4-45-20-PM.png')
        }
      }
      return images
    },
    dataPointSelectionHandler (event, chartContext, config) {
      // console.log(chartContext);  
      let spotifyUri = artistStore.currentArtist.albums[config.seriesIndex].spotify_uri;
      var result = /[^:]*$/.exec(spotifyUri)[0];
      // console.log(result)
      artistStore.getAlbums(spotifyUri)
    },
  },
})
</script>

<style lang="scss" scoped>
::v-deep(*) {
  .apexcharts-xaxis, .apexcharts-yaxis {
    * {
      fill: #EE9B80;
    }
  }
  .apexcharts-tooltip {
    display: flex!important;
    flex-direction: column!important;
    background: rgba(238, 155, 128, 1)!important;
    color: white;
  }
}
</style>
