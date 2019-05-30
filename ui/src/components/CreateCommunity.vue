<template>
    <b-row class="row justify-content-center">
        <b-col class="col-xs-12 col-sm-8 col-md-6">
            <div class="card">
                <div class="card-body">
                    <h3 class="card-title">Create Community</h3>

                    <!-- Create Community Step 1 -->
                    <div v-bind:class="{ invisibleStep: step1 }">
                        <b-input-group
                                prepend="Name"
                                class="mt-3"
                                description="name of the community"
                                label="Enter a community name"
                                label-for="name">
                            <b-form-input v-model="community_name" type="text"/>

                        </b-input-group>
                        <b-input-group
                                prepend="Purpose"
                                class="mt-3"
                                label="Purpose"
                                label-for="purpose">
                            <b-form-input v-model="community_purpose" type="text"/>
                        </b-input-group>

                        <b-input-group
                                prepend="Categories"
                                class="mt-3"
                                label="Categories"
                                label-for="categories">
                            <b-form-input v-model="community_category" type="text"/>
                            <b-input-group-append>
                                <b-button v-on:click="AddCategory" variant="btn btn-primary">Add</b-button>
                            </b-input-group-append>
                        </b-input-group>

                        <div id="categories">
                            <a href="javascript:" v-for="category in community_categories" :key="category" v-on:click="RemoveCategory(category)">
                                <b-badge class="mt-1 mr-1" size="sm" variant="dark">
                                    {{ category }}
                                </b-badge>
                            </a>
                        </div>

                        <b-button class="next" v-on:click="changeStep('step1')" variant="btn btn-dark outline-primary m-2">Next
                        </b-button>
                    </div>

                    <div v-bind:class="{ invisibleStep: step2 }">
                        <!-- Create Community Step 2 -->

                        <b-input-group
                                prepend="Description"
                                class="mt-3"
                                description="description of the community"
                                label="Enter description"
                                label-for="description">
                            <b-form-input v-model="community_description" type="text"/>

                        </b-input-group>

                        <b-input-group
                                prepend="Roles"
                                class="mt-3"
                                label="Roles"
                                label-for="roles">
                            <b-form-input v-model="community_role" type="text"/>
                            <b-input-group-append>
                                <b-button v-on:click="AddRole" variant="btn btn-primary">Add</b-button>
                            </b-input-group-append>
                        </b-input-group>

                        <div id="roles">
                            <a href="javascript:" v-for="role in community_roles" :key="role" v-on:click="RemoveRole(role)">
                                <b-badge class="mt-1 mr-1" size="sm" variant="dark">
                                    {{ role }}
                                </b-badge>
                            </a>
                        </div>

                        <b-button class="next" v-on:click="changeStep('step2')" variant="success m-2">Next</b-button>

                    </div>

                    <div v-bind:class="{ invisibleStep: step3 }">
                        <create-data-type :community_id="communityStep.id"></create-data-type>
                        <br />
                        <b-button class="next" v-on:click="changeStep('step3')" variant="success m-2">Finish</b-button>
                    </div>

                    <div v-bind:class="{ invisibleStep: step4 }">
                        <!-- Create Community Step 4 -->
                        <b-row class="my-1">
                            <b-col sm="3">
                                <label for="dataTypeName">Invite People :</label>
                            </b-col>
                            <b-col sm="9">
                                <b-form-input id="dataTypeName" value="https://communal-cloud.com/12321" disabled
                                              type="text"></b-form-input>
                            </b-col>
                        </b-row>
                        <b-row>OR</b-row>
                        <b-row>
                            <b-input-group
                                    prepend="e-mail"
                                    class="mt-3"
                                    id="email"
                                    label="E-mail"
                                    label-for="email">
                                <b-form-input v-model="email" type="email"/>
                                <b-input-group-append>
                                    <b-button v-on:click="AddEmail" variant="btn btn-primary">Invite</b-button>
                                </b-input-group-append>
                            </b-input-group>
                            <ul>
                                <li v-for="email in community_emails" :key="email">
                                    <b-button v-on:click="RemoveMail(email)">{{ email }}</b-button>
                                </li>
                            </ul>
                        </b-row>
                    </div>
                </div>
            </div>
        </b-col>
    </b-row>
</template>

<script>

    import axios from 'axios/index'
    import store from '../store'
    import CreateDataType from './CreateDataType.vue'

    export default {
        components: {

            CreateDataType
        },

        data() {
            return {
                communityStep: {},
                step1: false,
                step2: true,
                step3: true,
                step4: true,
                name: '',
                community_name: '',
                community_purpose: '',
                community_category: '',
                community_description: '',
                community_role: '',

                community_categories: [],

                community_roles: ['owner', 'member'],

                email: '',

                community_emails: []

            }
        },

        methods: {
            async changeStep(step) {
                if (step === 'step1') {
                    if(this.community_name === ''){
                        this.$swal('Community Name cannot be empty!')

                        return false
                    }

                    if(this.community_purpose === ''){
                        this.$swal('Community Purpose cannot be empty!')

                        return false
                    }

                    if(this.community_categories.length === 0){
                        this.$swal('Community Categories cannot be empty!')

                        return false
                    }

                    try {
                        await axios.post(process.env.VUE_APP_BASE_URL + 'community/', {
                                Name: this.community_name,
                                Purpose: this.community_purpose,
                                Categories: this.community_categories
                            },
                            {
                                headers: {
                                    Authorization: 'token ' + store.getters.token
                                }
                            }
                        ).then(data => {
                            this.communityStep = data.data

                            this.$swal("Step 1 completed")

                            this.step1 = true;
                            this.step2 = false;
                        })
                    } catch (e) {
                        this.$swal(e.message)
                    }

                } else if (step === 'step2') {
                    if(this.community_description === ''){
                        this.$swal('Community Description cannot be empty!')

                        return false
                    }

                    try {
                        await axios.put(process.env.VUE_APP_BASE_URL + 'community/' + this.communityStep.id + '/', {
                                Roles: this.community_roles,
                                Description: this.community_description

                            },
                            {
                                headers: {
                                    Authorization: 'token ' + store.getters.token
                                }
                            }
                        ).then(() => {
                            this.$swal("Step 2 completed")

                            this.step2 = true;
                            this.step3 = false;
                        })
                    } catch (e) {
                        this.$swal("Error when updating community")
                    }


                } else if (step === 'step3') {
                    this.step3 = true;
                    this.step4 = false;
                }
            },
            AddCategory() {
                if(this.community_categories.indexOf(this.community_category) === -1)
                    this.community_categories.push(this.community_category);

                else
                    this.$swal("You have already added this category!")
            },
            RemoveCategory(category) {
                if (this.community_categories.indexOf(category) !== -1)
                    this.community_categories.splice(this.community_categories.indexOf(category), 1);
            },
            AddRole() {
                this.community_roles.push(this.community_role);
            },
            RemoveRole(role) {
                if(role === 'owner' || role === 'member')
                    this.$swal('Pre-defined roles cannot be deleted!')

                else if (this.community_roles.indexOf(role) !== -1)
                    this.community_roles.splice(this.community_roles.indexOf(role), 1);
            },
            AddInput(type) {
                this.community_data.push({'type': type, name: ''});
            },
            RemoveInput(type) {

            },
            CreateDataType() {
                this.dataTypes.push({'Name': this.dataTypeName, ...this.dataType})
                console.log(this.dataTypes)
            },
            AddEmail() {
                this.community_emails.push(this.email);
            },
            RemoveMail() {

            },


        }

    }


    /* toggleModal(step) {
      // We pass the ID of the button that we want to return focus to
      // when the modal has hidden
      console.log(this.$refs)
      this.$root.$emit('bv::toggle::modal', step)
     // this.$refs[step].toggle('#'+step)
    }

*/
</script>
<style>
    body {
        background-repeat: repeat !important;
    }
</style>



