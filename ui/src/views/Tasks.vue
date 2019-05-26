<template>
    <div class="kt-portlet kt-portlet--height-fluid">
        <div class="kt-portlet__head">
            <div class="kt-portlet__head-label">
                <h3 class="kt-portlet__head-title">
                  Available Tasks
                </h3>
            </div>
            <div class="kt-portlet__head-toolbar">
                <router-link :to="'/community/'+$route.params.community_id+'/workflow/'+$route.params.workflow_id+'/task/create'" class="btn btn-label-brand btn-bold btn-sm">
                    <i class="fa fa-plus-circle"></i> Create Task
                </router-link>
            </div>
        </div>
        <div class="kt-portlet__body kt-portlet__body--fluid">
            <b-row>
                 <b-col cols="4" v-for="task in tasks" :key="task.id">
                     <task :task="task" :id="task.id"></task>
                 </b-col>
            </b-row>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src

import Task from './Task.vue'
import axios from 'axios'
import store from '../store'

export default {
    store: store,
    name: 'tasks',
    components: {
        Task
    },
    data() {
        return {
           
            tasks: []
        }
    },
    methods:{
        async getTasks(){
            try {
               const {data} = await axios.get(process.env.VUE_APP_BASE_URL+'workflow/' + this.$route.params.workflow_id + '/tasks/', {
                    headers: {
                        Authorization: 'token ' + store.getters.token
                    }
                })
 /*
                const data = [{
                    Name:"Join Us Here",
                    Description:"To join us please fill the form and submit",
                    Available: true,
                    AvailableTill: null,
                    AvailableTimes: 20000,
                    AssignedUsers: [1],
                    AssignedRoles: [],
                    Predecessors: [],
                    InputFields: [],
                    OutputFields: [15, 16 , 20]
                }]
*/
                console.log(data)

                this.tasks=data

            } catch (e) {
                this.$swal(e.message)
            }
        }
    },
    mounted(){
        this.getTasks()
    }
}
</script>