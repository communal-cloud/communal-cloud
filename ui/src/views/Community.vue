<template>

<div class="card" style="width: 22rem;">
  <div class="card-body">
    <h5 class="card-title">{{community.Name}}</h5>
     <h6 class="card-subtitle mb-2 text-muted">{{community.Purpose}}</h6>
    <p class="card-text">{{community.Description}}</p>
    <a href="#" class="btn btn-primary">Explore</a>
  </div>
</div>

</template>

<script>
import axios from 'axios'
import store from '../store'
  export default {
    props:{
      id:0
    },
    
    data() {
      return {
        community:{
          Name: '',
          Purpose:'',
          Description:''
        },
        
      }
    },
    mounted(){
      this.getCommunity();
    },
    methods:{
      async getCommunity(){
          try {
              const {data} = await axios.get(process.env.VUE_APP_BASE_URL+'community/'+this.id+'/', {
                  headers: {
                      Authorization: 'token ' + store.getters.token
                  }
              })
              console.log(data);
              this.community=data

          } catch (e) {
              this.$swal(e.message)
          }
      }
    },
  }
</script>