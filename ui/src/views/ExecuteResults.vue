<template>
    <div class="kt-portlet kt-portlet--height-fluid">
        <div class="kt-portlet kt-portlet--height-fluid">
            <div class="kt-portlet__head">
                <div class="kt-portlet__head-label">
                    <h3 class="kt-portlet__head-title">
                        Execution Results
                    </h3>
                </div>
               
            </div>
            <div class="kt-portlet__body kt-portlet__body--fluid" v-if="workflows">
                <b-row>
                <b-col cols="4" v-for="community in communities" :key="community.id">
                    <community :id="community.id">
                    </community>
                </b-col>
            </b-row>
            </div>
        </div>

    </div>
</template>

<script>
    import Community from './Community.vue'
    import Workflow from './Workflow.vue'
    import Workflows from './Workflows.vue'
    import store from '../store'

    export default {
        store: store,
        name: 'communityDetails',
        components: {
            Workflow
        },
        data() {
            return {
                community: {
                    Name: '',
                    Purpose: '',
                    Description: ''
                },
                workflows: []
            }
        },
        methods:{
            async getCommunity(){
               try {
                    if(id === null)
                        id = this.id

                    const {data} = await axios.get(process.env.VUE_APP_BASE_URL + 'community/' + id + '/', {
                        headers: {
                            Authorization: 'token ' + store.getters.token
                        }
                    })

                    return this.community = data
                } catch (e) {
                    this.$swal(e.message)
                }
            },
            
        },
        mounted(){
           
        }
    }

</script>

<style scoped>


</style>