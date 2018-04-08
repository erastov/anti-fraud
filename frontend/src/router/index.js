import Vue from 'vue'
import Router from 'vue-router'
import Forbidden from '@/components/Forbidden'
import NotFound from '@/components/NotFound'
import Login from '@/components/auth/Login'
import Dashboard from '@/components/Dashboard'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/dashboard'
      // meta: {
      //   roles: ['authenticated']
      // }
    },
    {
      path: '/login',
      component: Login
    },
    {
      path: '/dashboard',
      component: Dashboard
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
