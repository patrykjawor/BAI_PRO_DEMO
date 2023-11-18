<template>
    <div class="position-relative start-50 translate-middle-x card w-75 shadow p-2">
        <p>Title: <strong>{{ this.title }}</strong></p>
        <p>Date: <strong>{{ this.datetime.toLocaleDateString() }}&nbsp;{{ this.datetime.toLocaleTimeString() }}</strong></p>
        <p>Commment content: <label class="mt-1">{{ this.comment }}</label></p>
    </div>
</template>
<script>
export default {
    props: {
        title: String,
        comment: String,
        datetime: Date
    },
    name: 'SafeComment',

}
</script>