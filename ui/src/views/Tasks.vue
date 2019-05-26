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
                 <b-button id="show-btn" variant="success" @click="$bvModal.show('dataType')">Create Data Type</b-button>
            </div>
        </div>
        <div class="kt-portlet__body kt-portlet__body--fluid">
            <b-row>
                 <b-col cols="4" v-for="task in tasks" :key="task.id">
                     <task :task="task" :id="task.id"></task>
                 </b-col>
            </b-row>
        </div>



         <b-modal id="dataType" hide-footer>
            <template slot="modal-title">
            <code>Create Data Type</code> 
            </template>
            <div class="d-block text-center">
            <create-data-type :community_id="this.$route.params.community_id"></create-data-type>
            </div>
            <b-button class="mt-3" block @click="$bvModal.hide('dataType')">Close Me</b-button>
        </b-modal>

       
    </div>
</template>

<script>
// @ is an alias to /src
import CreateDataType from '../components/CreateDataType.vue'
import Task from './Task.vue'
import axios from 'axios'
import store from '../store'

export default {
    store: store,
    name: 'tasks',
    components: {
        Task,
        CreateDataType
    },
    data() {
        return {
           
            tasks: []
        }
    },
    methods:{
        async getTasks(id = null){
            try {
                if(id === null)
                    id = this.$route.params.workflow_id

               const {data} = await axios.get(process.env.VUE_APP_BASE_URL+'workflow/' + id + '/tasks/', {
                    headers: {
                        Authorization: 'token ' + store.getters.token
                    }
                })

                return this.tasks = data

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