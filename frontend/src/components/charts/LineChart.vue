<script>
  import VueCharts from 'vue-chartjs'

  const {reactiveProp} = VueCharts.mixins
  export default {
    name: 'line-chart',
    mixins: [reactiveProp],
    extends: VueCharts.Line,
    props: ['chartData'],
    data() {
      return {
        options: { //Chart.js options
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true
              },
              gridLines: {
                display: true
              }
            }],
            xAxes: [{
              display: false,
              gridLines: {
                display: false
              }
            }]
          },
          legend: {
            display: true
          },
          responsive: true,
          maintainAspectRatio: false
        }
      }
    },
    mounted() {
      this.renderChart(this.chartData, this.options)
    }
  }
</script>

