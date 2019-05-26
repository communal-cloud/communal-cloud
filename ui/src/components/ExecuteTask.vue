<template>
<div>

<form name="myForm" onsubmit="return false;">
  
<b-list-group >
        <b-list-group-item  href="#" v-for="(data,index) in task.OutputFields" :key="index">
         



<b-input-group :prepend="data.Name" class="mt-3">
    <b-form-input :name="data.Name" :type="data.Type"></b-form-input>
</b-input-group>
               
    

        </b-list-group-item>
  </b-list-group> 




  <input type="submit" value="Submit" @click="execute">
</form>
    


</div>

</template>

<script>


import axios from 'axios'
import store from '../store'


  export default {
  props:{
    task:{},
    execution:{}
  },
 
  methods:{
  async execute() {
    var Data=[]
      this.task.OutputFields.map(function(item) {
        Data.push({"Field" : item.id, "Value": document.forms["myForm"][item.Name].value })
      })

console.log(Data)
    
                try {
                    const {data} = await axios.post(process.env.VUE_APP_BASE_URL + 'execution/', {
                        
                        Task : this.task.id,
                        Data : Data,

                    },{headers : {
                            Authorization: 'token ' + store.getters.token
                        }})
                    console.log(data);
                    

                } catch (e) {
                    this.$swal(e.message)
                }
            },
  validateForm(){
    
     console.log(document.forms["myForm"]['Name'].value);

  }
  }
 }

</script>
