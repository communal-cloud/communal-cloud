<template>
    <div class="kt-grid__item kt-grid__item--fluid kt-grid kt-grid--desktop kt-grid--ver-desktop kt-grid--hor-tablet-and-mobile" style="background: white;">
        <div class="kt-grid__item  kt-grid__item--order-tablet-and-mobile-2  kt-grid kt-grid--hor kt-login__aside" style="margin: 10% auto; padding: 25px;">
            <div class="kt-login__wrapper">
                <div class="kt-login__container">
                    <div class="kt-login__body">
                        <div class="kt-login__signup">
                            <div class="kt-login__head">
                                <h3 class="kt-login__title">Sign Up</h3>
                                <div class="form-group form-group-last">
                                    <div class="alert alert-secondary" role="alert">
                                        <div class="alert-text">
                                            Enter your details to create your account
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="kt-login__form">
                                <b-form-group
                                        label="Name"
                                        class="text-left">
                                    <b-form-input
                                            placeholder="Please enter your name"
                                            v-model="name"
                                            class="form-control" />
                                </b-form-group>
                                <b-form-group
                                        label="E-mail Address"
                                        class="text-left">
                                    <b-form-input
                                            placeholder="Please enter your e-mail address"
                                            type="email"
                                            v-model="email"
                                            class="form-control" />
                                </b-form-group>
                                <b-form-group
                                        label="Password"
                                        class="text-left">
                                    <b-form-input
                                            placeholder="Please enter your password"
                                            type="password"
                                            v-model="password"
                                            class="form-control" />
                                </b-form-group>
                                <div class="kt-login__actions">
                                    <button id="kt_login_signup_submit" class="btn btn-brand btn-pill btn-elevate" v-on:click="signUp()">Sign Up</button>
                                    <router-link id="kt_login_signup_cancel" class="btn btn-outline-brand btn-pill" to="/user/login">Login</router-link>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import axios from 'axios/index'
    import store from '../../store'

    export default {
        data() {
            return {
                name:'',
                email:'',
                password:''
            }
        },
        methods:{
           
            async signUp(){
                const reg = /^(?=.*\d)(?=.*[\-\\*\'#$%_&()[\]{}=+/!^])(?=.*[a-z])(?=.*[A-Z])(?!.*\s).{6,}$/
                if(this.name.length<3)
                     this.$swal('Name field must contain at least 3 characters !')

                else if(reg.test(this.password) === false)
                    this.$swal("Password must contain at least one of the -*'#$%_&()[]{}=+/!^ characters at least one small and capital letter and number")

                else{
                    try {
                        const { data } = await axios.post(process.env.VUE_APP_BASE_URL+'user/', {
                                name: this.name,
                                email: this.email,
                                username: this.email,

                                password: this.password
                        })

                        if(data.email)
                            this.$swal("An activation mail has been sent to your e-mail address: " + data.email)

                        else {
                            console.log(data)

                            this.$swal("Wrong Info!")
                        }
                    } catch (e) {

                        if(e.response.status !== 500) {
                            this.$swal(JSON.stringify(e.response.data))
                        }

                        else
                            this.$swal(e.message)
                    }
                }
            }
        }
    }
</script>