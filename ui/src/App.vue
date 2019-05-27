<template>
  <div id="app">
    <!-- begin:: Header Mobile -->
    <div id="kt_header_mobile" class="kt-header-mobile  kt-header-mobile--fixed ">
      <div class="kt-header-mobile__logo">
        <router-link to="/">
          <img alt="Logo" width="140" src="/assets/media/logos/logo.png" />
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
                <div id="kt_header_menu" style="width: 100%;" class="kt-header-menu kt-header-menu-mobile">
                  <ul class="kt-menu__nav " >
                    <li class="kt-menu__item" v-if="store.getters.check">
                      <router-link  class="kt-menu__link" to="/communities"><span class="kt-menu__link-text">All Communities</span></router-link>
                    </li>
                    <li class="kt-menu__item" v-if="store.getters.check">
                      <router-link  class="kt-menu__link" to="/communities/my"><span class="kt-menu__link-text">My Communities</span></router-link>
                    </li>
                    <li class="kt-menu__item" v-if="store.getters.check">
                      <router-link  class="kt-menu__link" to="/community/create"><span class="kt-menu__link-text">Create Community</span></router-link>
                    </li>
                  </ul>
                  <b-nav-form v-if="store.getters.check">
                    <b-form-input v-model="search" size="sm" class="mr-sm-2" placeholder="Search Community"></b-form-input>
                    <router-link :to="'/search/communities/'+search">
                    <b-button size="sm" class="my-2 my-sm-0 searchButton" type="submit">Search</b-button>
                    </router-link>
                  </b-nav-form>
                </div>
              </div>

              <!-- end: Header Menu -->

              <!-- begin:: Header Topbar -->
              <div class="kt-header__topbar kt-grid__item">

                <!--begin: User bar -->
                <div class="kt-header__topbar-item kt-header__topbar-item--user" v-if="store.getters.check">
                  <div class="kt-header__topbar-wrapper">
                    <span class="kt-header__topbar-welcome">Hi,</span>
                    <span class="kt-header__topbar-username">{{ store.getters.user.name }}</span>
                    <a class="kt-header__topbar-username" v-on:click="logout"><i class="fa fa-sign-out-alt"></i></a>
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
      margin-left: 35%;
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

.searchButton{
  background-color: white;
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



      data() {
          return {
              store:store,
              search:""

          }
      },
    methods: {
      logout(){
        store.dispatch('logout')

        this.$swal("Successfully logged out!")

        this.$router.push('/user/login')
      }
    }
  }
</script>