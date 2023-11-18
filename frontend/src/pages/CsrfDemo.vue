<template>
<div class="min-vh-100">
    <h1 class="text-center mt-3 pb-2 mb-2 border-bottom border-2">CSRF vulnerability demo</h1>
    <div class="d-flex flex-column justify-content-center text-center">
        <div class="mb-2"><button @click="show = !show" class="btn btn-primary">Click here to {{show ? 'hide': 'view'}} &#128293; photos!</button><br/></div>
        <img v-if="show" style="max-width: 10rem; max-height: 10rem;" class="position-relative start-50 translate-middle-x" :src="base+'/main/subscribe/'" alt="Cat photo">
    </div>
</div>


</template>

<script>
import { baseURL } from '../getAxios.js';
export default {
        name: "Dashboard",
        data() {
            return {
                show: false,
                base: baseURL,
            }
        },
        methods: {
        }
    }
</script>