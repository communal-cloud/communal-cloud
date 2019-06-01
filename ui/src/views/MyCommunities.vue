<template>
    <div class="kt-portlet kt-portlet--height-fluid">
        <div class="kt-portlet__head">
            <div class="kt-portlet__head-label">
                <h1 class="kt-portlet__head-title">
                    My Communities
                </h1>
            </div>
        </div>
        <div class="kt-portlet__body kt-portlet__body--fluid">
            <b-row v-if="communities.length > 0">
                <b-col cols="4" v-for="community in communities" :key="community.id">
                    <community :id="community.id" :isMyCommunity=true>
                    </community>
                </b-col>
            </b-row>
            <b-row v-else>
                <b-col>
                    <p class="text-black-50">You are not member of any communities.</p>
                </b-col>
            </b-row>
        </div>
    </div>
</template>

<script>
    import Community from './Community.vue'
    import axios from 'axios'
    import store from '../store'

    export default {
        store: store,
        name: 'mycommunities',
        components: {
            Community
        },
        data() {
            return {
                store: store,
                communities: []
            }
        },
        methods: {
            async getCommunities() {
                try {
                    console.log(store.getters.user.id)
                    const {data} = await axios.get(process.env.VUE_APP_BASE_URL + 'member/' + store.getters.user.id + '/communities/', {
                        headers: {
                            Authorization: 'token ' + store.getters.token
                        }
                    })

                    if (data.length > 0)
                        this.communities = data
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
            store.dispatch('fetchUser').then(() => {
                this.getCommunities()
            })
        }
    }
</script>

<style scoped>

</style>