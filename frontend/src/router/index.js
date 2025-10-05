import {createRouter, createWebHistory} from "vue-router";
import MainLayout from "../layouts/MainLayout.vue";

import Register from "../views/Register.vue";
import Login from "../views/Login.vue";
import Catalog from "../views/Catalog.vue";

const routes = [
    {
        path: '/',
        component: MainLayout,
        meta: {requiredAuth: true},
        children: [
            {
                path: '',
                name: 'Catalog',
                component: Catalog,
            },
        ]
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
    },
    {
        path: '/register',
        name: 'Register',
        component: Register
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach((to, from, next) => {
    const loggedIn = localStorage.getItem("authToken");

    if (to.matched.some(record => record.meta.requiredAuth) && !loggedIn) {
        next('/login');
    } else {
        next();
    }
});

export default router;