<template>



        

        <div >
            <!-- Create Community Step 3 -->
            <b-row class="my-1">
                <b-col sm="3">
                    <label for="dataTypeName">Data Type Name :</label>
                </b-col>
                <b-col sm="9">
                    <b-form-input id="dataTypeName" v-model="dataTypeName" type="text"></b-form-input>
                </b-col>
            </b-row>
            <b-list-group class="mr-2">
                <b-list-group-item class="mb-1" href="#" v-for="(data,index) in community_data" :key="index"
                                   v-on:click="RemoveInput(data)">
                    <b-form-input v-model="community_data[index].name" placeholder="Name of the field"></b-form-input>
                    {{data.type}}
                </b-list-group-item>
            </b-list-group>
            <b-list-group>
                <b-list-group-item href="#" v-on:click="AddInput('Text')">Text</b-list-group-item>
                <b-list-group-item href="#" v-on:click="AddInput('Number')">Number</b-list-group-item>
                <b-list-group-item href="#" v-on:click="AddInput('Image')">Image</b-list-group-item>
                <b-list-group-item href="#" v-on:click="AddInput('Date')">Date</b-list-group-item>
                <b-list-group-item href="#" v-on:click="AddInput('GeoLocation')">GeoLocation</b-list-group-item>
                <b-list-group-item href="#" v-on:click="AddInput('Boolean')">Boolean</b-list-group-item>
                <b-list-group-item href="#" style='background: #eee'>- Add a Data Template -</b-list-group-item>
                <b-list-group-item href="#" v-on:click="AddInput('RSVP')">RSVP</b-list-group-item>
                <b-list-group-item href="#" v-on:click="AddInput('QA')">Question & Answer</b-list-group-item>
            </b-list-group>
            <b-button variant="success m-3">+ Add More Data Type</b-button>
            <br>
            <b-button class="next" v-on:click="create()" variant="success m-2">Create</b-button>

        </div>

     





</template>

<script>

    import axios from 'axios/index';
    import store from '../store'

    export default {
        props:{
            community_id:0
        },
        data() {
            return {
                
           
              
               
                dataTypeName: "",
                community_categories: [],
                dataTypes: [],
                dataType: {},
                community_roles: ['owner', 'member'],
                community_data: [],
                email: '',
                field_options: ['Required', 'Human Input', 'Saved'],
                community_emails: []

            }
        },

        methods: {
            async create() {
                

                    this.community_data = this.community_data.map(function (item) {
                        if (item.type == "Number") {
                            item.type = 1
                        }
                        else if (item.type == "Text") {
                            item.type = 2
                        }
                        else if (item.type == "Image") {
                            item.type = 8
                        }
                        else if (item.type == "Date") {
                            item.type = 4
                        }
                        else if (item.type == "GeoLocation") {
                            item.type = 5
                        }
                        else if (item.type == "Boolean") {
                            item.type = 3
                        }


                        return {Name: item.name, Class: item.type};
                    })

                    console.log(this.community_data)
                    try {
                        const {data} = await axios.post(process.env.VUE_APP_BASE_URL + 'data/' + this.community_id + '/', {
                            Name: this.dataTypeName,
                            Fields: this.community_data


                        },
                            {
                                headers: {
                                    Authorization: 'token ' + store.getters.token
                                }
                            })

                        if (data)
                            console.log(data)
                        

                    } catch (e) {
                        this.$swal("Error when creating data type")
                    }


                
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



