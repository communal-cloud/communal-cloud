<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="info"  >
      <b-navbar-brand href="#">Communal Cloud</b-navbar-brand>

      <b-navbar-toggle target="nav_collapse"  />

      <b-collapse is-nav id="nav_collapse">
       
       <b-nav-form >
            <b-form-input size="sm" class="mr-sm-2" type="text" placeholder="Search" />
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form>
      

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          
           
            <router-link  class="navSelect" to="/communities">All Communities</router-link> 
         
          
             <router-link  class="navSelect" to="/create">Create Community</router-link>  
            <router-link  class="navSelect" to="/createTask">Create Task</router-link> 
             <router-link  class="navSelect" to="/createWorkflow">Create Workflow</router-link> 
              <router-link  class="navSelect" to="/doTask">Do Task</router-link> 
            
         

          <b-nav-item-dropdown right>
            <!-- Using button-content slot -->
            
            <template slot="button-content"><em>User</em></template>
            <b-dropdown-item href="#">Profile</b-dropdown-item>
            <b-dropdown-item href="#">Signout</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  
}
.form-inline {
      margin-left: 30%;
}
.community {
  height: 200px;
  background-color: antiquewhite;
  justify-content: center;
  text-align: center;
  margin: 10px;
}
.navSelect{
    color: white;
    font-size: 18px;
    vertical-align: middle;
    margin-right: 25px;
    margin-top: 6px;
}
#categories{
  list-style: none;
}
#categories li {
      margin: 5px;
      display: inline-block;
}
.next{
  float: right;
}

.list-group{
      width: 45%;
      display: inline-block !important;
}
pre{
  text-align: left;
}
</style>
