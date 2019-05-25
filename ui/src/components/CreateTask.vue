<template>
    <div>
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

        <b-form-checkbox v-model="task_available" name="check-button" switch>
            Available <b>({{ (checked) ? 'Yes' : 'No' }})</b>
        </b-form-checkbox>

        <b-input-group
                prepend="Available Till"
                class="mt-3"
                id="task_available_till"
                label="Enter task's last available date"
                label-for="task_available_till">
            <b-form-input v-model="task_available_till" type="datetime"/>
        </b-input-group>

        <b-input-group
                prepend="Available Times"
                class="mt-3"
                id="task_available_times"
                label="Enter task's availability limit"
                label-for="task_available_times">
            <b-form-input v-model="task_available_times" type="number"/>
        </b-input-group>

        <b-form-select v-model="task_users" :options="community_users" multiple></b-form-select>

        <ul id="task_users">
            <li v-for="user in task_users" :key="user.id">
                <b-button v-on:click="RemoveTaskUser(user)">{{ user.name }}</b-button>
            </li>
        </ul>

        <b-form-select v-model="task_roles" :options="community_roles" multiple></b-form-select>

        <ul id="task_roles">
            <li v-for="role in task_roles" :key="role">
                <b-button v-on:click="RemoveTaskRole(role)">{{ role }}</b-button>
            </li>
        </ul>

        <div class="row">
            <div class="col">
                <b-form-select v-model="task_datas" multiple>
                    <option v-for="field in community_data" :key="field" :value="field.name">{{ dataTypeName }} - {{ field.name }} ({{ field.type }})
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

</template>
<script>
    import Community from "../views/Community";

    export default {
        data() {
            return {
                community_users: {},
                community_roles: {},
                community_data: {},
                task_name: '',
                task_description: '',
                task_available: false,
                task_available_till: null,
                task_available_times: null,
                task_users: [],
                task_roles: [],
                task_data: '',
                task_datas: [],
                checked:false
            }
        },
        methods: {
            AddTaskUser() {
                this.task_users.push(this.task_user);
            },
            RemoveTaskUser(user) {
                this.task_users.find(user).remove();
            },
            AddTaskRole() {
                this.task_roles.push(this.task_role);
            },
            RemoveTaskRole(role) {
                this.task_roles.find(role).remove();
            },
            AddTaskData() {
                this.task_datas.push(this.task_data);
            },
            createTask() {

            },
        }

    }
</script>