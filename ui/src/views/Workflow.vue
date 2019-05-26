<template>
    <div class="card m-4 border border-primary" style="width: 22rem;">
        <div class="card-body">
            <h5 class="card-title">{{workflow.Name}}</h5>
            <p class="card-text">{{workflow.Description}}</p>
            <router-link :to="'/community/'+workflow.Community+'/workflow/'+workflow.id+'/tasks/'" class="btn btn-primary">Tasks</router-link>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import store from '../store'

    export default {
        props: {
            workflow:{}
        },
        data() {
            return {
                
            }
        },
        methods: {
            async getWorkflow(id = null) {
                try {
                    if(id === null)
                        id = this.workflow.id

                    const {data} = await axios.get(process.env.VUE_APP_BASE_URL + 'workflow/' + id + '/', {
                        headers: {
                            Authorization: 'token ' + store.getters.token
                        }
                    })

                    /*const data = {
                        Name: "Bird Watch",
                        Description:"Watch bird for the community",
                    }*/

                    console.log(data);

                    this.workflow = data

                } catch (e) {
                    this.$swal(e.message)
                }
            }
        },
    }
</script>