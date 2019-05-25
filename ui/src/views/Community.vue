<template>

<<<<<<< HEAD
<div class="card" style="width: 32rem;">
  <div class="card-body">
    <h5 class="card-title">{{community.Name}}</h5>
     <h6 class="card-subtitle mb-2 text-muted">{{community.Purpose}}</h6>
    <p class="card-text">{{community.Description}}</p>
    <a href="#" class="btn btn-primary">Explore</a>
  </div>
</div>
=======
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

                <b-button href="#" variant="info btn-sm">Join Community</b-button>
            </b-card>
        </div>
    </div>
>>>>>>> 500a0e24d6a7a100397c96b3d4b1912153c585c4

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
                community: {
                    Name: '',
                    Purpose: '',
                    Description: ''
                },

            }
        },
        mounted() {
            this.getCommunity();
        },
        methods: {
            async getCommunity() {
                try {
                    const {data} = await axios.get(process.env.VUE_APP_BASE_URL + 'community/' + this.id + '/', {
                        headers: {
                            Authorization: 'token ' + store.getters.token
                        }
                    })
                    console.log(data);
                    this.community = data

                } catch (e) {
                    this.$swal(e.message)
                }
            }
        },
    }
</script>