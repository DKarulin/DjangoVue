import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';
import VueTheMask from 'vue-the-mask';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';


Vue.config.productionTip = false;
Vue.config.debug = true;
Vue.config.devtools = true;
Vue.use(BootstrapVue);
Vue.use(VueTheMask)

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
