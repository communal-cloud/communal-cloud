<template>
    <div class="kt-portlet kt-portlet--height-fluid">
        <h1 class="m-2">Community Name</h1>
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
                    <router-link :to="'/community/'+this.community_id+'/workflow/create'" class="btn btn-label-brand btn-bold btn-sm">
                        <i class="fa fa-plus-circle"></i> Create Workflow
                    </router-link>
                </div>
            </div>
            <div class="kt-portlet__body kt-portlet__body--fluid">
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
    import Workflow from './Workflow.vue'
    import axios from 'axios'
    import store from '../store'

    export default {
        store: store,
        name: 'workflows',
        components: {
            Workflow
        },
        data() {
            return {
                community_id: 1,
                community: [],
                workflows: []
            }
        },
        computed: {
            createWorkflowPath: function () {
                return "/community/" + this.community_id + "/workflow/create"
            }
        },
        methods:{
            async getWorkflows(){
                try {
                    const {data} = await axios.get(process.env.VUE_APP_BASE_URL+'community/' + this.community_id + '/workflow/', {
                        headers: {
                            Authorization: 'token ' + store.getters.token
                        }
                    })

                    /* const data = [{
                         Name: "Bird Watch",
                         Description:"Watch bird for the community",
                     }]
                     */

                    if(data)
                        this.workflows=data
                } catch (e) {
                    this.$swal(e.message)
                }
            }
        },
        mounted(){
            this.getWorkflows()
        }
    }

</script>

<style scoped>


</style>