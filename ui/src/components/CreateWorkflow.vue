<template>
    <div>
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
      <b-button variant="outline-success">Add</b-button>
    </b-input-group-append>
  </b-input-group>

<ul id="categories">
      <li v-for="role in workflow_roles" :key="role">
        <b-button>{{ role }}</b-button>
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
      <b-button variant="outline-success">Add</b-button>
    </b-input-group-append>
  </b-input-group>
  <ul id="categories">
      <li v-for="member in workflow_assigns" :key="member">
        <b-button >{{ member }}</b-button>
      </li>
    </ul>

     <b-button variant="outline-primary">Create</b-button>
    </div>

</template> 

<script>
  export default {
    
    data() {
        return {
            workflow_name:'',
            workflow_description:'',
            workflow_role:'',
            workflow_roles:[],
            workflow_assign:'',
            workflow_assigns:[]
        }

    }

  }
  </script>