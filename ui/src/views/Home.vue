<template>
  <div class="home">
   
    <b-container class="bv-example-row">
  <b-row class="justify-content-md-center">
  
    <b-col cols="12" md="auto">
       <sign-in></sign-in>
    </b-col>
 
  </b-row>

  
</b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import SignIn from '@/components/SignIn.vue'

export default {
  name: 'home',
  components: {
    SignIn
  }
}
</script>
