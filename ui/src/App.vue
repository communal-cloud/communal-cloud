<template>
  <div id="app">
    <!--<b-navbar toggleable="lg" type="dark" variant="info"  >
      <b-navbar-brand href="#">Communal Cloud</b-navbar-brand>

      <b-navbar-toggle target="nav_collapse"  />

      <b-collapse is-nav id="nav_collapse">
       
       <b-nav-form >
            <b-form-input size="sm" class="mr-sm-2" type="text" placeholder="Search" />
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form>
      

        <b-navbar-nav class="ml-auto">
          
           
            <router-link  class="navSelect" to="/communities">All Communities</router-link> 
         
          
             <router-link  class="navSelect" to="/create">Create Community</router-link>  
            <router-link  class="navSelect" to="/createTask">Create Task</router-link> 
             <router-link  class="navSelect" to="/createWorkflow">Create Workflow</router-link> 
              <router-link  class="navSelect" to="/doTask">Do Task</router-link> 
            
         

          <b-nav-item-dropdown right>

            <template slot="button-content"><em>User</em></template>
            <b-dropdown-item href="#">Profile</b-dropdown-item>
            <b-dropdown-item href="#">Signout</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>-->

    <!-- begin:: Header Mobile -->
    <div id="kt_header_mobile" class="kt-header-mobile  kt-header-mobile--fixed ">
      <div class="kt-header-mobile__logo">
        <router-link to="/">
          <img alt="Logo" src="/assets/media/logos/logo.png" />
        </router-link>
      </div>
      <div class="kt-header-mobile__toolbar">
        <button class="kt-header-mobile__toolbar-toggler" id="kt_header_mobile_toggler"><span></span></button>
        <button class="kt-header-mobile__toolbar-topbar-toggler" id="kt_header_mobile_topbar_toggler"><i class="flaticon-more-1"></i></button>
      </div>
    </div>

    <!-- end:: Header Mobile -->
    <div class="kt-grid kt-grid--hor kt-grid--root">
      <div class="kt-grid__item kt-grid__item--fluid kt-grid kt-grid--ver kt-page">
        <div class="kt-grid__item kt-grid__item--fluid kt-grid kt-grid--hor kt-wrapper " id="kt_wrapper">

          <!-- begin:: Header -->
          <div id="kt_header" class="kt-header  kt-header--fixed " data-ktheader-minimize="on">
            <div class="kt-container">

              <!-- begin:: Brand -->
              <div class="kt-header__brand   kt-grid__item" id="kt_header_brand">
                <router-link class="kt-header__brand-logo" to="/">
                  <img alt="Logo" src="/assets/media/logos/logo-white.png" width="140" class="kt-header__brand-logo-default" />
                  <img alt="Logo" src="/assets/media/logos/logo.png" width="100" class="kt-header__brand-logo-sticky" />
                </router-link>
              </div>

              <!-- end:: Brand -->

              <!-- begin: Header Menu -->
              <button class="kt-header-menu-wrapper-close" id="kt_header_menu_mobile_close_btn"><i class="la la-close"></i></button>
              <div class="kt-header-menu-wrapper kt-grid__item kt-grid__item--fluid" id="kt_header_menu_wrapper">
                <div id="kt_header_menu" class="kt-header-menu kt-header-menu-mobile">
                  <ul class="kt-menu__nav ">
                    <li class="kt-menu__item" v-if="store.getters.check">
                      <router-link  class="kt-menu__link" to="/communities"><span class="kt-menu__link-text">All Communities</span></router-link>
                    </li>
                    <li class="kt-menu__item" v-if="store.getters.check">
                      <router-link  class="kt-menu__link" to="/create"><span class="kt-menu__link-text">Create Community</span></router-link>
                    </li>
                    <li class="kt-menu__item" v-if="store.getters.check">
                      <router-link  class="kt-menu__link" to="/createTask"><span class="kt-menu__link-text">Create Task</span></router-link>
                    </li>
                    <li class="kt-menu__item" v-if="store.getters.check">
                      <router-link  class="kt-menu__link" to="/createWorkflow"><span class="kt-menu__link-text">Create Workflow</span></router-link>
                    </li>
                    <li class="kt-menu__item" v-if="store.getters.check">
                      <router-link  class="kt-menu__link" to="/doTask"><span class="kt-menu__link-text">Do Task</span></router-link>
                    </li>
                    <li class="kt-menu__item" v-if="!store.getters.check">
                      <router-link  class="kt-menu__link" to="/user/login"><span class="kt-menu__link-text">Login</span></router-link>
                    </li>
                    <li class="kt-menu__item" v-if="!store.getters.check">
                      <router-link  class="kt-menu__link" to="/user/register"><span class="kt-menu__link-text">Register</span></router-link>
                    </li>
                  </ul>
                </div>
              </div>

              <!-- end: Header Menu -->

              <!-- begin:: Header Topbar -->
              <div class="kt-header__topbar kt-grid__item">

                <!--begin: User bar -->
                <div class="kt-header__topbar-item kt-header__topbar-item--user" v-if="store.getters.check">
                  <div class="kt-header__topbar-wrapper" data-toggle="dropdown" data-offset="10px,0px">
                    <span class="kt-header__topbar-welcome">Hi,</span>
                    <span class="kt-header__topbar-username">{{ store.getters.user.name }}</span>
                  </div>
                  <div class="dropdown-menu dropdown-menu-fit dropdown-menu-right dropdown-menu-anim dropdown-menu-xl">
                    <!--begin: Navigation -->
                    <div class="kt-notification">
                      <div class="kt-notification__custom">
                        <router-link to="/user/logout" class="btn btn-label-brand btn-sm btn-bold">Sign Out</router-link>
                      </div>
                    </div>

                    <!--end: Navigation -->
                  </div>
                </div>

                <!--end: User bar -->
              </div>

              <!-- end:: Header Topbar -->
            </div>
          </div>

          <!-- end:: Header -->
          <div class="kt-grid__item kt-grid__item--fluid kt-grid kt-grid--ver kt-grid--stretch">
            <div class="kt-container kt-body  kt-grid kt-grid--ver" id="kt_body">
              <div class="kt-grid__item kt-grid__item--fluid kt-grid kt-grid--hor">
                <router-view :key="$route.fullPath"></router-view>
              </div>
            </div>
          </div>
          <!-- begin:: Footer -->
          <div class="kt-footer  kt-footer--extended  kt-grid__item" id="kt_footer" style="background-image: url('assets/media/bg/bg-2.jpg');">
            <div class="kt-footer__bottom">
              <div class="kt-container">
                <div class="kt-footer__wrapper">
                  <div class="kt-footer__logo">
                    <router-link class="kt-header__brand-logo" to="/">
                      <img alt="Logo" src="/assets/media/logos/logo-white.png" width="140" class="kt-header__brand-logo-sticky">
                    </router-link>
                    <div class="kt-footer__copyright">
                      2019&nbsp;&copy;&nbsp;
                      Communal Cloud
                    </div>
                  </div>
                  <div class="kt-footer__menu">
                    <a href="http://git.communal-cloud.com" target="_blank">Git</a>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- end:: Footer -->
        </div>
      </div>
    </div>
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

<script>
  import store from './store'

  export default {
    store:store,
    data: () => ({
      store:store
    })
  }
</script>