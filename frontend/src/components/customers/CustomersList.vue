<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex xs12>
        <v-card>
        <v-card-title>
          Customers
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
            <td class="text-xs-left">{{ props.item.first_name }}</td>
            <td class="text-xs-left">{{ props.item.last_name }}</td>
            <td class="text-xs-left">{{ props.item.age }}</td>
            <td class="text-xs-left">{{ props.item.city }}</td>
            <td class="text-xs-left">{{ props.item.address }}</td>
            <td class="text-xs-left">{{ props.item.reputation_score }}</td>
            <td class="justify-center layout px-0">
              <v-btn icon class="mx-0" @click="deleteItem(props.item)">
                <v-icon color="blue">info</v-icon>
              </v-btn>
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
  import axios from 'axios'

  export default {
    name: 'Transactions',
    components: {
      SearchBarTrans
    },
    data: function () {
      return {
        headers: [
          {text: 'First name', value: 'first_name'},
          {text: 'Last name', value: 'last_name'},
          {text: 'Age', value: 'age'},
          {text: 'City', value: 'city'},
          {text: 'Address', value: 'address'},
          {text: 'Reputation score', value: 'reputation_score'},
          {text: 'Info', value: 'id', sortable: false}
        ],
        items: [],
        search: ''
      }
    },
    created() {
      axios.get('/api/customers/')
        .then(response => {
          let transactions = response.data
          this.items = transactions.reverse()
        })
    }
  }
</script>

<style scoped>

</style>
