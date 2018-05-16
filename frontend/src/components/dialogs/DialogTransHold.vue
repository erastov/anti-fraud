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
          Hold transaction
          <v-spacer></v-spacer>
          <v-btn icon @click.native="dialog = false">
            <v-icon color="grey">close</v-icon>
          </v-btn>
        </v-card-title>
        <v-card-text>
          <h2 class="text-xs-center">{{ id }}</h2>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn round color="orange" dark @click="holdTrans">Hold</v-btn>
          <v-btn round color="primary" flat @click="dialog=false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
  export default {
    props: ['id'],
    name: 'dialog-trans-info',
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
