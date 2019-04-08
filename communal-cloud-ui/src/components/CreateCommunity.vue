<template>

    
   
  <div>
  <b-button v-b-modal.step1>Create Community</b-button>

  <!-- Modal Component -->
  <b-modal  size="lg" hide-footer id="step1" title="Community Info">
   
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
      <b-button v-on:click="AddCategory" variant="outline-success">Add</b-button>
    </b-input-group-append>
  </b-input-group>

<ul id="categories">
      <li v-for="category in community_categories" :key="category">
        <b-button v-on:click="RemoveCategory(category)">{{ category }}</b-button>
      </li>
    </ul>

     <b-button class="next" v-on:click="toggleModal('step1'), toggleModal('step2')" variant="outline-primary">Next</b-button>
  </b-modal>



   <!-- Step 2 Modal Component -->
  <b-modal  size="lg" hide-footer id="step2" title="Community Details">
   
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
      <b-button v-on:click="AddRole" variant="outline-success">Add</b-button>
    </b-input-group-append>
  </b-input-group>

<ul id="categories">
      <li v-for="role in community_roles" :key="role">
        <b-button v-on:click="RemoveRole(role)">{{ role }}</b-button>
      </li>
    </ul>

     <b-button class="next" v-on:click="toggleModal('step2'), toggleModal('step3')" variant="outline-primary">Next</b-button>
  </b-modal>




   <!-- Step 3 Modal Component -->
  <b-modal  size="lg" hide-footer id="step3" title="Community Data Types">
 
  <b-list-group >
    <b-input-group 
    prepend="Data Type Name" 
    class="mt-3"
    id="data_type"
   
    ><b-form-input v-model="data_type_name" type="text" /></b-input-group>
  <b-list-group-item  href="#" v-for="data in community_data" :key="data" v-on:click="RemoveInput(data)">{{data}}</b-list-group-item>
  <b-list-group-item  href="#" style="background: #eee">+ Add Another Data Type</b-list-group-item>
  </b-list-group> 
   <b-list-group>
  <b-list-group-item href="#" v-on:click="AddInput('Text')">Text</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('Number')" >Number</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('Image')">Image</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('Date')">Date</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('GeoLocation')" >GeoLocation</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('Boolean')" >Boolean</b-list-group-item>
  <b-list-group-item style="background: #eee">- Data Templates -</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('RSVP')">RSVP</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('QA')" >Question & Answer</b-list-group-item>
</b-list-group>

     <b-button class="next" v-on:click="toggleModal('step3'), toggleModal('step4')" variant="outline-primary">Next</b-button>
  </b-modal>
  
   <!-- Step 4 Modal Component -->
  <b-modal  size="lg" hide-footer id="step4" title="Community Tasks">
 
 <b-input-group 
    prepend="Task Name" 
    class="mt-3"
    id="data_type"
   
    ><b-form-input type="text" v-model="task_name" /></b-input-group>
	<p>{{data_type_name}}</p>
  <b-list-group >
  <b-list-group-item  href="#" v-for="data in community_data" :key="data" v-on:click="RemoveInput(data)">{{data}}</b-list-group-item>
  </b-list-group> 

     <b-button class="next" v-on:click="toggleModal('step4')" variant="outline-primary">Next</b-button>
  </b-modal>
</div>



</template>

<script>


  export default {
    computed: {
    },
    data() {
      return {
        name: '',
        community_name : '',
        community_purpose : '',
        community_category : '',
        community_description:'',
        community_role:'',
        community_roles:['owner', 'member'],
        community_categories:[],
        community_data:[],
		data_type_name: '',
		task_name: ''
      }
    },
    methods:{
     AddCategory(){
       this.community_categories.push(this.community_category);
     },
     AddRole(){
       this.community_roles.push(this.community_role);
     },
     AddInput(type){
       this.community_data.push(type);
     },
     RemoveInput(type){

     },
     RemoveCategory(){

     },
     RemoveRole(){
       
     },
     toggleModal(step) {
        // We pass the ID of the button that we want to return focus to
        // when the modal has hidden
        console.log(this.$refs)
        this.$root.$emit('bv::toggle::modal', step)
       // this.$refs[step].toggle('#'+step)
      }
     
    }
          
               }
</script>