<template>
  <div>
    <v-tooltip left>
      <v-btn class="mx-0" icon v-on:click="dialog = true" slot="activator">
        <v-icon color="blue">info</v-icon>
      </v-btn>
      Detail
    </v-tooltip>
    <v-dialog v-model="dialog" max-width="900px">
      <v-card>
        <v-card-title>
          Account info
          <v-spacer></v-spacer>
          <v-btn icon @click.native="dialog = false">
            <v-icon color="grey">close</v-icon>
          </v-btn>
        </v-card-title>
        <v-card-text>
            <v-layout row wrap>
              <v-flex xs12>
                <line-chart style="height: 240px;" :chart-data="datacollection">
                </line-chart>
              </v-flex>
              <v-flex xs12>
                <v-card>
                  <v-card-title>
                    Transactions
                    <v-spacer></v-spacer>
                    <v-text-field
                      v-model="search"
                      append-icon="search"
                      label="Search"
                      single-line
                      hide-details
                    ></v-text-field>
                  </v-card-title>
                  <v-data-table
                    :headers="headers"
                    :items="items"
                    :search="search"
                    :disable-initial-sort="true"
                    class="elevation-1"
                  >
                    <template slot="items" slot-scope="props">
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
                      <td class="text-xs-left">{{ props.item.time }}</td>
                      <td class="text-xs-left">{{ props.item.source_customer }}</td>
                      <td class="text-xs-left">{{ props.item.destination_customer }}</td>
                      <td class="text-xs-left">{{ props.item.amount }}</td>
                      <td class="text-xs-left">{{ props.item.score }}</td>
                      <td class="justify-center layout px-0">
                        <dialog-trans-hold :item="props.item"></dialog-trans-hold>
                        <dialog-trans-block :item="props.item"></dialog-trans-block>
                        <dialog-trans-info :id="props.item.id"></dialog-trans-info>
                      </td>
                    </template>
                    <v-alert slot="no-results" :value="true" color="error" icon="warning">
                      Your search for "{{ search }}" found no results.
                    </v-alert>
                  </v-data-table>
                </v-card>
              </v-flex>
            </v-layout>

        </v-card-text>
        <div style="padding-bottom: 15px;">
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn round color="orange" dark @click="holdTrans">Hold</v-btn>
            <v-btn round color="red" dark @click="blockTrans">Block</v-btn>
            <v-btn round color="primary" flat @click="dialog=false">Close</v-btn>
          </v-card-actions>
        </div>
      </v-card>
    </v-dialog>
    <v-snackbar
      :bottom="true"
      :left="true"
      :timeout="5000"
      :color="color"
      v-model="snackbar"
    >
      {{ text }}
      <v-btn dark flat @click.native="snackbar = false">Close</v-btn>
    </v-snackbar>
  </div>
</template>

<script>
  import LineChart from '../charts/LineChart'
  import DialogTransInfo from '../dialogs/DialogTransInfo'
  import DialogTransBlock from '../dialogs/DialogTransBlock'
  import DialogTransHold from '../dialogs/DialogTransHold'
  import axios from 'axios'

  export default {
    props: ['id'],
    components: {
      LineChart,
      DialogTransInfo,
      DialogTransBlock,
      DialogTransHold
    },
    name: 'dialog-account-info',
    data: function () {
      return {
        color: 'green',
        text: '',
        snackbar: false,
        dialog: false,
        time: '2018-04-24T17:52:51.557153Z',
        score: '90',
        status: 'Approve',
        source_account: '8458b586-c37d-40e4-a91d-922704545806',
        destination_account: 'c488f127-4ba8-4d66-a113-3dd1ff96688a',
        datacollection: null,
        timestamps: [],
        amounts: [],
        items: [],
        search: '',
        headers: [
          {text: 'Status', value: 'status', sortable: false},
          {text: 'Time', value: 'time'},
          {text: 'Source', value: 'source_customer'},
          {text: 'Destination', value: 'destination_customer'},
          {text: 'Amount', value: 'amount'},
          {text: 'Score', value: 'score'},
          {text: 'Actions', value: 'id', sortable: false}
        ]
      }
    },
    methods: {
      blockTrans: function () {
        this.text = 'Account successfully blocked'
        this.snackbar = true
      },
      holdTrans: function () {
      }
    },
    created() {
      axios.get('/api/transactions/')
        .then(response => {
          let transactions = response.data
          this.timestamps = transactions.map(t => t.time)
          this.amounts = transactions.map(t => t.amount)
          this.items = transactions.reverse()

          this.datacollection = {
            labels: this.timestamps,
            datasets: [
              {
                label: 'Amount (by hour)',
                backgroundColor: 'rgba(84, 242, 255, 0.5)',
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

