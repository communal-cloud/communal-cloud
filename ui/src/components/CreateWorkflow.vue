<template>
    <div class="row justify-content-center">
        <div class="col-xs-12 col-sm-8 col-md-6 col-lg-4">
            <div class="card">
                <div class="card-body">
                    <h3 class="card-title">Create Workflow</h3>
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

                    <b-button variant="info m-4" v-on:click="createWorkflow">Create</b-button>
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
        methods:{
            async createWorkflow(){
                    try {
                        const { data } = await axios.post(process.env.VUE_APP_BASE_URL+'workflow/'+this.$route.params.community_id+'/', {
                            Name: this.workflow_name,
                            Description: this.workflow_description
                        })

                        console.log(data)

                        if(data) {
                            this.$swal("Workflow created")

                            this.$router.push('/community/'+this.$route.params.community_id+'/workflows')
                        }
                    } catch (e) {
                        this.$swal("Error when creating workflow")
                    }
                }
            }
        }
</script>