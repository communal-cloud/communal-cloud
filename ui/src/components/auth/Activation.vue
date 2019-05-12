<template>
    <div class="kt-grid__item kt-grid__item--fluid kt-grid kt-grid--desktop kt-grid--ver-desktop kt-grid--hor-tablet-and-mobile" style="background: white;">
        <div class="kt-grid__item  kt-grid__item--order-tablet-and-mobile-2  kt-grid kt-grid--hor kt-login__aside" style="margin: 10% auto; padding: 25px;">
            <div class="kt-login__wrapper">
                <div class="kt-login__container">
                    <div class="kt-login__body">
                        <div class="kt-login__signin">
                            <div class="kt-login__head">
                                <h3 class="kt-login__title">Activation</h3>
                                <div class="form-group form-group-last">
                                    <div class="alert alert-secondary" role="alert">
                                        <div class="alert-text">
                                            Click below button to activate your account
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="kt-login__form">
                                <div class="kt-login__actions">
                                    <button class="btn btn-brand btn-pill btn-elevate" v-on:click="activation()">Activate</button>
                                </div>
                                <hr />
                                <div class="kt-login__extra">
                                    <router-link to="/user/login" id="kt_login_forgot">Already have an account ?</router-link>
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

      }
    },
      methods: {
          async activation() {
              try {
                  const {data} = await axios.post(process.env.VUE_APP_BASE_URL+'user/activation/?token='+this.$route.params.token)

                  if(data.status === "OK"){
                      this.$swal("Successfully activated! Please login with your account credentials.")

                      this.$router.push('/user/login')
                  }

                  else{
                      console.log(data)

                      this.$swal(data.status)
                  }

              } catch (e) {
                  this.$swal("Token not found!")
              }
          }
      },
      mounted() {

      }
  }
</script>