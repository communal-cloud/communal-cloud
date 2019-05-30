import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import VueSwal from 'vue-swal'

window._ = require("lodash")
window.$ = window.jQuery = require("jquery")
window.$.Popper = window.Popper = require("popper.js").default
require("bootstrap")
require("js-cookie")
require('dotenv').config()

Vue.config.productionTip = false

Vue.use(BootstrapVue)

Vue.use(VueSwal)

new Vue({
    store,
    router,
    render: h => h(App)
}).$mount('#app')
