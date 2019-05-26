<template>

    <div class="card" style="margin: 50px; margin-top: 0px;">
        <div>
            <b-card
                    :title="community.Name"
                    img-src="https://jpublicrelations.com/wp-content/uploads/2015/12/placeholder-1.png.1236x617_default.png"
                    img-alt="Image"
                    img-top
                    tag="article"
                    class="mb-2"
            >
                <b-card-text>
                    {{community.Description}}
                </b-card-text>

                <b-button v-if="this.isMyCommunity" :href="this.getCommunityDetailsPath" variant="info btn-sm">Go To Community</b-button>
                <template v-else>
                    <b-button href="#" variant="info btn-sm">Join Community</b-button>
                </template>
            </b-card>
        </div>
    </div>

</template>

<script>
    import axios from 'axios'
    import store from '../store'

    export default {
        props: {
            id: 0,
            isMyCommunity: false
        },

        data() {
            return {
                community: {
                    Name: '',
                    Purpose: '',
                    Description: ''
                },
            }
        },
        computed: {
            getCommunityDetailsPath: function () {
                return "/community/" + this.id
            }
        },
        mounted() {
            this.getCommunity();
        },
        methods: {
            async getCommunity(id = null) {
                try {
                    if(id === null)
                        id = this.id

                    const {data} = await axios.get(process.env.VUE_APP_BASE_URL + 'community/' + id + '/', {
                        headers: {
                            Authorization: 'token ' + store.getters.token
                        }
                    })

                    return this.community = data

                } catch (e) {
                    this.$swal(e.message)
                }
            },
            async getCommunityMembers(id = null) {
                try {
                    if(id === null)
                        id = this.id

                    const {data} = await axios.get(process.env.VUE_APP_BASE_URL + 'community/' + id + '/members/', {
                        headers: {
                            Authorization: 'token ' + store.getters.token
                        }
                    })

                    return data

                } catch (e) {
                    this.$swal(e.message)
                }
            },
            async getCommunityRoles(id = null) {
                try {
                    if(id === null)
                        id = this.id

                    const {data} = await axios.get(process.env.VUE_APP_BASE_URL + 'community/' + id + '/roles/', {
                        headers: {
                            Authorization: 'token ' + store.getters.token
                        }
                    })

                    return data
                    console.log(data)

                } catch (e) {
                    this.$swal(e.message)
                }
            }
        },
    }
</script>