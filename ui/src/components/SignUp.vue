<template>
    <div class="kt-grid__item kt-grid__item--fluid kt-grid kt-grid--desktop kt-grid--ver-desktop kt-grid--hor-tablet-and-mobile" style="background: white;">
        <div class="kt-grid__item  kt-grid__item--order-tablet-and-mobile-2  kt-grid kt-grid--hor kt-login__aside" style="margin: 10% auto; padding: 25px;">
            <div class="kt-login__wrapper">
                <div class="kt-login__container">
                    <div class="kt-login__body">
                        <div class="kt-login__signup">
                            <div class="kt-login__head">
                                <h3 class="kt-login__title">Sign Up</h3>
                                <div class="kt-login__desc">Enter your details to create your account:</div>
                            </div>
                            <div class="kt-login__form">
                                <b-input-group
                                        prepend="Nickname"
                                        class="mt-3">
                                    <b-form-input v-model="username" />
                                </b-input-group>
                                <b-input-group
                                        prepend="Full Name"
                                        class="mt-3">
                                    <b-form-input v-model="name" />
                                </b-input-group>
                                <b-input-group
                                        prepend="E-mail Address"
                                        class="mt-3">
                                    <b-form-input v-model="email" />
                                </b-input-group>
                                <b-input-group
                                        prepend="Password"
                                        class="mt-3">
                                    <b-form-input type="password" v-model="password" />
                                </b-input-group>
                                <div class="kt-login__actions">
                                    <button id="kt_login_signup_submit" class="btn btn-brand btn-pill btn-elevate" v-on:click="signUp()">Sign Up</button>
                                    <button id="kt_login_signup_cancel" class="btn btn-outline-brand btn-pill">Cancel</button>
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
    import axios from 'axios'
    import store from '../store'

    export default {

        data() {
            return {
                username:'',
                name:'',
                email:'',
                password:''
            }
        },
        methods:{
            async signUp(){
                try {
                    const { data } = await axios.post('http://api.communal-cloud.com/user/', {
                            name: this.name,
                            username : this.username,
                            email: this.email,
                            password: this.password
                    })
                    console.log(data)
                } catch (e) {
                    console.log('FAIL')
                    console.log(e)
                }
            }
        }
    }
</script>
