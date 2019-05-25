<template>

    
   
  <div>
  
  




  <!-- Create Community Step 1 -->
   <div v-bind:class="{ invisibleStep: step1 }">
    <b-input-group 
    prepend="Name" 
    class="mt-3"
    id="name"
    description="name of the community"
    label="Enter a community name"
    label-for="name"
   
    >
    <b-form-input v-model="community_name" type="text"/>
   
  </b-input-group>
   <b-input-group 
    prepend="Purpose" 
    class="mt-3"
    id="purpose"
    label="Purpose"
    label-for="purpose"
   
    >
    <b-form-input v-model="community_purpose" type="text" />
  </b-input-group>

  <b-input-group 
    prepend="Categories" 
    class="mt-3"
    id="categories"
    label="Categories"
    label-for="categories"
   
    >
    <b-form-input v-model="community_category" type="text" />
   <b-input-group-append>
      <b-button v-on:click="AddCategory" variant="btn btn-primary">Add</b-button>
    </b-input-group-append>
  </b-input-group>

<ul id="categories">
      <li v-for="category in community_categories" :key="category">
        <b-button class="btn btn-primary" v-on:click="RemoveCategory(category)">{{ category }}</b-button>
      </li>
    </ul>

     <b-button class="next" v-on:click="changeStep('step1')" variant="btn btn-dark outline-primary">Next</b-button>

   </div>



<div v-bind:class="{ invisibleStep: step2 }">
   <!-- Create Community Step 2 -->
   
    <b-input-group 
    prepend="Description" 
    class="mt-3"
    id="description"
    description="description of the community"
    label="Enter description"
    label-for="description"
   
    >
    <b-form-input v-model="community_description" type="text"/>
   
  </b-input-group>

  <b-input-group 
    prepend="Roles" 
    class="mt-3"
    id="roles"
    label="Roles"
    label-for="roles"
   
    >
    <b-form-input v-model="community_role" type="text" />
   <b-input-group-append>
      <b-button v-on:click="AddRole" variant="btn btn-primary">Add</b-button>
    </b-input-group-append>
  </b-input-group>

<ul id="categories">
      <li v-for="role in community_roles" :key="role">
        <b-button class="btn btn-primary" v-on:click="RemoveRole(role)">{{ role }}</b-button>
      </li>
    </ul>

     <b-button class="next"  v-on:click="changeStep('step2')" variant="btn btn-primary">Next</b-button>

</div>

<div v-bind:class="{ invisibleStep: step3 }">
  <!-- Create Community Step 3 -->
 <b-row class="my-1" >
      <b-col sm="3">
        <label for="dataTypeName">Data Type Name :</label>
      </b-col>
      <b-col sm="9">
        <b-form-input id="dataTypeName" v-model="dataTypeName" type="text"></b-form-input>
      </b-col>
    </b-row>
  <b-list-group >
  <b-list-group-item  href="#" v-for="(data,index) in community_data" :key="index" v-on:click="RemoveInput(data)"> <b-form-input v-model="community_data[index].name" placeholder="Name of the field"></b-form-input>{{data.type}}</b-list-group-item>
  </b-list-group> 
  <>
   <b-list-group>
  <b-list-group-item href="#" v-on:click="AddInput('Text')">Text</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('Number')" >Number</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('Image')">Image</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('Date')">Date</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('GeoLocation')" >GeoLocation</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('Boolean')" >Boolean</b-list-group-item>
   <b-list-group-item href="#" style='background: #eee'>- Add a Data Template -</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('RSVP')" >RSVP</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('QA')" >Question & Answer</b-list-group-item>
</b-list-group>
<b-button   variant="success">+ Add More Data Type</b-button>
<br></br>
     <b-button class="next" v-on:click="changeStep('step3')" variant="outline-primary">Next</b-button>

</div>

<div v-bind:class="{ invisibleStep: step4 }">
     <!-- Create Community Step 4 -->
   
   <b-row class="my-1" >
      <b-col sm="3">
        <label for="dataTypeName">Invite People :</label>
      </b-col>
      <b-col sm="9">
        <b-form-input id="dataTypeName" value="https://communal-cloud.com/12321" disabled type="text"></b-form-input>
      </b-col>
    </b-row>
    <b-row>OR</b-row>
    <b-row>
      <b-input-group 
      prepend="e-mail" 
      class="mt-3"
      id="email"
      label="E-mail"
      label-for="email"
    
      >
      <b-form-input v-model="email" type="email" />
    <b-input-group-append>
        <b-button v-on:click="AddEmail" variant="btn btn-primary">Invite</b-button>
      </b-input-group-append>
    </b-input-group>
    <ul id="categories">
      <li v-for="email in community_emails" :key="email">
        <b-button v-on:click="RemoveMail(email)">{{ email }}</b-button>
      </li>
    </ul>
    </b-row>

     <b-button class="next"  variant="outline-primary">Finish</b-button>
    
    </div>


</div>



</template>

<script>
import {mapState, mapMutations} from 'vuex';
import axios from 'axios/index';


  export default {
    computed: {
   ...mapState([
     'community_roles',
     'community_data',
     'dataTypeName'
   ])
    },
    
    data() {
      return {
        step1:false,
        step2:true,
        step3:true,
        step4:true,
        name: '',
        community_name : '',
        community_purpose : '',
        community_category : '',
        community_description:'',
        community_role:'',
        
        community_categories:[],
        dataTypes:[],
        dataType:{},
        
        email:'',
        field_options: ['Required', 'Human Input', 'Saved'],
        community_emails:[]
       
      }
    },
    
    methods:{
     async changeStep(step){
         if(step == 'step1'){
             this.step1=true;
             this.step2=false;
             console.log(this.community_categories)

              try {
                        const { data } = await axios.post(process.env.VUE_APP_BASE_URL+'community/', {
                                Name: this.community_name,
                                Description: this.community_purpose,
                                Categories: this.community_categories
                        })

                        if(data)
                            this.$swal("Community created")
                    } catch (e) {
                        this.$swal("Error when adding community")
                    }

         }else if(step=='step2'){
             this.step2=true;
             this.step3=false;
         }else if(step=='step3'){
             this.step3=true;
             this.step4=false;
         }
     },
     AddCategory(){
       this.community_categories.push(this.community_category);
     },
     RemoveCategory(){

     },
     AddRole(){
       this.community_roles.push(this.community_role);
     },
     RemoveRole(){
       
     },
     AddInput(type){
       this.community_data.push({'type' : type, name: ''});
     },
     RemoveInput(type){

     },
     CreateDataType(){
       this.dataTypes.push( {'name' : this.dataTypeName , ...this.dataType} ) 
       console.log(this.dataTypes)
     },
     AddEmail(){
       this.community_emails.push(this.email);
     },
     RemoveMail(){

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




