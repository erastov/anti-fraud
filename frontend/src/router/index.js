import Vue from 'vue'
import Router from 'vue-router'
import Forbidden from '@/components/Forbidden'
import NotFound from '@/components/NotFound'
import Login from '@/components/auth/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/'
      // meta: {
      //   roles: ['authenticated']
      // }
    },
    {
      path: '/login',
      component: Login
    },
    {
      path: '/forbidden',
      component: Forbidden
    },
    {
      path: '*',
      component: NotFound
    }
  ]
})
