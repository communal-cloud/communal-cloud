<template>
<<<<<<< HEAD
    <b-row class="row justify-content-center">
        <b-col class="col-xs-12 col-sm-8 col-md-6">
=======
    <div class="row justify-content-center">
        <div class="col-xs-12 col-sm-8 col-md-6 col-lg-4">
>>>>>>> parent of 1b3711fd... Merge remote-tracking branch 'origin/master'
            <div class="card">
                <div class="card-body">
                    <h3 class="card-title">Create Task</h3>
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

<<<<<<< HEAD
                    <b-form-checkbox v-model="task_available" name="check-button" switch>
                        Available <b>({{ (checked) ? 'Yes' : 'No' }})</b>
                    </b-form-checkbox>
=======
                    <b-row class="mt-4 mb-4">
                        <b-col class="text-left">
                            <b-form-checkbox v-model="task_available" name="check-button" switch>
                                Available <b>({{ (task_available) ? 'Yes' : 'No' }})</b>
                            </b-form-checkbox>
                        </b-col>
                    </b-row>
>>>>>>> parent of 1b3711fd... Merge remote-tracking branch 'origin/master'

                    <b-input-group
                            prepend="Available Till"
                            class="mt-3"
                            id="task_available_till"
                            label="Enter task's last available date"
                            label-for="task_available_till">
<<<<<<< HEAD
                        <b-form-input v-model="task_available_till" type="datetime"/>
                    </b-input-group>

                    <b-input-group
                            prepend="Availability Limit"
=======
                        <b-form-input v-model="task_available_till" type="datetime-local"/>
                    </b-input-group>

                    <b-input-group
                            prepend="Available Times"
>>>>>>> parent of 1b3711fd... Merge remote-tracking branch 'origin/master'
                            class="mt-3"
                            id="task_available_times"
                            label="Enter task's availability limit"
                            label-for="task_available_times">
                        <b-form-input v-model="task_available_times" type="number"/>
                    </b-input-group>

<<<<<<< HEAD
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
=======
                    <b-form-select v-model="task_users" :options="community_members" multiple></b-form-select>

                    <ul id="task_users">
                        <li v-for="user in task_users" :key="user.id">
                            <b-button v-on:click="RemoveTaskUser(user)">{{ user.name }}</b-button>
                        </li>
                    </ul>

                    <b-form-select v-model="task_roles" :options="community_roles" multiple>
                        <template slot="option">
                            <option value="ASasd">asd</option>
                        </template>
                    </b-form-select>

                    <ul id="task_roles">
                        <li v-for="role in task_roles" :key="role.id">
                            <b-button v-on:click="RemoveTaskRole(role.id)">{{ role.Name }}</b-button>
                        </li>
                    </ul>

                    <div class="row">
                        <div class="col">
                            <b-form-select v-model="task_datas" multiple>
                                <option v-for="field in community_data_types" :key="field" :value="field.name">{{ dataTypeName }} - {{ field.name }} ({{ field.type }})
                                </option>
                            </b-form-select>
                        </div>
                        <div class="col">
                            <ul id="task_datas">
                                <li v-for="data in task_datas" :key="data">
                                    <b-button>{{ data }}</b-button>
                                    <b-form-group label="Field Options">
                                        <b-form-checkbox-group
                                                v-model="selected"
                                                :options="field_options"
                                                name="flavour-2a"
                                                stacked
                                        ></b-form-checkbox-group>
                                    </b-form-group>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <b-button v-on:click="createTask()" variant="outline-primary">Create</b-button>
                </div>
            </div>
        </div>
    </div>
>>>>>>> parent of 1b3711fd... Merge remote-tracking branch 'origin/master'

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
                                <b-badge class="mt-1 mr-1" size="sm" variant="dark" v-for="task in task_predecessors" :key="task">
                                    {{ workflow_tasks.find((workflow_task) => {return workflow_task.value === task}).text }}
                                </b-badge>
                            </div>
                        </b-col>
                    </b-row>

                    <hr/>

                    <b-row class="mt-2 mb-2">
                        <b-col class="text-left">
                            <label><strong>Input Fields</strong></label>
                            <b-form-select v-model="task_datas" :options="community_data_types" multiple></b-form-select>
                        </b-col>
                        <b-col class="text-left">
                            <ul id="task_datas">
                                <li v-for="data in task_datas" :key="data">
                                    <b-button>{{ data }}</b-button>
                                    <b-form-group label="Field Options">
                                        <b-form-checkbox-group
                                                v-model="selected"
                                                :options="community_field_options.find((field) => {return field.id === data}).options"
                                                name="flavour-2a"
                                                stacked
                                        ></b-form-checkbox-group>
                                    </b-form-group>
                                </li>
                            </ul>
                        </b-col>
                    </b-row>

                    <b-button v-on:click="createTask()" variant="outline-primary">Create</b-button>
                </div>
            </div>
        </b-col>
    </b-row>
</template>
<script>
    import Community from "../views/Community";
    import Workflow from "../views/Workflow";
    import Tasks from "../views/Tasks";

    export default {
        computed: {
            community: function () {
                return Community.methods.getCommunity(this.$route.params.community_id)
            },
            workflow: function () {
                return Workflow.methods.getWorkflow(this.$route.params.workflow_id)
            }
        },
        data() {
            return {
                community_data: {},
                community_members: [],
                community_roles: [],
                community_data_types: {},
                community_field_options: [],
                task_name: '',
                task_description: '',
                task_available: true,
                task_available_till: null,
                task_available_times: null,
                task_members: [],
                task_roles: [],
                task_data: '',
                task_datas: [],
<<<<<<< HEAD
                task_predecessors: [],
                workflow_tasks: []
=======
>>>>>>> parent of 1b3711fd... Merge remote-tracking branch 'origin/master'
            }
        },
        methods: {
            AddTaskData() {
                this.task_datas.push(this.task_data);
            },
            createTask() {

            },
<<<<<<< HEAD
            async getDataTypes() {
                await Community.methods.getCommunityDataTypes(this.$route.params.community_id).then((data_types) => {
                    let temp = []
                    let temp2 = []

                    data_types.forEach(function (data_type) {
                        if (data_type.Fields.length) {
                            data_type.Fields.forEach(function (field) {
                                temp.push({
                                    value: field.id,
                                    text: data_type.Name + ' - ' + field.Name
                                })

                                temp2.push({
                                    id: field.id,
                                    options: field.Parameters
                                })
                            })
                        }
                    })

                    this.community_data_types = temp

                    this.community_field_options = temp2

                    console.log(this.community_data_types)
                })
            },
            async getMembers() {
                await Community.methods.getCommunityMembers(this.$route.params.community_id).then((members) => {
                    this.community_members = members.map(function (member) {
                        return {value: member.id, text: member.Name}
                    })
                })
            },
            async getRoles() {
                await Community.methods.getCommunityRoles(this.$route.params.community_id).then((roles) => {
                    this.community_roles = roles.map(function (role) {
                        return {value: role.id, text: role.Name}
                    })
                })
=======
            async getMembers(){
                    await Community.methods.getCommunityMembers(this.$route.params.community_id).then((members) => {
                        this.community_members = members.map(function(member){ return {value: member.User.id, text: member.User.name}})
                   })
                   console.log(this.community_members)
>>>>>>> parent of 1b3711fd... Merge remote-tracking branch 'origin/master'
            },
            async getTasks() {
                await Tasks.methods.getTasks(this.$route.params.workflow_id).then((tasks) => {
                    this.workflow_tasks = tasks.map(function (task) {
                        return {value: task.id, text: task.Name}
                    })
                })
            },
        },
<<<<<<< HEAD
        mounted() {
            this.getDataTypes()

            this.getMembers()

            this.getRoles()

            this.getTasks()
=======
        mounted(){
            this.getMembers()

            this.getRoles()
>>>>>>> parent of 1b3711fd... Merge remote-tracking branch 'origin/master'
        }
    }
</script>