<template lang="pug">
.chartwrapper
  h1 {{ albums }}
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
      series: [{
        name: 'TEAM 1',
        data: this.generateDayWiseTimeSeries(new Date('11 Feb 2017 GMT').getTime(), 20, {
          min: 10,
          max: 60
        })
      },
      {
        name: 'TEAM 2',
        data: this.generateDayWiseTimeSeries(new Date('11 Feb 2017 GMT').getTime(), 20, {
          min: 10,
          max: 60
        })
      },
      {
        name: 'TEAM 3',
        data: this.generateDayWiseTimeSeries(new Date('11 Feb 2017 GMT').getTime(), 30, {
          min: 10,
          max: 60
        })
      },
      {
        name: 'TEAM 4',
        data: this.generateDayWiseTimeSeries(new Date('11 Feb 2017 GMT').getTime(), 10, {
          min: 10,
          max: 60
        })
      },
      {
        name: 'TEAM 5',
        data: this.generateDayWiseTimeSeries(new Date('11 Feb 2017 GMT').getTime(), 30, {
          min: 10,
          max: 60
        })
      },
    ],
    chartOptions: {
      chart: {
        height: 350,
        type: 'scatter',
        zoom: {
          type: 'xy'
        }
      },
      dataLabels: {
        enabled: false
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
      yaxis: {
        max: 70
      },
      legend: {
        show: false
      }
    },
  }
},
  computed: {
    albums () {
      // let series = [{
      //   name: 'TEAM 1',
      //   data: this.generateDayWiseTimeSeries(new Date('11 Feb 2017 GMT').getTime(), 20, {
      //     min: 10,
      //     max: 60
      //   })
      // }]
      let series = []
      let albums = artistStore.currentArtist.albums
      for (const index in albums) {
        let album = albums[index]
        let test = {
          name: album.name
        }
        series.push(test)
        // console.log(this.generateDayWiseTimeSeries(new Date('11 Feb 2017 GMT').getTime(), 20, {
        //   min: 10,
        //   max: 60
        // }))
        
      }
      return series
    }
  },
  methods: {
    generateDayWiseTimeSeries: function(baseval, count, yrange) {
      var i = 0;
      var series = [];
      while (i < count) {
        var x = baseval;
        var y =
          Math.floor(Math.random() * (yrange.max - yrange.min + 1)) +
          yrange.min;

        series.push([x, y]);
        baseval += 86400000;
        i++;
      }
      return series;
    },
    dataPointSelectionHandler (event, chartContext, config) {
      console.log(chartContext);  
      console.log(config);  
    }
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
}
</style>
