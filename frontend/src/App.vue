<style>
  #login {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    z-index: 100;
    background-color: #fff;
  }

  .btn-icon {
    padding: 4px;
  }

  @font-face {
    font-family: MuseoSansCyrl;
    src: url(/static/fonts/MuseoSansCyrl_500.otf);
  }

  .my-font {
    font-family: MuseoSansCyrl;
  }
</style>
<template>
  <v-app id="inspire">
    <v-navigation-drawer
      clipped
      fixed
      v-model="drawer"
      app
      dark
    >
      <v-list dense>
        <v-list-tile href="#/dashboard">
          <v-list-tile-action>
            <v-icon>dashboard</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Dashboard</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile href="#/transactions">
          <v-list-tile-action>
            <v-icon>payment</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Transactions</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile href="#/customers">
          <v-list-tile-action>
            <v-icon>account_box</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Customers</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile href="#/settings">
          <v-list-tile-action>
            <v-icon>settings</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Settings</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar app fixed clipped-left dark>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>ANTIFRAUD</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu offset-y>
        <v-btn class="my-font" dark flat slot="activator" style="color: #FF8C00">
          <v-icon class="btn-icon">account_circle</v-icon>
          {{username}}
        </v-btn>
        <v-list>
          <v-list-tile @click="logOut">
            <v-list-tile-title class="my-font">Log-Out</v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-menu>
    </v-toolbar>
    <v-content class="white">
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  import router from '@/router'
  import axios from 'axios'

  let currentTitle = {}

  router.afterEach(function (to) {
    if (to.meta && to.meta.title) {
      currentTitle.value = to.meta.title
    }
  })

  export default {
    data() {
      return {
        appName: 'ANTIFRAUD',
        drawer: true,
        get username() {
          return localStorage.getItem('_username')
        }
      }
    },
    methods: {
      logOut: function (event) {
        axios.get('/api/logout')
        this.$router.push('/login')
      }
    }
  }
</script>

<style>
</style>
