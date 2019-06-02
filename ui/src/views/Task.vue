<template>
    <div class="card border border-success m-4" style="width: 32rem;">
        <b-button class="mt-3" block @click="$bvModal.show(modalID+'edit')">Edit</b-button>
        <router-link :to="'/community/'+$route.params.community_id+'/workflow/'+$route.params.workflow_id+'/tasks/'+id+'/results'" class="btn btn-primary">Execution Data</router-link>

        <div class="card-body">
            <h2 class="card-title">{{task.Name}}</h2>
            <p class="card-text">{{task.Description}}</p>
            <h6 class="card-text">Available executions: {{task.AvailableTimes}}</h6>
            <p class="card-text" v-if="task.AssignedRoles.length > 0">Assigned Roles:
                <b-badge variant="dark mr-2" v-for="role in task.AssignedRoles">{{role.Name}}</b-badge>
            </p>
            <p v-else>No Assigned Role</p>
            <p class="card-text" v-if="task.AssignedUsers.length > 0">Assigned Users:
                <b-badge variant="dark mr-2" v-for="role in task.AssignedUsers">{{role.Name}}</b-badge>
            </p>
            <p v-else>No Assigned User</p>
            <p class="card-text" v-if="task.Predecessors.length > 0">Predecessors Tasks:
                <b-badge variant="dark mr-2" v-for="role in task.Predecessors">{{role.Name}}</b-badge>
            </p>
            <p v-else>No Predecessors Tasks</p>

            <b-button id="show-btn" variant="danger mr-2 btn-sm">Delete</b-button>
            <b-button id="show-btn" variant="success" @click="$bvModal.show(modalID)">Execute</b-button>
        </div>
        <b-modal :id="modalID+'edit'" size="xl" hide-footer>
            <create-task :taskUpdate="task"></create-task>
        </b-modal>
        <b-modal :id="modalID" hide-footer>
            <div class="d-block text-center">
                <execute-task :task="task" :execute="execution"></execute-task>
            </div>
        </b-modal>
    </div>
</template>

<script>
    import axios from 'axios'
    import store from '../store'
    import ExecuteTask from '../components/ExecuteTask.vue'
    import CreateTask from '../components/CreateTask.vue'
    import {exec} from 'child_process';

    export default {
        components: {
            ExecuteTask, CreateTask
        },
        props: {
            id: 0,
            task: {}
        },
        data() {
            return {}
        },
        computed: {
            modalID: function () {
                return String(this.id)
            },
            execution: function () {
                var execute = {};
                execute = this.task.OutputFields.map(function (item) {
                    if (item.Type == "1") {
                        item.Type = "number"
                    }
                    else if (item.Type == "2") {
                        item.Type = 'text'
                    }
                    else if (item.Type == "8") {
                        item.Type = 'img'
                    }
                    else if (item.Type == "4") {
                        item.Type = 'date'
                    }
                    else if (item.Type == "5") {
                        item.Type = 'geolocation'
                    }
                    else if (item.Type == "3") {
                        item.Type = 'boolean'
                    }

                    return {Name: item.Name, Class: item.Type};
                })
                return execute
            }
        },

        mounted() {
            //this.getTask();
        },
        /* methods: {
             async getTask() {
                 try {
                     const {data} = await axios.get(process.env.VUE_APP_BASE_URL + 'task/' + this.id + '/', {
                         headers: {
                             Authorization: 'token ' + store.getters.token
                         }
                     })

                     const data = {
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
                     }

                     console.log(data);

                     this.task = data

                 } catch (e) {
                     this.$swal(e.message)
                 }
             }
         },*/
    }
</script>