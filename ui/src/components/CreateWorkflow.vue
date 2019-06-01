<template>
    <div class="row justify-content-center">
        <div class="col-xs-12 col-sm-8 col-md-6 col-lg-4">
            <div class="card">
                <div class="card-body">
                    <h3 v-if="workflowUpdate !== undefined" class="card-title">Update Workflow</h3>
                    <h3 v-else class="card-title">Create Workflow</h3>
                    <b-input-group
                            prepend="Name"
                            class="mt-3"
                            id="workflow_name"
                            description="description of the community"
                            label="Enter workflow name"
                            label-for="workflow_name">
                        <b-form-input v-model="workflow_name" type="text"/>

                    </b-input-group>

                    <b-input-group
                            prepend="Description"
                            class="mt-3"
                            id="workflow_description"
                            description="description of the workflow"
                            label="Enter workflow description"
                            label-for="workflow_description">
                        <b-form-input v-model="workflow_description" type="text"/>

                    </b-input-group>

                    <b-button v-if="workflowUpdate !== undefined" variant="info m-4" v-on:click="updateWorkflow">Update</b-button>
                    <b-button v-else variant="info m-4" v-on:click="createWorkflow">Create</b-button>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
    import axios from 'axios'
    import store from '../store'

    export default {
        data() {
            return {
                workflow_name: '',
                workflow_description: ''
            }
        },
        props: {
            workflowUpdate: {}
        },
        methods: {
            async updateWorkflow() {
                try {
                    const {data} = await axios.put(process.env.VUE_APP_BASE_URL + 'workflow/' + this.workflowUpdate.id + '/', {
                        Name: this.workflow_name,
                        Description: this.workflow_description
                    })

                    if (data) {
                        this.$swal('Success!', "Workflow updated", 'success')
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
            async createWorkflow() {
                if (this.workflow_name === '') {
                    this.$swal('Error!', 'Workflow Name cannot be empty!', 'error')

                    return false
                }

                if (this.workflow_description === '') {
                    this.$swal('Error!', 'Workflow Description cannot be empty!', 'error')

                    return false
                }

                try {
                    await axios.post(process.env.VUE_APP_BASE_URL + 'workflow/' + this.$route.params.community_id + '/', {
                        Name: this.workflow_name,
                        Description: this.workflow_description
                    }).then((data) => {
                        if (data.data) {
                            this.$swal('Success!', "Workflow created", 'success')

                            this.$router.push('/community/' + this.$route.params.community_id + '/workflows')
                        }
                    })
                } catch (e) {
                    if (e.response.status !== 500) {
                        Object.keys(e.response.data).forEach(key => {
                            this.$swal(key, e.response.data[key][0], 'error')
                        })
                    } else
                        this.$swal('Server Error!', e.message, 'error')
                }
            }
        },
        mounted() {
            if (this.workflowUpdate !== undefined) {
                this.workflow_name = this.workflowUpdate.Name
                this.workflow_description = this.workflowUpdate.Description
            }
        }
    }
</script>