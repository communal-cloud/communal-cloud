<template>
    <div class="card" style="width: 22rem;">
        <div class="card-body">
            <h5 class="card-title">{{task.Name}}</h5>
            <p class="card-text">{{task.Description}}</p>
            <a href="#" class="btn btn-primary">Execute</a>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import store from '../store'

    export default {
        props: {
            id: 0
        },
        data() {
            return {
                task: {
                    Name: '',
                    Description: ''
                },
            }
        },
        mounted() {
            this.getTask();
        },
        methods: {
            async getTask() {
                try {
                    /*const {data} = await axios.get(process.env.VUE_APP_BASE_URL + 'task/' + this.id + '/', {
                        headers: {
                            Authorization: 'token ' + store.getters.token
                        }
                    })*/

                    const data = {
                        Name:"Join Us Here",
                        Description:"To join us please fill the form and submit",
                        Available: true,
                        AvailableTill: null,
                        AvailableTimes: 20000,
                        AssignedUsers: [1],
                        AssignedRoles: [],
                        Predecessors: [],
                        InputFields: [],
                        OutputFields: [15, 16 , 20]
                    }

                    console.log(data);

                    this.task = data

                } catch (e) {
                    this.$swal(e.message)
                }
            }
        },
    }
</script>