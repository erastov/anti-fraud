<script>
  import VueCharts from 'vue-chartjs'

  export default {
    name: 'line-chart',
    extends: VueCharts.Line,
    props: ['labels', 'datasets'],
    mounted() {
      this.renderChart({
        labels: this.labels,
        datasets: this.datasets
      }, {responsive: true, maintainAspectRatio: false})
    }
  }
</script>

<style scoped>

</style>
