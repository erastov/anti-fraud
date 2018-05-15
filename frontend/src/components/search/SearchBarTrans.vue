<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex xs3>
        <v-text-field
          label=""
          v-model="subject"
          @keyup.enter="submit"
        ></v-text-field>
      </v-flex>
      <v-flex xs2>
        <v-text-field
          label="Ticket"
          v-model="ticket"
          @keyup.enter="submit"
        ></v-text-field>
      </v-flex>
      <v-flex xs3>
        <v-text-field
          label="Description"
          v-model="description"
          @keyup.enter="submit"
        ></v-text-field>
      </v-flex>
      <v-flex xs4>
        <v-select
          label="Owners (e-mail)"
          chips
          tags
          append-icon=""
          clearable
          v-model="owners"
          :rules="ownersRules"
        >
          <template slot="selection" slot-scope="data">
            <v-chip
              close
              @input="remove(data.item)"
              :selected="data.selected"
            >
              {{ data.item }}
            </v-chip>
          </template>
        </v-select>
      </v-flex>
      <v-flex xs3>
        <v-select
          label="CA"
          v-model="ca"
          :items="caChoices"
        ></v-select>
      </v-flex>
      <v-flex xs3>
        <v-select
          label="Type"
          v-model="type"
          item-text="name"
          item-value="id"
          :items="types"
        ></v-select>
      </v-flex>
      <v-flex xs2>
        <v-select
          label="Status"
          v-model="status"
          :items="statusChoices"
        ></v-select>
      </v-flex>
      <v-flex xs2>
        <v-select
          label="Revoked"
          v-model="revoked"
          :items="booleanChoices"
          ></v-select>
      </v-flex>
      <v-flex xs2>
        <v-select
          label="Private key"
          v-model="privateKey"
          :items="booleanChoices"
        ></v-select>
      </v-flex>
      <v-flex xs1>
        <v-subheader>Valid from:</v-subheader>
      </v-flex>
      <v-flex xs2>
        <v-menu
          lazy
          :close-on-content-click="false"
          v-model="menu"
          transition="scale-transition"
          offset-y
          full-width
          :nudge-right="40"
          max-width="290px"
          min-width="290px"
        >
          <v-text-field
            slot="activator"
            label="Min"
            v-model="MinValidFrom"
            prepend-icon="event"
            clearable
          ></v-text-field>
          <v-date-picker v-model="MinValidFrom" no-title scrollable actions autosave>
          </v-date-picker>
        </v-menu>
      </v-flex>
      <v-flex xs2>
        <v-menu
          lazy
          :close-on-content-click="false"
          v-model="menu2"
          transition="scale-transition"
          offset-y
          full-width
          :nudge-right="40"
          max-width="290px"
          min-width="290px"
        >
          <v-text-field
            slot="activator"
            label="Max"
            v-model="MaxValidFrom"
            prepend-icon="event"
            clearable
          ></v-text-field>
          <v-date-picker v-model="MaxValidFrom" no-title scrollable actions autosave>
          </v-date-picker>
        </v-menu>
      </v-flex>
      <v-flex xs1>
        <v-subheader>Valid to:</v-subheader>
      </v-flex>
      <v-flex xs2>
        <v-menu
          lazy
          :close-on-content-click="false"
          v-model="menu3"
          transition="scale-transition"
          offset-y
          full-width
          :nudge-right="40"
          max-width="290px"
          min-width="290px"
        >
          <v-text-field
            slot="activator"
            label="Min"
            v-model="MinValidTo"
            prepend-icon="event"
            clearable
          ></v-text-field>
          <v-date-picker v-model="MinValidTo" no-title scrollable actions autosave>
          </v-date-picker>
        </v-menu>
      </v-flex>
      <v-flex xs2>
        <v-menu
          lazy
          :close-on-content-click="false"
          v-model="menu4"
          transition="scale-transition"
          offset-y
          full-width
          :nudge-right="40"
          max-width="290px"
          min-width="290px"
        >
          <v-text-field
            slot="activator"
            label="Max"
            v-model="MaxValidTo"
            prepend-icon="event"
            clearable
          ></v-text-field>
          <v-date-picker v-model="MaxValidTo" no-title scrollable actions autosave>
          </v-date-picker>
        </v-menu>
      </v-flex>
      <v-flex>
        <v-btn flat
               round
               @click="reset"
        >reset
        </v-btn>
        <v-btn
          small
          fab
          @click="submit"
          color="primary"
        >
          <v-icon>search</v-icon>
        </v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'search-bar-trans',
    data: function () {
      return {
        subject: '',
        ticket: '',
        description: '',
        owners: [],
        MinValidFrom: '',
        MaxValidFrom: '',
        MinValidTo: '',
        MaxValidTo: '',
        menu: false,
        menu2: false,
        menu3: false,
        menu4: false,
        statusChoices: [
          {'value': '', 'text': 'All'},
          {'value': 0, 'text': 'Active'},
          {'value': 1, 'text': 'Not active yet'},
          {'value': 2, 'text': 'Expired'}
        ],
        caChoices: [
          {'value': '', 'text': 'All'},
          {'value': 0, 'text': 'Root CA'},
          {'value': 1, 'text': 'Intermediate CA'},
          {'value': 2, 'text': 'Client cert'}
        ],
        booleanChoices: [
          {'value': '', 'text': 'All'},
          {'value': true, 'text': 'Yes'},
          {'value': false, 'text': 'No'}
        ],
        types: [{'id': '', 'name': 'All'}],
        type: '',
        status: '',
        revoked: '',
        ca: '',
        privateKey: '',
        ownersRules: [
          (list) => {
            let listIsValid = list.every((v) => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v))
            return listIsValid || 'E-mail must be valid'
          }
        ]
      }
    },
    methods: {
      reset: function () {
        this.subject = ''
        this.MinValidFrom = ''
        this.MaxValidFrom = ''
        this.MinValidTo = ''
        this.MaxValidTo = ''
        this.type = ''
        this.status = ''
        this.revoked = ''
        this.ca = ''
        this.privateKey = ''
        this.owners = []
        this.ticket = ''
        this.description = ''
        this.$emit('reset')
      },
      submit: function () {
        var arr = [
          this.type,
          this.revoked,
          this.subject,
          this.MinValidFrom || '',
          this.MaxValidFrom || '',
          this.MinValidTo || '',
          this.MaxValidTo || '',
          this.privateKey,
          this.ca,
          this.status,
          this.owners,
          this.ticket,
          this.description
        ]
        if (!arr.every(x => x.length === 0)) {
          var queryParams = [
            `type=${this.type}`,
            `&revoked=${this.revoked}`,
            `&subject=${this.subject}`,
            `&min_valid_from=${this.MinValidFrom || ''}`,
            `&max_valid_from=${this.MaxValidFrom || ''}`,
            `&min_valid_to=${this.MinValidTo || ''}`,
            `&max_valid_to=${this.MaxValidTo || ''}`,
            `&has_private_key=${this.privateKey}`,
            `&ca=${this.ca}`,
            `&status=${this.status}`,
            `&ticket=${this.ticket}`,
            `&description=${this.description}`
          ]
          let i = 0
          for (i = 0; i < this.owners.length; i += 1) {
            queryParams.push(`&owners=${this.owners[i]}`)
          }
          this.$emit('submit', queryParams.join(''))
        }
      },
      remove: function (item) {
        this.owners.splice(this.owners.indexOf(item), 1)
        this.owners = [...this.owners]
      }
    },
    created: function () {
      axios.get('/api/types/')
        .then(response => {
          this.types = this.types.concat(response.data)
        })
    }
  }
</script>

