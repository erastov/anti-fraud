<template>
  <div>
    <v-tooltip left>
      <v-btn class="mx-0" icon v-on:click="dialog = true" slot="activator">
        <v-icon color="red">lock</v-icon>
      </v-btn>
      Block
    </v-tooltip>
    <v-dialog v-model="dialog" max-width="500px" scrollable>
      <v-card>
        <v-card-title>
          Account block
          <v-spacer></v-spacer>
          <v-btn icon @click.native="dialog = false">
            <v-icon color="grey">close</v-icon>
          </v-btn>
        </v-card-title>
        <v-card-text>
          <h1 class="text-xs-center">ERASTOV FEDOR</h1>
          <h2 class="text-xs-center">Type: {{ item.type }} </h2>
          <h2 class="text-xs-center">Balance: {{ item.balance }} {{item.currency}}</h2>
        </v-card-text>
        <div style="padding-bottom: 15px;">
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn round color="red" dark @click="blockTrans">Block</v-btn>
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
    name: 'dialog-account-block',
    data: function () {
      return {
        dialog: false
      }
    },
    methods: {
      blockTrans: function () {
      }
    }
  }
</script>

<style scoped>

</style>
