// import Authorize from './authorize.js'
// import IsAuthorizedDirective from './directive.js'
// import IsAuthorizedComponent from './component.js'

import axios from 'axios'

class Authorize {
  constructor () {
    this.identity_ = null
  }

  identity () {
    let promise = null
    if (this.identity_ != null) {
      promise = new Promise((resolve, reject) => {
        resolve(this.identity_)
      })
    } else {
      promise = axios.get('api/user-settings/')
        .then(response => {
          this.identity_ = response.data
        })
    }
    return promise
  }

  isInAnyRole (roles) {
    for (let i = 0; i < roles.length; ++i) {
      if (this.identity_.roles[roles[i]]) {
        return true
      }
    }
    return false
  }

  login (login, password) {
    return axios.post('api/login/', {
      login: login,
      password: password
    }).then(response => {
      this.identity_ = null
      localStorage.setItem('_username', response.data.username)
      localStorage.setItem('_userid', response.data.id)
      localStorage.setItem('_email', response.data.email)
    })
  }
};

const Auth = {
  install (Vue, options) {
    if (!options.loginUrl) {
      throw new Error("'login' is not defined")
    }

    // if (options.logoutUrl) {
    //   axios.get('api/logout')
    //   console.log('logout!')
    // }

    if (!options.forbiddenUrl) {
      throw new Error("'forbidden' is not defined")
    }

    // Vue.directive('isAuthorized', IsAuthorizedDirective)
    // Vue.component('isAuthorized', IsAuthorizedComponent)

    let authorizeInstance = null
    Object.defineProperties(Vue.prototype, {
      $auth: {
        get () {
          if (!authorizeInstance) {
            authorizeInstance = new Authorize()
          }
          return authorizeInstance
        }
      }
    })

    let router = options.router
    if (router) {
      router.beforeEach(function (to, from, next) {
        if (to.meta && to.meta.roles) {
          router.app.$auth.identity().then(function () {
            if (!router.app.$auth.isInAnyRole(to.meta.roles)) {
              return next(options.forbiddenUrl)
            } else {
              next()
            }
          }).catch(function () {
            return next(options.loginUrl)
          })
        } else {
          next()
        }
      })
    }
  }
}

export default Auth
