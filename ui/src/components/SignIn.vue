<template>
    <div class="kt-grid__item kt-grid__item--fluid kt-grid kt-grid--desktop kt-grid--ver-desktop kt-grid--hor-tablet-and-mobile">
        <div class="kt-grid__item  kt-grid__item--order-tablet-and-mobile-2  kt-grid kt-grid--hor kt-login__aside">
            <div class="kt-login__wrapper">
                <div class="kt-login__container">
                    <div class="kt-login__body">
                        <div class="kt-login__signin">
                            <div class="kt-login__head">
                                <h3 class="kt-login__title">Sign In</h3>
                            </div>
                            <div class="kt-login__form">
                                <form class="kt-form" action="">
                                    <b-input-group
                                            prepend="e-mail"
                                            class="mt-3"
                                            id="fieldset1"
                                            description="Let us know your email."
                                            label="Enter your email"
                                            label-for="input1"
                                            :invalid-feedback="invalidFeedback"
                                            :valid-feedback="validFeedback"
                                            :state="state">
                                        <b-form-input />
                                    </b-input-group>

                                    <b-input-group
                                            prepend="Password"
                                            class="mt-3"
                                            id="fieldset1"
                                            label="Enter your password"
                                            label-for="input1"
                                            :invalid-feedback="invalidFeedback"
                                            :valid-feedback="validFeedback"
                                            :state="state">
                                        <b-form-input type="password" />
                                    </b-input-group>
                                    <div class="kt-login__extra">
                                        <router-link to="/user/forgot" id="kt_login_forgot">Forget Password ?</router-link>
                                    </div>
                                    <div class="kt-login__actions">
                                        <button id="kt_login_signin_submit" class="btn btn-brand btn-pill btn-elevate">Sign In</button>
                                    </div>
                                </form>
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
  export default {
    computed: {
      state() {
        return this.name.length >= 4 ? true : false
      },
      invalidFeedback() {
        if (this.name.length > 4) {
          return ''
        } else if (this.name.length > 0) {
          return 'Enter at least 4 characters'
        } else {
          return 'Please enter something'
        }
      },
      validFeedback() {
        return this.state === true ? 'Thank you' : ''
      }
    },
    data() {
      return {
        name: ''
      }
    }
  }
</script>