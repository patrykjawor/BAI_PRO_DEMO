import './assets/main.css'
import './assets/base.css'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle';
import 'bootstrap-icons/font/bootstrap-icons.css'

import { createRouter, createWebHashHistory } from 'vue-router';
import { createApp } from 'vue'
import VueCookies from 'vue-cookies';
import App from './App.vue'
import routes from './Router';


// createApp(App).mount('#app')
const router = createRouter({
    history: createWebHashHistory(),
    routes: routes,
})



const app = createApp(App);

app.use(router);
app.use(VueCookies)
app.mount('#app');
