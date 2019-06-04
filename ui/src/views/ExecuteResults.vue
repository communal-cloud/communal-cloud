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
            <div class="kt-portlet__body kt-portlet__body--fluid">
                <b-row>
                <b-col cols="4" v-for="task in taskData" :key="task.id">
                    <b-row v-for="exec in task" :key="String(exec.id)">
                    {{exec.Value}}
                     </b-row>
                </b-col>
            </b-row>
            </div>
        </div>

    </div>
</template>

<script>
    
    import store from '../store'
      import axios from 'axios'

    export default {
        store: store,
        name: 'ExecuteResults',
        
        data() {
            return {
                taskData:[],
             
            }
        },
        methods:{
            async getExecutionData(){
                try {
                    const {data} = await axios.post(process.env.VUE_APP_BASE_URL + 'executiondata/' + this.$route.params.task_id + '/', {},{
                        headers: {
                            Authorization: 'token ' + store.getters.token
                        }
                    })

                    if (data)
                        this.taskData = data
                        console.log("data")
                } catch (e) {
                    this.$swal(e.message)
                }


            }
              
            
        },
        mounted(){
           
           this.getExecutionData()
        }
    }

</script>

<style scoped>


</style>