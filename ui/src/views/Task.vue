<template>
    <div class="card border border-success m-4" style="width: 32rem;">
         <b-button class="mt-3" block @click="$bvModal.show(modalID+'edit')" >Edit</b-button>
        <div class="card-body">
            <h2 class="card-title">{{task.Name}}</h2>
            <p class="card-text">{{task.Description}}</p>
            <h6 class="card-text">Available executions: {{task.AvailableTimes}}</h6>
            <h5 class="card-text">Assigned Roles: {{task.AssignedRoles.map(({ Name }) => Name)}}</h5>
            <h5 class="card-text">Assigned Users: {{task.AssignedUsers.map(({ Name }) => Name)}}</h5>
            <h5 class="card-text">Predecessors Tasks: {{task.Predecessors.map(({ Name }) => Name)}}</h5>

            <b-button id="show-btn" variant="danger mr-2 btn-sm" >Delete</b-button>
              <b-button id="show-btn" variant="success" @click="$bvModal.show(modalID)">Execute</b-button>
        </div>
    
<div>




  <b-modal :id="modalID+'edit'" size="xl" hide-footer>
    <template slot="modal-title">
       <code>{{task.Name}}</code> 
       
    </template>
   
      <create-task :taskUpdate="task"></create-task>
  
    <b-button class="mt-3" block @click="$bvModal.hide(modalID+'edit')">Close Me</b-button>
  </b-modal>



  <b-modal :id="modalID" hide-footer>
    <template slot="modal-title">
       <code>{{task.Name}}</code> 
       
    </template>
    <div class="d-block text-center">
      <execute-task :task="task" :execute="execution"></execute-task>
    </div>
    <b-button class="mt-3" block @click="$bvModal.hide(modalID)">Close Me</b-button>
  </b-modal>
</div>
    


    </div>
</template>

<script>
    import axios from 'axios'
    import store from '../store'
    import ExecuteTask from '../components/ExecuteTask.vue'
    import CreateTask from '../components/CreateTask.vue'
    import { exec } from 'child_process';

    export default {
        components: {
            ExecuteTask,CreateTask
        },
        props: {
            id: 0,
            task:{}
        },
        data() {
            return {
                
            }
        },
        computed:{
            modalID: function(){
                console.log(String(this.id))
                return String(this.id)
            },
            execution: function(){
                var execute={};
                execute=this.task.OutputFields.map(function(item) {
                  if(item.Type=="1")
                  {
                    item.Type="number"
                  }
                  else if(item.Type=="2")
                  {
                    item.Type='text'
                  }
                  else if(item.Type=="8")
                  {
                    item.Type='img'
                  }
                  else if(item.Type=="4")
                  {
                    item.Type='date'
                  }
                  else if(item.Type=="5")
                  {
                    item.Type='geolocation'
                  }
                  else if(item.Type=="3")
                  {
                    item.Type='boolean'
                  }
            
                   return { Name: item.Name, Class : item.Type };
              })
               return execute
        }
        },

        mounted() {
            //this.getTask();
        },
       /* methods: {
            async getTask() {
                try {
                    const {data} = await axios.get(process.env.VUE_APP_BASE_URL + 'task/' + this.id + '/', {
                        headers: {
                            Authorization: 'token ' + store.getters.token
                        }
                    })

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
        },*/
    }
</script>