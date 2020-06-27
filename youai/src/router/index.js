import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '../views/Index.vue'
import I from '../views/Info.vue'
import Auth from '../views/Auth.vue'
import Admin from '../views/Admin.vue'
import User from '../views/Admin/User.vue'
import Info from '../views/Admin/Info.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Index',
        component: Index,
        meta: { keepAlive: true },
    },
    {
        path: '/info',
        name: 'I',
        component: I,
    },
    {
        path: '/auth',
        name: 'Auth',
        component: Auth,
    },
    {
        path: '/admin',
        name: 'Admin',
        component: Admin,
        redirect: '/admin/user',
        children: [
            {
                path: 'user',
                name: 'User',
                component: User,
                meta: { keepAlive: true },
            },
            {
                path: 'info',
                name: 'Info',
                component: Info,
                meta: { keepAlive: true },
            },
        ],
    },
]

const router = new VueRouter({
    routes,
})

export default router
