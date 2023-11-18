<template>
<div class="vh-100">
    <h1 class="text-center mt-3 pb-2 border-bottom border-2">Page not found</h1>
    <div class="d-flex justify-content-center align-items-center h-100 text-center">
        <h3>Route " <i>{{ this.$route.path }}</i>&nbsp;"&nbsp;&nbsp; does not exist!<br/>
            <button @click="goBack" class="btn btn-primary">Back</button>
        </h3>
        
    </div>
</div>
</template>

<script>
export default {
    name: "NotFound",
    methods: {
        goBack(){
            this.$router.back()
        }
    }
}
</script>