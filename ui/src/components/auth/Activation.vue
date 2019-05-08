<template>
    <div class="kt-grid__item kt-grid__item--fluid kt-grid kt-grid--desktop kt-grid--ver-desktop kt-grid--hor-tablet-and-mobile" style="background: white;">
        <div class="kt-grid__item  kt-grid__item--order-tablet-and-mobile-2  kt-grid kt-grid--hor kt-login__aside" style="margin: 10% auto; padding: 25px;">
            <div class="kt-login__wrapper">
                <div class="kt-login__container">
                    <div class="kt-login__body">
                        <div class="kt-login__signin">
                            <div class="kt-login__head">
                                <h3 class="kt-login__title">Activation</h3>
                            </div>
                            <div class="kt-login__form">
                                <p><strong>Token: </strong>{{ $route.params.token }}</p>
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
                  const {data} = await axios.post('http://api.communal-cloud.com/user/activation?token='+this.$route.params.token)

                  console.log(data)
              } catch (e) {
                  this.$swal(e.message)
              }
          }
      },
      mounted() {
        this.activation()
      }
  }
</script>