<template>
    <div class="card" style="width: 22rem;">
        <div class="card-body">
            <h5 class="card-title">{{workflow.Name}}</h5>
            <p class="card-text">{{workflow.Description}}</p>
            <router-link :to="'/workflow/'+workflow.id+'/tasks/'" class="btn btn-primary">Execute</router-link>
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
        mounted() {
            /*this.getWorkflow(); */
        },
        /*methods: {
            async getWorkflow() {
                try {
                    /*const {data} = await axios.get(process.env.VUE_APP_BASE_URL + 'workflow/' + this.id + '/', {
                        headers: {
                            Authorization: 'token ' + store.getters.token
                        }
                    })

                    const data = {
                        Name: "Bird Watch",
                        Description:"Watch bird for the community",
                    }

                    console.log(data);

                    this.workflow = data

                } catch (e) {
                    this.$swal(e.message)
                }
            }
        }, */
    }
</script>