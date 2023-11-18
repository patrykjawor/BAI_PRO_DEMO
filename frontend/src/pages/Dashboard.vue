<template>
    <div class="min-vh-100 text-center">
        <h1 class="text-center pt-3 mb-2 pb-2 border-bottom border-2">This is dashboard</h1>
        <router-link to="/login" class="btn btn-primary"><i class="bi bi-box-arrow-in-left"></i> Login page</router-link><br/>
        <router-link to="/register" class="btn btn-primary mt-2"><i class="bi bi-plus-circle"></i> Register page</router-link><br/>
        <button @click="genComments" class="btn btn-primary mt-2">Generate comments</button><br/>
        <button @click="genSample" class="btn btn-primary mt-2">Generate sample database</button>
    </div>
</template>

<script>
    import api from '../getAxios.js';
    export default {
        name: "Dashboard",
        data() {
            return {
                
            }
        },
        mounted() {
        },
        methods: {
        genComments() {
                api.post('main/comments/gen/')
                .then(response => {
                    return response.data
                })
                .then(data => {
                    alert(data.message);
                })
                .catch(error => {
                    console.warn(error);
                    alert('Failed to generate comments!')
                })
        },
        genSample() {
            var form = new FormData()

            form.append('csrfmiddlewaretoken', this.$cookies.get('csrftoken'))
            api.post('main/sqlgen/', form, {
                headers:{
                    'Content-Type': 'multipart/form-data',
                    'X-CSRFToken': this.$cookies.get('csrftoken')
                }
            })
            .then(response => {
                return response.data;
            })
            .then(data => {
                alert(data.message);
            })
            .catch(error => {
                console.warn(error);
                alert('Failed to create sample database');
            })
        }
      }
    }
</script>