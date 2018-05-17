<template>
  <div>
    <v-tooltip left>
      <v-btn class="mx-0" icon v-on:click="dialog = true" slot="activator">
        <v-icon color="orange">report</v-icon>
      </v-btn>
      Hold
    </v-tooltip>
    <v-dialog v-model="dialog" max-width="500px" scrollable>
      <v-card>
        <v-card-title>
          Transaction hold
          <v-spacer></v-spacer>
          <v-btn icon @click.native="dialog = false">
            <v-icon color="grey">close</v-icon>
          </v-btn>
        </v-card-title>
        <v-card-text>
          <h2 class="text-xs-center">{{ item.source_customer }} -> {{ item.destination_customer }}</h2>
          <h1 class="text-xs-center">{{ item.amount }}</h1>
        </v-card-text>
        <div style="padding-bottom: 15px;">
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn round color="orange" dark @click="holdTrans">Hold</v-btn>
            <v-btn round color="primary" flat @click="dialog=false">Close</v-btn>
          </v-card-actions>
        </div>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
  export default {
    props: ['item'],
    name: 'dialog-trans-hold',
    data: function () {
      return {
        dialog: false
      }
    },
    methods: {
      holdTrans: function () {
      }
    }
  }
</script>

<style scoped>

</style>
