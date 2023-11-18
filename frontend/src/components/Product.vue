<template>
        <div class="card shadow position-relative start-50 translate-middle-x mb-4 p-2 w-75">
            <div style="display: inline-block"><img :src="this.thumbnail" class="rounded" style="max-width: 15rem; max-height: 15rem;"/> {{ this.name }}</div>
            <label><strong>{{ this.price }}&nbsp;zł</strong></label>
        </div>
</template>

<script>
export default {
    name: 'Product',
    props:{
        name: String,
        price: Number,
        thumbnail: String
    }
}
</script>