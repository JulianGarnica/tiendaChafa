import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';
import loadingCSS from "@/components/static/loadingCSS.vue";


Vue.config.productionTip = false
Vue.use(VueSweetalert2);

let globalData = new Vue({
  data: { $dataUser: {} }
});
Vue.mixin({
  computed: {
    $dataUser: {
      get: function () { return globalData.$data.$dataUser },
      set: function (newdataUser) { globalData.$data.$dataUser = newdataUser; }
    }
  }
})

new Vue({
  router,
  store,
  vuetify,
  loadingCSS,
  render: h => h(App)
}).$mount('#app')
