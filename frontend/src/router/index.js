import Vue from 'vue'
import Router from 'vue-router'
import Forbidden from '@/components/Forbidden'
import NotFound from '@/components/NotFound'
import Login from '@/components/auth/Login'
import Dashboard from '@/components/Dashboard'
import TransactionsList from '@/components/transactions/TransactionsList'
import TransactionDetail from '@/components/transactions/TransactionDetail'
import CustomerDetail from '@/components/customers/CustomerDetail'
import CustomersList from '@/components/customers/CustomersList'
import SettingsPanel from '@/components/settings/SettingsPanel'

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
      path: '/transactions',
      component: TransactionsList
    },
    {
      path: '/transaction',
      component: TransactionDetail
    },
    {
      path: '/customers',
      component: CustomersList
    },
    {
      path: '/customers/:id',
      component: CustomerDetail
    },
    {
      path: '/settings',
      component: SettingsPanel
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
