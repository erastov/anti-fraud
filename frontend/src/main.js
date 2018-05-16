// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'
import VueAxios from 'vue-axios'
import Axios from 'axios'
import Auth from './auth'
import '../node_modules/vuetify/dist/vuetify.min.css'
import * as VueGoogleMaps from 'vue2-google-maps'

Axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
Axios.defaults.xsrfCookieName = 'csrftoken'

Vue.config.productionTip = false
Vue.use(Vuetify)
Vue.use(VueAxios, Axios)
Vue.use(Auth, {
  loginUrl: '/login',
  forbiddenUrl: '/forbidden',
  logoutUrl: '/logout',
  router
})

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyAZ0SKWkM3WjBIK9Ynumd9wEvg8xYdFQ5o',
    libraries: 'places' // This is required if you use the Autocomplete plugin
    // OR: libraries: 'places,drawing'
    // OR: libraries: 'places,drawing,visualization'
    // (as you require)

    // If you want to set the version, you can do so:
    // v: '3.26',
  }

  // If you intend to programmatically custom event listener code
  // (e.g. `this.$refs.gmap.$on('zoom_changed', someFunc)`)
  // instead of going through Vue templates (e.g. `<GmapMap @zoom_changed="someFunc">`)
  // you might need to turn this on.
  // autobindAllEvents: false,

  // If you want to manually install components, e.g.
  // import {GmapMarker} from 'vue2-google-maps/src/components/marker'
  // Vue.component('GmapMarker', GmapMarker)
  // then disable the following:
  // installComponents: true,
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})
