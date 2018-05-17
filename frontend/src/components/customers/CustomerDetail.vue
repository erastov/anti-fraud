<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex xs4>
        <v-card>
          <v-card-media src="https://i.pinimg.com/originals/e1/3d/c9/e13dc9a0bf47cf259b74b8814bbd24af.png"
                        height="200px">
            <v-layout column class="media">
              <v-spacer></v-spacer>
              <h1 class="text-xs-center" style="padding-bottom: 15px; color: black;">ERASTOV FEDOR</h1>
            </v-layout>
          </v-card-media>
          <v-list two-line>
            <v-list-tile @click="">
              <v-list-tile-action>
                <v-icon color="indigo">phone</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>(650) 555-1234</v-list-tile-title>
                <v-list-tile-sub-title>Mobile</v-list-tile-sub-title>
              </v-list-tile-content>
              <v-list-tile-action>
                <v-icon>chat</v-icon>
              </v-list-tile-action>
            </v-list-tile>
            <v-list-tile @click="">
              <v-list-tile-action></v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>(323) 555-6789</v-list-tile-title>
                <v-list-tile-sub-title>Work</v-list-tile-sub-title>
              </v-list-tile-content>
              <v-list-tile-action>
                <v-icon>chat</v-icon>
              </v-list-tile-action>
            </v-list-tile>
            <v-list-tile @click="">
              <v-list-tile-action>
                <v-icon color="indigo">location_on</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>Studencheskaya 33k8</v-list-tile-title>
                <v-list-tile-sub-title>Russia, Moscow</v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-divider inset></v-divider>
            <v-list-tile @click="">
              <v-list-tile-action>
                <v-icon color="indigo">face</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>21</v-list-tile-title>
                <v-list-tile-sub-title>Age</v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile @click="">
              <v-list-tile-action>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>Male</v-list-tile-title>
                <v-list-tile-sub-title>Gender</v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile @click="">
              <v-list-tile-action>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>Single</v-list-tile-title>
                <v-list-tile-sub-title>Marital status</v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-divider inset></v-divider>
            <v-list-tile @click="">
              <v-list-tile-action>
                <v-icon color="red">pan_tool</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>10</v-list-tile-title>
                <v-list-tile-sub-title>Reputation score</v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-card>
      </v-flex>
      <v-flex xs8>
        <v-container grid-list-md text-xs-center>
          <v-layout row wrap>
            <v-flex xs12>
              <v-card>
                <line-chart style="height: 230px;" :chart-data="datacollection">
                </line-chart>
              </v-card>
            </v-flex>
            <v-flex xs12>
              <v-card>
                <GmapMap
                  :center="{lat: 55.751244, lng: 37.618423}"
                  :zoom="6"
                  map-type-id="terrain"
                  style="width: auto; height: 220px;"
                >
                  <GmapCircle
                    :center="{lat: 55.751244, lng: 37.618423}"
                    :radius="70000"
                    :options="{
                    strokeColor: '#FF0000',
                    strokeOpacity: 0.8,
                    strokeWeight: 2,
                    fillColor: '#FF0000',
                    fillOpacity: 0.35
                    }"
                  ></GmapCircle>
                  <GmapCircle
                    :center="{lat: 56.2965039, lng: 43.9360589}"
                    :radius="10000"
                    :options="{
                    strokeColor: '#FF0000',
                    strokeOpacity: 0.8,
                    strokeWeight: 2,
                    fillColor: '#FF0000',
                    fillOpacity: 0.35
                    }"
                  ></GmapCircle>
                </GmapMap>
              </v-card>
            </v-flex>
            <v-flex xs12>
              <v-card>
                <v-data-table
                  :headers="headers"
                  :items="items"
                  hide-actions
                  :disable-initial-sort="true"
                  class="elevation-1"
                >
                  <template slot="items" slot-scope="props">
                    <td>
                      <v-tooltip v-if="props.item.status === 'Active'" right>
                        <v-icon slot="activator" color="green">lens</v-icon>
                        Active
                      </v-tooltip>
                      <v-tooltip v-if="props.item.status === 'Frozen'" right>
                        <v-icon slot="activator" color="yellow">lens</v-icon>
                        Frozen
                      </v-tooltip>
                      <v-tooltip v-if="props.item.status === 'Block'" right>
                        <v-icon slot="activator" color="red">lens</v-icon>
                        Block
                      </v-tooltip>
                    </td>
                    <td class="text-xs-left">{{ props.item.type }}</td>
                    <td class="text-xs-left">{{ props.item.currency }}</td>
                    <td class="text-xs-left">{{ props.item.balance }}</td>
                    <td class="text-xs-left">{{ props.item.credit }}</td>
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
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import LineChart from '../charts/LineChart'
  import DialogTransInfo from '../dialogs/DialogTransInfo'
  import DialogTransBlock from '../dialogs/DialogTransBlock'
  import DialogTransHold from '../dialogs/DialogTransHold'
  import axios from 'axios'

  export default {
    name: 'CustomerDetail',
    components: {
      LineChart,
      DialogTransInfo,
      DialogTransBlock,
      DialogTransHold
    },
    data: function () {
      return {
        id: this.$route.params.id,
        datacollection: null,
        timestamps: [],
        amounts: [],
        headers: [
          {text: 'Status', value: 'status'},
          {text: 'Type', value: 'type'},
          {text: 'Currency', value: 'currency'},
          {text: 'Balance', value: 'balance'},
          {text: 'Credit', value: 'credit'},
          {text: 'Actions', value: 'id'}
        ],
        items: []
      }
    },
    created() {
      axios.get('/api/transactions/')
        .then(response => {
          let transactions = response.data
          this.timestamps = transactions.map(t => t.time)
          this.amounts = transactions.map(t => t.amount)

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
        })
      axios.get('/api/accounts/')
        .then(response => {
          this.items = response.data
        })
    }
  }
</script>

<style scoped>

</style>
