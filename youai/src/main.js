import Vue from "vue";
import App from "./App.vue";
import router from "./router";

import axios from "axios";
import VueAxios from "vue-axios";
Vue.use(VueAxios, axios);

axios.interceptors.request.use(
  (request) => {
    request.headers["token"] = localStorage.getItem("token");
    return request;
  },
  (error) => {
    return Promise.reject(error);
  }
);

import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
Vue.use(ElementUI);

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
