<template>
  <v-container fluid grid-list-md>
    <v-layout row wrap>
      <v-flex xs3>
        <v-card color="blue-grey darken-2" class="white--text">
          <v-card-title>
            <div class="headline">Сегодня: 301 транз.</div>
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
            <div class="headline">Сегодня: 300400 ₽</div>
            <v-spacer></v-spacer>
            <div>Прогноз: 500410 ₽</div>
          </v-card-title>
        </v-card>
      </v-flex>
      <v-flex xs3>
        <v-card color="red lighten-1" class="white--text">
          <v-card-title>
            <div class="headline">Месяц: 4 млн. ₽</div>
            <v-spacer></v-spacer>
            <div>Прогноз: 11 млн. ₽</div>
          </v-card-title>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card>
          <line-chart style="height: 240px;"></line-chart>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card>
          <line-chart style="height: 240px;"></line-chart>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card>
          <line-chart style="height: 240px;" :chart-data="datacollection">
          </line-chart>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card>
          <line-chart style="height: 240px;"></line-chart>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card>
          <line-chart style="height: 240px;"></line-chart>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card>
          <line-chart style="height: 240px;"></line-chart>
        </v-card>
      </v-flex>
      <v-flex xs12>
        <v-data-table
          :headers="headers"
          :items="items"
          hide-actions
          hide-headers
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
  import Pusher from 'pusher-js'

  const socket = new Pusher('16b0026a0399f224c710', {
    cluster: 'eu',
    encrypted: true
  })
  const channel = socket.subscribe('my-channel')

  export default {
    name: "dashboard",
    components: {LineChart},
    data: () => ({
      datacollection: null,
      timestamps: [],
      amounts: [],
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
    }),
    methods: {
      fetchData() {
        channel.bind('my-event', data => {
          let transaction = data.message
          this.timestamps.push(transaction.time)
          this.amounts.push(transaction.amount)

          //The Chart's dataset is updated with the latest data gotten from Pusher
          this.datacollection = {
            labels: this.timestamps,
            datasets: [
              {
                label: 'Amount',
                backgroundColor: '#11f8f1',
                data: this.amounts
              }
            ]
          }
        })
      }
    },
    created () {
      this.fetchData()
    }
  }
</script>

<style scoped>

</style>
