<template>
<div>

<form name="myForm" onsubmit="return false;">
  
<b-list-group >
        <b-list-group-item  href="#" v-for="(data,index) in community_data" :key="index">
         



<b-input-group :prepend="data.name" class="mt-3">
    <b-form-input name="CCC" type="text"></b-form-input>
</b-input-group>
               
    

        </b-list-group-item>
  </b-list-group> 




  <input type="submit" value="Submit" @click="validateForm">
</form>
    


</div>

</template>

<script>


import axios from 'axios'
import store from '../store'

  export default {
  props:{
    task:{}
  },
 
  methods:{
  validateForm(){
    
    // console.log(document.forms["myForm"]['Abc'].value);

  }
  }
 }

</script>
