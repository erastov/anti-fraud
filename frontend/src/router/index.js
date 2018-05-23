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
      redirect: '/dashboard',
      meta: {
        roles: ['authenticated']
      }
    },
    {
      path: '/login',
      component: Login
    },
    {
      path: '/dashboard',
      component: Dashboard,
      meta: {
        roles: ['authenticated']
      }
    },
    {
      path: '/transactions',
      component: TransactionsList,
      meta: {
        roles: ['authenticated']
      }
    },
    {
      path: '/transaction',
      component: TransactionDetail,
      meta: {
        roles: ['authenticated']
      }
    },
    {
      path: '/customers',
      component: CustomersList,
      meta: {
        roles: ['authenticated']
      }
    },
    {
      path: '/customers/:id',
      component: CustomerDetail,
      meta: {
        roles: ['authenticated']
      }
    },
    {
      path: '/settings',
      component: SettingsPanel,
      meta: {
        roles: ['authenticated']
      }
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
