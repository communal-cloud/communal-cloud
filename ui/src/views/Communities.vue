<template>
    <div class="kt-portlet kt-portlet--height-fluid">
        <div class="kt-portlet__head">
            <div class="kt-portlet__head-label">
                <h1 class="kt-portlet__head-title">
                    Available Communities
                </h1>
            </div>
        </div>
        <div class="kt-portlet__body kt-portlet__body--fluid">

            <b-row>
                <b-col cols="4" v-for="community in communities" :key="community.id">
                    <community :id="community.id">
                    </community>
                </b-col>
            </b-row>


        </div>
    </div>
</template>

<script>
    // @ is an alias to /src

    import Community from './Community.vue'
    import axios from 'axios'
    import store from '../store'

    export default {
        store: store,
        name: 'availablecommunities',
        components: {
            Community
        },
        data() {
            return {
                communities: []
            }
        },
        methods: {
            async getCommunities() {
                try {
                    const {data} = await axios.get(process.env.VUE_APP_BASE_URL + 'community/notjoined/', {
                        headers: {
                            Authorization: 'token ' + store.getters.token
                        }
                    })

                    this.communities = data

                } catch (e) {
                    this.$swal(e.message)
                }
            }
        },
        mounted() {
            this.getCommunities()
        }
    }
</script>