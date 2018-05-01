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
      <v-flex xs12>
        <v-card>
          <line-chart style="height: 230px;" :chart-data="datacollection">
          </line-chart>
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
          <line-chart style="height: 240px;" :chart-data="datacollection2">
          </line-chart>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card>
          <line-chart style="height: 240px;" :chart-data="datacollection3">
          </line-chart>
        </v-card>
      </v-flex>
      <v-flex xs12>
        <v-data-table
          :headers="headers"
          :items="items"
          :disable-initial-sort="true"
          hide-actions
          class="elevation-1"
          dark
        >
          <template slot="items" slot-scope="props">
            <td>{{ props.item.time }}</td>
            <td>{{ props.item.amount }}</td>
            <td>{{ props.item.score }}</td>
            <td>
              <v-tooltip v-if="props.item.status === 'Approve'" right>
                <v-icon slot="activator" color="green">lens</v-icon>
                Approve
              </v-tooltip>
              <v-tooltip v-if="props.item.status === 'Hold'" right>
                <v-icon slot="activator" color="yellow">lens</v-icon>
                Hold
              </v-tooltip>
              <v-tooltip v-if="props.item.status === 'Lock'" right>
                <v-icon slot="activator" color="red">lens</v-icon>
                Lock
              </v-tooltip>
            </td>
          </template>
        </v-data-table>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import LineChart from './charts/LineChart'
  import Pusher from 'pusher-js'
  import axios from 'axios'

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
      datacollection2: null,
      datacollection3: null,
      timestamps: [],
      amounts: [],
      headers: [
        {text: 'Time', value: 'time'},
        {text: 'Amount', value: 'amount'},
        {text: 'Score', value: 'score'},
        {text: 'Status', value: 'status'}
      ],
      items: []
    }),
    methods: {
      fetchData() {
        channel.bind('my-event', data => {
          let transaction = data.message
          this.timestamps.splice(0, 1)
          this.timestamps.push(transaction.time)
          this.amounts.splice(0, 1)
          this.amounts.push(transaction.amount)
          this.items.splice(0, 1)
          this.items.unshift(transaction)

          this.datacollection = {
            labels: this.timestamps,
            datasets: [
              {
                label: 'Amount',
                backgroundColor: 'rgba(84, 242, 255, 0.5)',
                data: this.amounts
              }
            ]
          }
          this.datacollection2 = {
            labels: this.timestamps,
            datasets: [
              {
                label: 'Amount',
                backgroundColor: 'rgba(255, 84, 87, 0.5)',
                data: this.amounts
              }
            ]
          }
          this.datacollection3 = {
            labels: this.timestamps,
            datasets: [
              {
                label: 'Amount',
                backgroundColor: 'rgba(100, 255, 104, 0.5)',
                data: this.amounts
              }
            ]
          }
        })
      }
    },
    created() {
      this.fetchData()
      axios.get('/api/transactions/')
        .then(response => {
          let transactions = response.data
          this.timestamps = transactions.map(t => t.time)
          this.amounts = transactions.map(t => t.amount)
          this.items = transactions.reverse().slice(0, 3)

          this.datacollection = {
            labels: this.timestamps,
            datasets: [
              {
                label: 'Amount',
                backgroundColor: 'rgba(84, 242, 255, 0.5)',
                data: this.amounts
              }
            ]
          }
          this.datacollection2 = {
            labels: this.timestamps,
            datasets: [
              {
                label: 'Amount',
                backgroundColor: 'rgba(255, 84, 87, 0.5)',
                data: this.amounts
              }
            ]
          }
          this.datacollection3 = {
            labels: this.timestamps,
            datasets: [
              {
                label: 'Amount',
                backgroundColor: 'rgba(100, 255, 104, 0.5)',
                data: this.amounts
              }
            ]
          }
        })
    }
  }
</script>

<style scoped>

</style>
