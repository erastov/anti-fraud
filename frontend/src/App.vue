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
    <v-toolbar style="background-color: #2D3540" dark app fixed clipped-left>
      <a href="#/">
        <img style="height: 45px; margin-top: 2px;"
             src="/static/imgs/certm_horiz.png"
             alt="logo">
      </a>
      <v-btn class="my-font" flat dark href="#/generate_csr">
        <v-icon class="btn-icon">dashboard</v-icon>
        Dashboard
      </v-btn>
      <v-btn class="my-font" flat dark href="#/import">
        <v-icon class="btn-icon">cloud_upload</v-icon>
        Import
      </v-btn>
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
        <router-view style="max-width: 1200px; color:black"></router-view>
      </v-container>
      <notifications position="bottom left" group="foo"/>
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
        drawer: false,
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
