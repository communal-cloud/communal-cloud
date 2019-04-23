<template>
<div>   
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

  <b-form-select v-model="task_roles" :options="community_roles" multiple></b-form-select>

<ul id="categories">
      <li v-for="role in task_roles" :key="role">
        <b-button v-on:click="RemoveTaskRole(role)">{{ role }}</b-button>
      </li>
    </ul>

<div class="row"><div class="col">
      <b-form-select v-model="task_datas" multiple >
         <option v-for="field in community_data" :key="field" :value="field.name">{{ dataTypeName }} - {{ field.name }} ({{ field.type }})</option>
      </b-form-select>
    </div>
    <div class="col">
  <ul id="categories">
      <li v-for="data in task_datas" :key="data">
        <b-button >{{ data }}</b-button>
            <b-form-group label="Field Options">
      <b-form-checkbox-group
        v-model="selected"
        :options="field_options"
        name="flavour-2a"
        stacked
      ></b-form-checkbox-group>
    </b-form-group>
      </li>
    </ul>
    </div>
    </div>

     <b-button  v-on:click="toggleModal()" variant="outline-primary">Create</b-button>
</div>

  </template>
  <script>
  import {mapState, mapMutations} from 'vuex';

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
            task_name:'',
            task_role:'',
            task_roles:[],
            task_data:'',
            task_datas:[]
            
        }

    },
    methods : {

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
     
     
     
     
     RemoveTaskRole(){
       
     },
    }

  }
  </script>