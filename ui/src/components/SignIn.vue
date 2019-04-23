<template>
    <div class="kt-grid__item kt-grid__item--fluid kt-grid kt-grid--desktop kt-grid--ver-desktop kt-grid--hor-tablet-and-mobile">
        <div class="kt-grid__item  kt-grid__item--order-tablet-and-mobile-2  kt-grid kt-grid--hor kt-login__aside">
            <div class="kt-login__wrapper">
                <div class="kt-login__container">
                    <div class="kt-login__body">
                        <div class="kt-login__logo">
                            <a href="#">
                                <img src="assets/media/company-logos/logo-2.png">
                            </a>
                        </div>
                        <div class="kt-login__signin">
                            <div class="kt-login__head">
                                <h3 class="kt-login__title">Sign In To Admin</h3>
                            </div>
                            <div class="kt-login__form">
                                <form class="kt-form" action="">
                                    <div class="form-group">
                                        <input class="form-control" type="text" placeholder="Email" name="email" autocomplete="off">
                                    </div>
                                    <div class="form-group">
                                        <input class="form-control form-control-last" type="password" placeholder="Password" name="password">
                                    </div>
                                    <div class="kt-login__extra">
                                        <label class="kt-checkbox">
                                            <input type="checkbox" name="remember"> Remember me
                                            <span></span>
                                        </label>
                                        <a href="javascript:;" id="kt_login_forgot">Forget Password ?</a>
                                    </div>
                                    <div class="kt-login__actions">
                                        <button id="kt_login_signin_submit" class="btn btn-brand btn-pill btn-elevate">Sign In</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                        <div class="kt-login__signup">
                            <div class="kt-login__head">
                                <h3 class="kt-login__title">Sign Up</h3>
                                <div class="kt-login__desc">Enter your details to create your account:</div>
                            </div>
                            <div class="kt-login__form">
                                <form class="kt-form" action="">
                                    <div class="form-group">
                                        <input class="form-control" type="text" placeholder="Fullname" name="fullname">
                                    </div>
                                    <div class="form-group">
                                        <input class="form-control" type="text" placeholder="Email" name="email" autocomplete="off">
                                    </div>
                                    <div class="form-group">
                                        <input class="form-control" type="password" placeholder="Password" name="password">
                                    </div>
                                    <div class="form-group">
                                        <input class="form-control form-control-last" type="password" placeholder="Confirm Password" name="rpassword">
                                    </div>
                                    <div class="kt-login__extra">
                                        <label class="kt-checkbox">
                                            <input type="checkbox" name="agree"> I Agree the <a href="#">terms and conditions</a>.
                                            <span></span>
                                        </label>
                                    </div>
                                    <div class="kt-login__actions">
                                        <button id="kt_login_signup_submit" class="btn btn-brand btn-pill btn-elevate">Sign Up</button>
                                        <button id="kt_login_signup_cancel" class="btn btn-outline-brand btn-pill">Cancel</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                        <div class="kt-login__forgot">
                            <div class="kt-login__head">
                                <h3 class="kt-login__title">Forgotten Password ?</h3>
                                <div class="kt-login__desc">Enter your email to reset your password:</div>
                            </div>
                            <div class="kt-login__form">
                                <form class="kt-form" action="">
                                    <div class="form-group">
                                        <input class="form-control" type="text" placeholder="Email" name="email" id="kt_email" autocomplete="off">
                                    </div>
                                    <div class="kt-login__actions">
                                        <button id="kt_login_forgot_submit" class="btn btn-brand btn-pill btn-elevate">Request</button>
                                        <button id="kt_login_forgot_cancel" class="btn btn-outline-brand btn-pill">Cancel</button>
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
                    <a href="javascript:;" id="kt_login_signup" class="kt-login__account-link">Sign Up!</a>
                </div>
            </div>
        </div>
        <div class="kt-grid__item kt-grid__item--fluid kt-grid__item--center kt-grid kt-grid--ver kt-login__content" style="background-image: url(assets/media//bg/bg-4.jpg);">
            <div class="kt-login__section">
                <div class="kt-login__block">
                    <h3 class="kt-login__title">Join Our Community</h3>
                    <div class="kt-login__desc">
                        Lorem ipsum dolor sit amet, coectetuer adipiscing
                        <br>elit sed diam nonummy et nibh euismod
                    </div>
                </div>
            </div>
        </div>
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