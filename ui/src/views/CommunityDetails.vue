<template>
    <div class="kt-portlet kt-portlet--height-fluid">
        <h1 class="m-2" v-if="community">{{ community.Name }}</h1>
        <h5>123 Members</h5>
        <h5>Category: Example Category</h5>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ex felis, convallis at tellus et,
            consectetur molestie lacus. Vivamus bibendum tristique elit. Fusce volutpat enim in nunc blandit, id cursus
            arcu suscipit. In facilisis, metus quis dictum malesuada, lorem metus tincidunt mi, nec fermentum massa
            lorem venenatis nisl. Etiam at quam mattis, luctus nulla sit amet, efficitur tortor. Praesent ut purus orci.
            Pellentesque condimentum lobortis convallis. Quisque semper, enim vel feugiat rhoncus, erat justo
            ullamcorper nibh, eu molestie felis sem et turpis. Quisque risus magna, varius a dui eget, congue rutrum
            odio. Donec pharetra pretium lacus, ac ornare magna auctor eget. Orci varius natoque penatibus et magnis dis
            parturient montes, nascetur ridiculus mus. Donec consequat orci consectetur porta commodo. Duis faucibus
            purus vel consequat laoreet.</p>



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