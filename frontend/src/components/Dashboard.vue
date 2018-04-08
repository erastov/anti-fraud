<template>
  <v-container  fluid grid-list-md>
    <v-layout row wrap>
      <v-flex xs4>
        <line-chart style="height: 95%;"></line-chart>
      </v-flex>
      <v-flex xs4>
        <line-chart style="height: 95%;"></line-chart>
      </v-flex>
      <v-flex xs4>
        <line-chart style="height: 95%;"></line-chart>
      </v-flex>
      <v-flex xs4>
        <line-chart style="height: 95%;"></line-chart>
      </v-flex>
      <v-flex xs4>
        <line-chart style="height: 95%;"></line-chart>
      </v-flex>
      <v-flex xs4>
        <line-chart style="height: 95%;"></line-chart>
      </v-flex>
      <v-flex xs12>
        <v-data-table
          :headers="headers"
          :items="items"
          hide-actions
          class="elevation-1"
        >
          <template slot="items" slot-scope="props">
            <td>{{ props.item.name }}</td>
            <td class="text-xs-right">{{ props.item.calories }}</td>
            <td class="text-xs-right">{{ props.item.fat }}</td>
            <td class="text-xs-right">{{ props.item.carbs }}</td>
            <td class="text-xs-right">{{ props.item.protein }}</td>
            <td class="text-xs-right">{{ props.item.iron }}</td>
          </template>
        </v-data-table>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import Vue from 'vue'
  import VueCharts from 'vue-chartjs'

  Vue.component('line-chart', {
    extends: VueCharts.Line,
    mounted() {
      this.renderChart({
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#f87979',
            data: [40, 39, 10, 40, 39, 80, 40]
          }
        ]
      }, {responsive: true, maintainAspectRatio: false})
    }

  })

  export default {
    name: "dashboard",
    data: () => ({
      chartData: {},
      headers: [
        {
          text: 'Dessert (100g serving)',
          align: 'left',
          sortable: false,
          value: 'name'
        },
        {text: 'Calories', value: 'calories'},
        {text: 'Fat (g)', value: 'fat'},
        {text: 'Carbs (g)', value: 'carbs'},
        {text: 'Protein (g)', value: 'protein'},
        {text: 'Iron (%)', value: 'iron'}
      ],
      items: [
        {
          value: false,
          name: 'Frozen Yogurt',
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          iron: '1%'
        },
        {
          value: false,
          name: 'Ice cream sandwich',
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: '1%'
        },
        {
          value: false,
          name: 'Eclair',
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          iron: '7%'
        },
        {
          value: false,
          name: 'Cupcake',
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          iron: '8%'
        }
      ]
    })
  }
</script>

<style scoped>

</style>
