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
</style>
<template>
  <v-container class="pt-5" fluid grid-list-md>
    <div id="login">
      <v-layout fill-height align-center row justify-center>
        <v-flex xs3>
          <v-card>
            <h5 class="text-xs-center pa-2" style="background-color: #2D3540">
              <img style="height: 60px; margin-top: 2px;"
             src="/static/imgs/certm2.png"
             alt="avatar">
            </h5>
            <br>
            <v-form v-model="valid" class="px-4 pb-2" @submit.prevent="submit">
              <v-text-field
                label="Login"
                v-model="login"
                :rules="loginRules"
                required
              ></v-text-field>
              <v-text-field
                label="Password"
                type="password"
                v-model="password"
                :rules="passwordRules"
                required
              ></v-text-field>
              <div class="red--text text-xs-center">{{ message }}</div>
              <div class="text-xs-center">
                <v-btn type="submit" :disabled="!valid">Log-In</v-btn>
              </div>
            </v-form>
          </v-card>
          <p class="text-xs-center mt-3 blue-grey--text text--darken-4">
			            <span class="caption text--darken-2">
			            </span>
          </p>
        </v-flex>
      </v-layout>
    </div>
  </v-container>
</template>
<script>
  export default {
    data () {
      return {
        valid: false,
        login: '',
        loginRules: [
          (v) => !!v || 'This field is required'
        ],
        password: '',
        passwordRules: [
          (v) => !!v || 'This field is required'
        ],
        message: ''
      }
    },
    methods: {
      submit () {
        this.$auth.login(this.login, this.password).then(() => {
          this.$router.push('/')
        }).catch(e => {
          this.login = ''
          this.password = ''
          if (e.response.status === 401) {
            this.message = 'Wrong login or password'
          } else {
            this.message = 'Some troubles on server :('
          }
        })
      }
    }
  }
</script>
