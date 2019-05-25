<template>
  <div class="kt-portlet kt-portlet--height-fluid">
      <div class="kt-portlet__head">
          <div class="kt-portlet__head-label">
              <h3 class="kt-portlet__head-title">
                  Available Communities
              </h3>
          </div>
      </div>
      <div class="kt-portlet__body kt-portlet__body--fluid">
          <div class="kt-widget12">
              <div class="kt-widget12__content">
                  <div class="kt-widget12__item">
                      <community></community>
                      <community></community>
                      <community></community>
                      <community></community>
                      <community></community>
                  </div>
              </div>
          </div>
      </div>
  </div>
</template>

<script>
// @ is an alias to /src

import Community from '@/components/Community.vue'
import axios from 'axios'
import store from '../store'

export default {
    store:store,
  name: 'home',
  components: {
    Community
  },
    data() {
        return {
            communities:[]
        }
    },
    methods:{
      async getCommunities(){
          try {
              const {data} = await axios.get('http://api.communal-cloud.com/community', {
                  headers: {
                      Authorization: 'token ' + store.getters.token
                  }
              })

              console.log(data)

          } catch (e) {
              this.$swal(e.message)
          }
      }
    },
    mounted(){
        this.getCommunities()
    }
}
</script>