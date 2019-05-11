<template>
    <div class="kt-grid__item kt-grid__item--fluid kt-grid kt-grid--desktop kt-grid--ver-desktop kt-grid--hor-tablet-and-mobile" style="background: white;">
        <div class="kt-grid__item  kt-grid__item--order-tablet-and-mobile-2  kt-grid kt-grid--hor kt-login__aside" style="margin: 10% auto; padding: 25px;">
            <div class="kt-login__wrapper">
                <div class="kt-login__container">
                    <div class="kt-login__body">
                        <div class="kt-login__signin">
                            <div class="kt-login__head">
                                <h3 class="kt-login__title">Sign In</h3>
                            </div>
                            <div class="kt-login__form">
                                <b-input-group
                                        prepend="E-mail Address"
                                        class="mt-3">
                                    <b-form-input v-model="username" />
                                </b-input-group>

                                <b-input-group
                                        prepend="Password"
                                        class="mt-3">
                                    <b-form-input type="password" v-model="password" />
                                </b-input-group>
                                <div class="kt-login__extra">
                                    <router-link to="/user/forgot" id="kt_login_forgot">Forget Password ?</router-link>
                                </div>
                                <div class="kt-login__actions">
                                    <button id="kt_login_signin_submit" class="btn btn-brand btn-pill btn-elevate" v-on:click="signIn()">Sign In</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="kt-login__account">
                    <span class="kt-login__account-msg">
                        Don't have an account yet ?
                    </span>&nbsp;&nbsp;
                    <router-link to="/user/register" id="kt_login_signup" class="kt-login__account-link">Sign Up!</router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  import axios from 'axios/index'
  import store from '../../store'

  export default {
    computed: {},
    data() {
      return {
          username:'',
          password:''
      }
    },
      methods: {
          async signIn() {
              try {
                  const {data} = await axios.post(process.env.VUE_APP_BASE_URL+'user/login', {
                      username: this.username,
                      password: this.password
                  })

                  if(data.token) {
                      store.commit('save_token', {token:data.token, remember:true})

                      store.dispatch('fetchUser')

                      this.$router.push('/')
                  }

                  else {
                      this.$swal('Wrong info!')
                  }
              } catch (e) {
                  this.$swal(e.message)
              }
          }
      }
  }
</script>