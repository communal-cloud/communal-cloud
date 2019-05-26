<template>
    <div class="kt-portlet kt-portlet--height-fluid">
        <h1 class="m-2" v-if="community">{{ community.Name }}</h1>
        <h5>{{ community.Purpose }}</h5>
        <p>{{ community.Description }}</p>



        <div class="kt-portlet kt-portlet--height-fluid">
            <div class="kt-portlet__head">
                <div class="kt-portlet__head-label">
                    <h3 class="kt-portlet__head-title">
                        Available Workflows
                    </h3>
                </div>
                <div class="kt-portlet__head-toolbar">
                    <router-link v-if="community" :to="'/community/'+community.id+'/workflow/create'" class="btn btn-label-brand btn-bold btn-sm">
                        <i class="fa fa-plus-circle"></i> Create Workflow
                    </router-link>
                </div>
            </div>
            <div class="kt-portlet__body kt-portlet__body--fluid" v-if="workflows">
                <b-row>
                    <b-col cols="4" v-for="workflow in workflows" :key="workflow.id">
                        <workflow :workflow="workflow"></workflow>
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
                this.community = await Community.methods.getCommunity(this.$route.params.community_id)
            },
            async getWorkflows(){
                this.workflows = await Workflows.methods.getWorkflows(this.$route.params.community_id)
            },
        },
        mounted(){
            this.getCommunity()

            this.getWorkflows()
        }
    }

</script>

<style scoped>


</style>