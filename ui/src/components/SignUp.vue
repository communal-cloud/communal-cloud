<template>
    <div class="kt-grid__item kt-grid__item--fluid kt-grid kt-grid--desktop kt-grid--ver-desktop kt-grid--hor-tablet-and-mobile">
        <div class="kt-grid__item  kt-grid__item--order-tablet-and-mobile-2  kt-grid kt-grid--hor kt-login__aside">
            <div class="kt-login__wrapper">
                <div class="kt-login__container">
                    <div class="kt-login__body">
                        <div class="kt-login__signup">
                            <div class="kt-login__head">
                                <h3 class="kt-login__title">Sign Up</h3>
                                <div class="kt-login__desc">Enter your details to create your account:</div>
                            </div>
                            <div class="kt-login__form">
                             
                                    <div class="form-group">
                                        <input class="form-control" type="text" placeholder="User Name" v-model="username">
                                    </div>
                                    <div class="form-group">
                                        <input class="form-control" type="text" placeholder="Name" v-model="name">
                                    </div>
                                    <div class="form-group">
                                        <input class="form-control" type="text" placeholder="Email" v-model="email" autocomplete="off">
                                    </div>
                                    <div class="form-group">
                                        <input class="form-control" type="password" placeholder="Password" v-model="password">
                                    </div>
                                   
                                    
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
            console.log('sign Up')
           
            try {
        const { data } = await axios.post('http://api.communal-cloud.com/user/', {
            headers: {
        
            Host : 'api.communal-cloud.com'
          },
          body: {
            name: this.name,
            username : this.username,
            email: this.email,
            password: this.password
          }
        },{
            useCredentials : true
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