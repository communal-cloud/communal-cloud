<template>
    <b-row class="row justify-content-center">
        <b-col class="col-xs-12 col-sm-8 col-md-6">
            <div class="card">
                <div class="card-body">
                    <h3 v-if="taskUpdate !== undefined" class="card-title">Update Task</h3>
                    <h3 v-else class="card-title">Create Task</h3>
                    <b-input-group
                            prepend="Name"
                            class="mt-3"
                            id="task_name"
                            label="Enter task name"
                            label-for="task_name">
                        <b-form-input v-model="task_name" type="text"/>
                    </b-input-group>

                    <b-input-group
                            prepend="Description"
                            class="mt-3"
                            id="task_description"
                            label="Enter task description"
                            label-for="task_description">
                        <b-form-input v-model="task_description" type="text"/>
                    </b-input-group>

                    <b-row class="mt-4 mb-4">
                        <b-col class="text-left">
                            <b-form-checkbox v-model="task_available" name="check-button" switch>
                                Available <b>({{ (task_available) ? 'Yes' : 'No' }})</b>
                            </b-form-checkbox>
                        </b-col>
                    </b-row>

                    <b-input-group
                            prepend="Available Till"
                            class="mt-3"
                            id="task_available_till"
                            label="Enter task's last available date"
                            label-for="task_available_till">
                        <b-form-input v-model="task_available_till" type="datetime-local"/>
                    </b-input-group>

                    <b-input-group
                            prepend="Availability Limit"
                            class="mt-3"
                            id="task_available_times"
                            label="Enter task's availability limit"
                            label-for="task_available_times">
                        <b-form-input v-model="task_available_times" type="number"/>
                    </b-input-group>

                    <hr/>

                    <b-row class="mt-2 mb-2">
                        <b-col class="text-left">
                            <label><strong>Restrict to Members</strong></label>
                            <b-form-select v-model="task_members" :options="community_members" multiple></b-form-select>
                            <div id="task_users">
                                <b-badge class="mt-1 mr-1" size="sm" variant="dark" v-for="member in task_members"
                                         :key="member">
                                    {{ community_members.find((community_member) => {return community_member.value ===
                                    member}).text }}
                                </b-badge>
                            </div>
                        </b-col>
                    </b-row>

                    <hr/>

                    <b-row class="mt-2 mb-2">
                        <b-col class="text-left">
                            <label><strong>Restrict to Roles</strong></label>
                            <b-form-select v-model="task_roles" :options="community_roles" multiple></b-form-select>
                            <div id="task_roles">
                                <b-badge class="mt-1 mr-1" size="sm" variant="dark" v-for="role in task_roles"
                                         :key="role">
                                    {{ community_roles.find((community_role) => {return community_role.value ===
                                    role}).text }}
                                </b-badge>
                            </div>
                        </b-col>
                    </b-row>

                    <hr/>

                    <b-row class="mt-2 mb-2">
                        <b-col class="text-left">
                            <label><strong>Predecessor Tasks</strong></label>
                            <b-form-select v-model="task_predecessors" :options="workflow_tasks"
                                           multiple></b-form-select>
                            <div id="task_predecessors">
                                <b-badge class="mt-1 mr-1" size="sm" variant="dark" v-for="task in task_predecessors"
                                         :key="task">
                                    {{ workflow_tasks.find((workflow_task) => {return workflow_task.value ===
                                    task}).text }}
                                </b-badge>
                            </div>
                        </b-col>
                    </b-row>

                    <hr/>

                    <b-row class="mt-2 mb-2">
                        <b-col class="text-left">
                            <label><strong>Input Fields</strong></label>
                            <b-form-select v-model="task_input_fields" :options="workflow_input_fields"
                                           multiple></b-form-select>
                            <div id="task_input_fields">
                                <b-badge class="mt-1 mr-1" size="sm" variant="dark"
                                         v-for="(data,i) in task_input_fields" :key="data+i">
                                    {{ workflow_input_fields.find((workflow_input_field) => {return
                                    workflow_input_field.value === data}).text }}
                                </b-badge>
                            </div>
                        </b-col>
                    </b-row>

                    <hr/>

                    <b-row class="mt-2 mb-2">
                        <b-col class="text-left">
                            <label><strong>Output Fields</strong></label>
                            <b-form-select v-model="task_output_fields" :options="community_data_types"
                                           multiple></b-form-select>
                        </b-col>
                        <b-col class="text-left">
                            <ul id="task_output_fields" style="list-style: none">
                                <li v-for="(data,i) in task_output_fields" :key="data+i">
                                    <b-button>{{ community_data_types.find((community_data_type) => {return
                                        community_data_type.value === data}).text }}
                                    </b-button>
                                    <b-form-group label="Field Options">
                                        <b-form-checkbox-group
                                                v-model="task_output_field_options[data]"
                                                :options="field_options"
                                                name="flavour-2a"
                                                stacked
                                        ></b-form-checkbox-group>
                                    </b-form-group>
                                </li>
                            </ul>
                        </b-col>
                    </b-row>

                    <b-button v-if="taskUpdate === undefined" v-on:click="createTask()" variant="outline-primary">Create
                    </b-button>
                    <b-button v-else v-on:click="updateTask()" variant="outline-primary">Update</b-button>
                </div>
            </div>
        </b-col>
    </b-row>
</template>
<script>
    import Community from "../views/Community";
    import Workflow from "../views/Workflow";
    import Tasks from "../views/Tasks";
    import axios from 'axios'
    import store from '../store'

    export default {
        computed: {
            community: function () {
                return Community.methods.getCommunity(this.$route.params.community_id)
            },
            workflow: function () {
                return Workflow.methods.getWorkflow(this.$route.params.workflow_id)
            }
        },
        props: {
            taskUpdate: {}
        },
        data() {
            return {
                community_id:0,
                workflow_id:0,
                community_data: {},
                community_members: [],
                community_roles: [],
                community_data_types: {},
                field_types: [],
                field_options: [],
                task_name: '',
                task_description: '',
                task_available: true,
                task_available_till: null,
                task_available_times: null,
                task_members: [],
                task_roles: [],
                task_input_fields: [],
                task_output_fields: [],
                task_output_field_options: [],
                task_predecessors: [],
                workflow_input_fields: [],
                workflow_tasks: []
            }
        },
        methods: {
            async updateTask() {
                try {
                    const {data} = await axios.put(process.env.VUE_APP_BASE_URL + 'task/' + this.taskUpdate.id + '/', {
                        Name: this.task_name,
                        Description: this.task_description,
                        Available: this.task_available,
                        AvailableTill: (this.task_available_till !== null) ? new Date(this.task_available_till).toISOString().slice(0, 19).replace('T', ' ') : this.task_available_till,
                        AvailableTimes: parseInt(this.task_available_times),
                        AssignedUsers: this.task_members.filter(Number),
                        AssignedRoles: this.task_roles.filter(Number),
                        Predecessors: this.task_predecessors.filter(Number),
                        InputFields: this.task_input_fields.filter(Number),
                        OutputFields: this.task_output_fields.filter(Number)
                    })

                    if (data) {
                        this.$swal("Task updated")
                    }
                } catch (e) {
                    if (e.response.status !== 500) {
                        Object.keys(e.response.data).forEach(key => {
                            this.$swal(key, e.response.data[key][0], 'error')
                        })
                    } else
                        this.$swal("Error when updating task")
                }
            },
            async createTask() {
                try {
                    const {data} = await axios.post(process.env.VUE_APP_BASE_URL + 'task/' + this.$route.params.workflow_id + '/', {
                        Name: this.task_name,
                        Description: this.task_description,
                        Available: this.task_available,
                        AvailableTill: (this.task_available_till !== null) ? new Date(this.task_available_till).toISOString().slice(0, 19).replace('T', ' ') : this.task_available_till,
                        AvailableTimes: parseInt(this.task_available_times),
                        AssignedUsers: this.task_members.filter(Number),
                        AssignedRoles: this.task_roles.filter(Number),
                        Predecessors: this.task_predecessors.filter(Number),
                        InputFields: this.task_input_fields.filter(Number),
                        OutputFields: this.task_output_fields.filter(Number)
                    })

                    if (data) {
                        this.$swal("Task created")

                        this.$router.push('/community/' + this.$route.params.community_id + '/workflow/' + this.$route.params.workflow_id + '/tasks/')
                    }
                } catch (e) {
                    if (e.response.status !== 500) {
                        Object.keys(e.response.data).forEach(key => {
                            this.$swal(key, e.response.data[key][0], 'error')
                        })
                    } else
                        this.$swal("Error when creating task")
                }
            },
            async getDataTypes() {
                await Community.methods.getCommunityDataTypes(this.$route.params.community_id).then((data_types) => {
                    let temp = []

                    let field_types = this.field_types

                    data_types.forEach(function (data_type) {
                        if (data_type.Fields.length) {
                            data_type.Fields.forEach(function (field) {
                                temp.push({
                                    value: field.id,
                                    text: data_type.Name + ' - ' + field.Name + ' (' + field_types[field.Type] + ')'
                                })
                            })
                        }
                    })

                    this.community_data_types = temp
                })
            },
            async getFieldTypes() {
                try {
                    const {data} = await axios.get(process.env.VUE_APP_BASE_URL + 'data/', {
                        headers: {
                            Authorization: 'token ' + store.getters.token
                        }
                    })

                    return this.field_types = data
                } catch (e) {
                    this.$swal(e.message)
                }
            },
            async getFieldOptions() {
                try {
                    /*const {data} = await axios.get(process.env.VUE_APP_BASE_URL + 'data/', {
                        headers: {
                            Authorization: 'token ' + store.getters.token
                        }
                    })*/

                    const data = [
                        'required',
                        'hidden',
                        'read-only'
                    ]

                    return this.field_options = data
                } catch (e) {
                    this.$swal(e.message)
                }
            },
            async getMembers() {
                await Community.methods.getCommunityMembers(this.$route.params.community_id).then((members) => {
                    this.community_members = members.map(function (member) {
                        return {value: member.User.id, text: member.User.name}
                    })
                })
            },
            async getRoles() {
                await Community.methods.getCommunityRoles(this.$route.params.community_id).then((roles) => {
                    this.community_roles = roles.map(function (role) {
                        return {value: role.id, text: role.Name}
                    })
                })
            },
            async getTasks(community_id,workflow_id,_this) {

                const {data} = await axios.get(process.env.VUE_APP_BASE_URL+'workflow/' + workflow_id + '/tasks/', {
                    headers: {
                        Authorization: 'token ' + store.getters.token
                    }
                })
                let temp=[]
                let field_types = this.field_types
                data.forEach(function (task) {
                        if (task.OutputFields.length) {
                            task.OutputFields.forEach(function (field) {
                                temp.push({
                                    value: field.id,
                                    text: task.Name + ' - ' + field.Name + ' (' + field_types[field.Type] + ')'
                                })
                            })
                        }
                    })

                    this.workflow_input_fields = temp

                
            },
        },
        mounted() {
            this.community_id=this.$route.params.community_id
            this.workflow_id=this.$route.params.workflow_id
            this.getFieldTypes()

            this.getFieldOptions()

            this.getDataTypes()

            this.getMembers()

            this.getRoles()

            this.getTasks(this.community_id,this.workflow_id,this)
            
            

            if (this.taskUpdate !== undefined) {
                this.task_name = this.taskUpdate.Name
                this.task_description = this.taskUpdate.Description
                this.task_available = this.taskUpdate.Available
                this.task_available_till = this.taskUpdate.AvailableTill
                this.task_available_times = this.taskUpdate.AvailableTimes
                this.task_roles = this.taskUpdate.AssignedRoles
            }
        }
    }
</script>