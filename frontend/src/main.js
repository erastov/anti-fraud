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

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
