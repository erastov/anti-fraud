<template>
  <v-container fluid grid-list-md>
    <v-layout row wrap>
      <v-flex xs3>
        <v-card color="blue-grey darken-2" class="white--text">
          <v-card-title>
            <div class="headline">Сегодня: 30541 транз.</div>
            <div>Прогноз: 47540 транз.</div>
          </v-card-title>
        </v-card>
      </v-flex>
      <v-flex xs3>
        <v-card color="cyan darken-2" class="white--text">
          <v-card-title>
            <div class="headline">Месяц: 1 млн. транз.</div>
            <v-spacer></v-spacer>
            <div>Прогноз: 3 млн. транз.</div>
          </v-card-title>
        </v-card>
      </v-flex>
      <v-flex xs3>
        <v-card color="purple" class="white--text">
          <v-card-title>
            <div class="headline">Сегодня: 300400 ₽</div><v-spacer></v-spacer>
            <div>Прогноз: 500410 ₽</div>
          </v-card-title>
        </v-card>
      </v-flex>
      <v-flex xs3>
        <v-card color="red lighten-1" class="white--text">
          <v-card-title>
             <div class="headline">Месяц: 4 млн. ₽</div><v-spacer></v-spacer>
            <div>Прогноз: 11 млн. ₽</div>
          </v-card-title>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card>
          <line-chart style="height: 240px;"
                      :datasets="chartData"
                      :labels="labels">
          </line-chart>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card>
          <line-chart style="height: 240px;"
                      :datasets="chartData2"
                      :labels="labels">
          </line-chart>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card>
          <line-chart style="height: 240px;"
                      :datasets="chartData3"
                      :labels="labels">
          </line-chart>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card>
          <line-chart style="height: 240px;"
                      :datasets="chartData4"
                      :labels="labels">
          </line-chart>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card>
          <line-chart style="height: 240px;"
                      :datasets="chartData5"
                      :labels="labels">
          </line-chart>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card>
          <line-chart style="height: 240px;"
                      :datasets="chartData6"
                      :labels="labels">
          </line-chart>
        </v-card>
      </v-flex>
      <v-flex xs12>
        <v-data-table
          :headers="headers"
          :items="items"
          hide-actions
          class="elevation-1"
          dark
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
  import LineChart from './charts/LineChart'

  export default {
    name: "dashboard",
    components: {LineChart},
    data: () => ({
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
      chartData: [
        {
          label: 'Кол-во транзакций в час',
          backgroundColor: '#11f8f1',
          data: [40, 39, 10, 40, 39, 80, 40]
        }
      ],
      chartData2: [
        {
          label: 'Кол-во транзакций в сутки',
          backgroundColor: '#4ae4f8',
          data: [40, 39, 10, 40, 39, 80, 40]
        }
      ],
      chartData3: [
        {
          label: 'Кол-во транзакций в месяц',
          backgroundColor: '#13c3f8',
          data: [40, 39, 10, 40, 39, 80, 40]
        }
      ],
      chartData4: [
        {
          label: 'Сумма транзакций в час',
          backgroundColor: '#c4f8c8',
          data: [40, 39, 10, 40, 39, 80, 40]
        }
      ],
      chartData5: [
        {
          label: 'Сумма транзакций в сутки',
          backgroundColor: '#94f8ae',
          data: [40, 39, 10, 40, 39, 80, 40]
        }
      ],
      chartData6: [
        {
          label: 'Сумма транзакций в месяц',
          backgroundColor: '#1af881',
          data: [40, 39, 10, 40, 39, 80, 40]
        }
      ],
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
        }
      ]
    })
  }
</script>

<style scoped>

</style>
