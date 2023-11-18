import Register from './pages/Register.vue';
import Login from './pages/Login.vue';
import Dashboard from './pages/Dashboard.vue';
import SqlDemo from './pages/SqlDemo.vue';
import XssDemo from './pages/XssDemo.vue';
import CsrfDemo from './pages/CsrfDemo.vue';
import NotFound from './pages/NotFound.vue';

const routes = [
    {
        path: "/login",
        name: "login",
        component: Login
    },
    {
        path: "/register",
        name: "register",
        component: Register
    },
    {
        path: "/dashboard",
        name: "dashboard",
        component: Dashboard
    },
    {
        path:"/dashboard/sqldemo",
        name: "sqldemo",
        component: SqlDemo
    },
    {
        path:"/dashboard/xssdemo",
        name: "xssdemo",
        component: XssDemo
    },
    {
        path:"/dashboard/csrfdemo",
        name: "csrfdemo",
        component: CsrfDemo
    },
    {
        path: "/:notFound*",
        name: "not-found",
        component: NotFound
    }
]


export default routes;