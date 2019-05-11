import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import VueSwal from 'vue-swal'

/* BEGIN Metronic theme assets */
var KTAppOptions = {
    "colors": {
        "state": {
            "brand": "#366cf3",
            "light": "#ffffff",
            "dark": "#282a3c",
            "primary": "#5867dd",
            "success": "#34bfa3",
            "info": "#36a3f7",
            "warning": "#ffb822",
            "danger": "#fd3995"
        },
        "base": {
            "label": ["#c5cbe3", "#a1a8c3", "#3d4465", "#3e4466"],
            "shape": ["#f0f3ff", "#d9dffa", "#afb4d4", "#646c9a"]
        }
    }
};
window.$ = window.jQuery = require("../public/assets/vendors/general/jquery/dist/jquery.js")
window.$.Popper = window.Popper = require("../public/assets/vendors/general/popper.js/dist/umd/popper.js").default
require("../public/assets/vendors/general/bootstrap/dist/js/bootstrap.min.js")
require("../public/assets/vendors/general/js-cookie/src/js.cookie.js")
window.moment = require("../public/assets/vendors/general/moment/min/moment.min.js")
require("../public/assets/vendors/general/tooltip.js/dist/umd/tooltip.min.js")
require("../public/assets/vendors/general/perfect-scrollbar/dist/perfect-scrollbar.js")
require("../public/assets/vendors/general/sticky-js/dist/sticky.min.js")
require("../public/assets/vendors/general/wnumb/wNumb.js")

require("../public/assets/vendors/general/jquery-form/dist/jquery.form.min.js")
require("../public/assets/vendors/general/block-ui/jquery.blockUI.js")
require("../public/assets/vendors/general/bootstrap-datepicker/dist/js/bootstrap-datepicker.min.js")
require("../public/assets/vendors/custom/js/vendors/bootstrap-datepicker.init.js")
require("../public/assets/vendors/general/bootstrap-datetime-picker/js/bootstrap-datetimepicker.min.js")
require("../public/assets/vendors/general/bootstrap-timepicker/js/bootstrap-timepicker.min.js")
require("../public/assets/vendors/custom/js/vendors/bootstrap-timepicker.init.js")
require("../public/assets/vendors/general/bootstrap-touchspin/dist/jquery.bootstrap-touchspin.js")
require("../public/assets/vendors/general/bootstrap-maxlength/src/bootstrap-maxlength.js")
require("../public/assets/vendors/custom/vendors/bootstrap-multiselectsplitter/bootstrap-multiselectsplitter.min.js")
require("../public/assets/vendors/general/bootstrap-select/dist/js/bootstrap-select.js")
require("../public/assets/vendors/general/bootstrap-switch/dist/js/bootstrap-switch.js")
require("../public/assets/vendors/custom/js/vendors/bootstrap-switch.init.js")
require("../public/assets/vendors/general/select2/dist/js/select2.full.js")
require("../public/assets/vendors/general/ion-rangeslider/js/ion.rangeSlider.js")
require("../public/assets/vendors/general/typeahead.js/dist/typeahead.bundle.js")
require("../public/assets/vendors/general/handlebars/dist/handlebars.js")
require("../public/assets/vendors/general/inputmask/dist/jquery.inputmask.bundle.js")
require("../public/assets/vendors/general/inputmask/dist/inputmask/inputmask.date.extensions.js")
require("../public/assets/vendors/general/inputmask/dist/inputmask/inputmask.numeric.extensions.js")
require("../public/assets/vendors/general/nouislider/distribute/nouislider.js")
require("../public/assets/vendors/general/owl.carousel/dist/owl.carousel.js")
require("../public/assets/vendors/general/autosize/dist/autosize.js")
require("../public/assets/vendors/general/clipboard/dist/clipboard.min.js")
require("../public/assets/vendors/general/dropzone/dist/dropzone.js")
require("../public/assets/vendors/general/markdown/lib/markdown.js")
require("../public/assets/vendors/general/bootstrap-markdown/js/bootstrap-markdown.js")
require("../public/assets/vendors/custom/js/vendors/bootstrap-markdown.init.js")
require("../public/assets/vendors/general/bootstrap-notify/bootstrap-notify.min.js")
require("../public/assets/vendors/custom/js/vendors/bootstrap-notify.init.js")
require("../public/assets/vendors/general/jquery-validation/dist/jquery.validate.js")
require("../public/assets/vendors/general/jquery-validation/dist/additional-methods.js")
require("../public/assets/vendors/custom/js/vendors/jquery-validation.init.js")
require("../public/assets/vendors/general/toastr/build/toastr.min.js")
require("../public/assets/vendors/general/raphael/raphael.js")
require("../public/assets/vendors/general/morris.js/morris.js")
require("../public/assets/vendors/general/chart.js/dist/Chart.bundle.js")
require("../public/assets/vendors/custom/vendors/bootstrap-session-timeout/dist/bootstrap-session-timeout.min.js")
require("../public/assets/vendors/custom/vendors/jquery-idletimer/idle-timer.min.js")
require("../public/assets/vendors/general/waypoints/lib/jquery.waypoints.js")
require("../public/assets/vendors/general/counterup/jquery.counterup.js")
require("../public/assets/vendors/general/es6-promise-polyfill/promise.min.js")
require("../public/assets/vendors/general/jquery.repeater/src/lib.js")
require("../public/assets/vendors/general/jquery.repeater/src/jquery.input.js")
require("../public/assets/vendors/general/jquery.repeater/src/repeater.js")
require("../public/assets/vendors/general/dompurify/dist/purify.js")

require("../public/assets/js/demo4/scripts.bundle.js")

require("../public/assets/js/demo4/pages/dashboard.js")
/* END Metronic theme assets */

//import 'bootstrap/dist/css/bootstrap.css'
//import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

Vue.use(BootstrapVue)

Vue.use(VueSwal)

new Vue({
    store,
    router,
    render: h => h(App)
}).$mount('#app')
