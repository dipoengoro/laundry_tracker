import { createRouter, createWebHistory } from "vue-router";
import Register from "../views/Register.vue";
import Login from "../views/Login.vue";
import Catalog from "../views/Catalog.vue";

const routes = [
    {
        path: '/register',
        name: 'Register',
        component: Register
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/',
        name: 'Catalog',
        component: Catalog,
        meta: { requiredAuth: true }
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach((to, from, next) => {
    const loggedIn = localStorage.getItem("authToken");
    if (to.meta.requiredAuth && !loggedIn) {
        // Jika rute butuh login & tidak ada token, paksa ke halaman login
        next("/login");
    } else {
        // Jika tidak, latjutkan seperti biasa
        next();
    }
});

export default router;