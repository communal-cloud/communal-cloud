<template>

    
   
  <div>
  <b-button v-b-modal.step1>Create Community</b-button>
  <b-button v-b-modal.stepTask1>Create Task</b-button>
    <b-button v-b-modal.stepWorkflow1>Create Workflow</b-button>

 <!-- Step 1 Workflow Modal Component -->
  <b-modal  size="lg" hide-footer id="stepWorkflow1" title="Create Workflow">
   
    <b-input-group 
    prepend="Name" 
    class="mt-3"
    id="workflow_name"
    description="description of the community"
    label="Enter workflow name"
    label-for="workflow_name"
   
    >
    <b-form-input v-model="workflow_name" type="text"/>
   
  </b-input-group>

   <b-input-group 
    prepend="Description" 
    class="mt-3"
    id="workflow_description"
    description="description of the workflow"
    label="Enter workflow description"
    label-for="workflow_description"
   
    >
    <b-form-input v-model="workflow_description" type="text"/>
   
  </b-input-group>

  <b-input-group 
    prepend="Allowed Roles" 
    class="mt-3"
    id="workflow_role"
    label="Allowed Roles"
    label-for="workflow_role"
   
    >
    <b-form-input v-model="workflow_role" type="text" />
   <b-input-group-append>
      <b-button v-on:click="AddWorkflowRole" variant="outline-success">Add</b-button>
    </b-input-group-append>
  </b-input-group>

<ul id="categories">
      <li v-for="role in workflow_roles" :key="role">
        <b-button v-on:click="RemoveWorkflowRole(role)">{{ role }}</b-button>
      </li>
    </ul>


    <b-input-group 
    prepend="Assigned Members" 
    class="mt-3"
    id="workflow_assign"
    label="Assigned Members"
    label-for="workflow_assign"
   
    >
    <b-form-input v-model="workflow_assign" type="text" />
   <b-input-group-append>
      <b-button v-on:click="AddWorkflowAssign" variant="outline-success">Add</b-button>
    </b-input-group-append>
  </b-input-group>
  <ul id="categories">
      <li v-for="member in workflow_assigns" :key="member">
        <b-button >{{ member }}</b-button>
      </li>
    </ul>

     <b-button variant="outline-primary">Create</b-button>
  </b-modal>



   <!-- Step 1 Task Modal Component -->
  <b-modal  size="lg" hide-footer id="stepTask1" title="Create Task">
   
    <b-input-group 
    prepend="Name" 
    class="mt-3"
    id="task_name"
    description="description of the community"
    label="Enter task name"
    label-for="task_name"
   
    >
    <b-form-input v-model="task_name" type="text"/>
   
  </b-input-group>

  <b-input-group 
    prepend="Allowed Roles" 
    class="mt-3"
    id="task_role"
    label="Allowed Roles"
    label-for="task_role"
   
    >
    <b-form-input v-model="task_role" type="text" />
   <b-input-group-append>
      <b-button v-on:click="AddTaskRole" variant="outline-success">Add</b-button>
    </b-input-group-append>
  </b-input-group>

<ul id="categories">
      <li v-for="role in task_roles" :key="role">
        <b-button v-on:click="RemoveTaskRole(role)">{{ role }}</b-button>
      </li>
    </ul>


    <b-input-group 
    prepend="Data Type" 
    class="mt-3"
    id="task_data"
    label="Data Type"
    label-for="task_data"
   
    >
    <b-form-input v-model="task_data" type="text" />
   <b-input-group-append>
      <b-button v-on:click="AddTaskData" variant="outline-success">Add</b-button>
    </b-input-group-append>
  </b-input-group>
  <ul id="categories">
      <li v-for="data in task_datas" :key="data">
        <b-button >{{ data }}</b-button>
      </li>
    </ul>

     <b-button  v-on:click="toggleModal('step2'), toggleModal('step3')" variant="outline-primary">Create</b-button>
  </b-modal>



  <!-- Modal Component -->
  <b-modal  size="lg" hide-footer id="step1" title="Add Community  Step 1">
   
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
  <b-modal  size="lg" hide-footer id="step2" title="Add Community  Step 2">
   
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
  <b-modal  size="lg" hide-footer id="step3" title="Add Community  Step 3">
 <b-row class="my-1" >
      <b-col sm="3">
        <label for="dataTypeName">Data Type Name :</label>
      </b-col>
      <b-col sm="9">
        <b-form-input id="dataTypeName" v-model="dataTypeName" type="text"></b-form-input>
      </b-col>
    </b-row>
  <b-list-group >
  <b-list-group-item  href="#" v-for="(data,index) in community_data" :key="data" v-on:click="RemoveInput(data)"> <b-form-input v-model="dataType[(data+'-'+index)]" placeholder="Name of the field"></b-form-input>{{data}}</b-list-group-item>
  </b-list-group> 
  <>
   <b-list-group>
  <b-list-group-item href="#" v-on:click="AddInput('Text')">Text</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('Number')" >Number</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('Image')">Image</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('Date')">Date</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('GeoLocation')" >GeoLocation</b-list-group-item>
  <b-list-group-item href="#" v-on:click="AddInput('Boolean')" >Boolean</b-list-group-item>
</b-list-group>
<b-button   variant="success" v-on:click="CreateDataType">Create Data Type</b-button>
<br></br>
     <b-button class="next" v-on:click="toggleModal('step3'), toggleModal('step4')" variant="outline-primary">Next</b-button>
  </b-modal>




   <!-- Step 4 Modal Component -->
  <b-modal  size="lg" hide-footer id="step4" title="Add Community  Step 4">
   
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
        <b-button v-on:click="AddEmail" variant="outline-success">Invite</b-button>
      </b-input-group-append>
    </b-input-group>
    <ul id="categories">
      <li v-for="email in community_emails" :key="email">
        <b-button v-on:click="RemoveMail(email)">{{ email }}</b-button>
      </li>
    </ul>
    </b-row>

     <b-button class="next" v-on:click=" toggleModal('step')" variant="outline-primary">Finish</b-button>
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
        community_roles:[],
        community_categories:[],
        community_data:[],
        dataTypes:[],
        dataType:{},
        dataTypeName:"",
        email:'',
        community_emails:[],
        task_name:'',
        task_role:'',
        task_roles:[],
        task_data:'',
        task_datas:[],
        workflow_name:'',
        workflow_description:'',
        workflow_role:'',
        workflow_roles:[],
        workflow_assign:'',
        workflow_assigns:[]
      }
    },
    methods:{
      CreateDataType(){
       this.dataTypes.push( {'name' : this.dataTypeName , ...this.dataType} ) 
      },
     AddCategory(){
       this.community_categories.push(this.community_category);
     },
     AddRole(){
       this.community_roles.push(this.community_role);
     },
     AddTaskRole(){
       this.task_roles.push(this.task_role);
     },
     AddWorkflowRole(){
       this.workflow_roles.push(this.workflow_role);
     },
     AddWorkflowAssign(){
       this.workflow_assigns.push(this.workflow_assign);
     },
     AddTaskData(){
       this.task_datas.push(this.task_data);
     },
     AddEmail(){
       this.community_emails.push(this.email);
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
     RemoveTaskRole(){
       
     },
     RemoveMail(){

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