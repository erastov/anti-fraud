<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
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
              <dialog-trans-hold :id="props.item.id"></dialog-trans-hold>
              <dialog-trans-block :id="props.item.id"></dialog-trans-block>
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
  </v-container>
</template>

<script>
  import SearchBarTrans from '../search/SearchBarTrans'
  import DialogTransInfo from '../dialogs/DialogTransInfo'
  import DialogTransBlock from '../dialogs/DialogTransBlock'
  import DialogTransHold from '../dialogs/DialogTransHold'
  import axios from 'axios'

  export default {
    name: 'Transactions',
    components: {
      SearchBarTrans,
      DialogTransInfo,
      DialogTransBlock,
      DialogTransHold
    },
    data: function () {
      return {
        headers: [
          {text: 'Status', value: 'status', sortable: false},
          {text: 'Time', value: 'time'},
          {text: 'Source', value: 'source_customer'},
          {text: 'Destination', value: 'destination_customer'},
          {text: 'Amount', value: 'amount'},
          {text: 'Score', value: 'score'},
          {text: 'Actions', value: 'id', sortable: false}
        ],
        items: [],
        search: ''
      }
    },
    created() {
      axios.get('/api/transactions/')
        .then(response => {
          let transactions = response.data
          this.items = transactions.reverse()
        })
    }
  }
</script>

<style scoped>

</style>
