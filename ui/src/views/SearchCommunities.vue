<template>
    <div class="kt-portlet kt-portlet--height-fluid">
        <div class="kt-portlet__head">
            <div class="kt-portlet__head-label">
                <h1 class="kt-portlet__head-title">
                    Searched Communities:
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
    import Community from './Community.vue'
    import axios from 'axios'
    import store from '../store'

    export default {
        store: store,
        name: 'SearchCommunities',
        components: {
            Community
        },
        computed:{
            keyword: function(){
                return this.$route.params.keyword
            }
        },
        data() {
            return {
                communities: []
            }
        },
        methods: {
            async getCommunities() {
                try {
                    const {data} = await axios.post(process.env.VUE_APP_BASE_URL + 'community/search/', {
                        "Name":this.keyword
                        }
                    )

                    if(data.length)
                        this.communities = data

                    else
                        this.$swal("Nothing found!")

                } catch (e) {
                    this.$swal(e.message)
                }
            }
        },
        mounted() {
            if(this.$route.params.keyword)
                this.getCommunities()
        }
    }
</script>

<style scoped>

</style>