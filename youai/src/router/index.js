import Vue from "vue";
import VueRouter from "vue-router";
import Index from "../views/Index.vue";
import Auth from "../views/Auth.vue";
import Admin from "../views/Admin.vue";
import User from "../views/Admin/User.vue";
import Info from "../views/Admin/Info.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Index",
    component: Index,
  },
  {
    path: "/auth",
    name: "Auth",
    component: Auth,
  },
  {
    path: "/admin",
    name: "Admin",
    component: Admin,
    redirect: "/admin/user",
    children: [
      {
        path: "user",
        name: "User",
        component: User,
      },
      {
        path: "info",
        name: "Info",
        component: Info,
      },
    ],
  },
];

const router = new VueRouter({
  routes,
});

export default router;
