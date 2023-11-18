<template>
<div class="min-vh-100">
    <h1 class="text-center mt-3 mb-2 pb-2 border-bottom border-2">XSS demo with example of comments</h1>
    <h2 class="text-center">Unsafe version of comments</h2>
    <div style="padding-left: 5rem;">
        Select comment to view:
        <select class="form-select form-select-md w-75" style="display: inline-block">
            <option v-for="(comment, index) in comments" :value="index" @click="renderItem(index)">{{ comment.title }}</option>
        </select>
    </div>
    <div v-if="comment !== null" class="mt-4">
        <Comment :title="comment.title" :comment="comment.comment" :datetime="new Date(comment.date_time)"/>
    </div>
    <h2 class="mt-5 mb-2 text-center">Safe version of comments</h2>
    <div style="padding-left: 5rem;">
        Select comment to view:
        <select class="form-select form-select-md w-75" style="display: inline-block">
            <option v-for="(comment, index) in comments" :value="index" @click="safeRender(index)">{{ comment.title }}</option>
        </select>
    </div>
    <div v-if="safecomment !== null" class="mt-4">
        <SafeComment :title="safecomment.title" :comment="safecomment.comment" :datetime="new Date(safecomment.date_time)"/>
    </div>
</div>
</template>
<!--
    <div class="mb-2">
            {{ comment.title }} - 
        </div>
-->

<script>
import Comment from "../components/Comment.vue";
import SafeComment from '../components/SafeComment.vue';
import api from "../getAxios";
export default {
        name: "Dashboard",
        components: { Comment, SafeComment },
        data() {
            return {
                comments: [],
                comment: null,
                safecomment: null,
            }
        },
        methods: {
        renderItem(index){
            this.comment = this.comments[index]
        },
        safeRender(index){
            this.safecomment = this.comments[index]
        }
      },
      mounted() {
        api.get('main/comments/')
        .then(response => {
            return response.data
        })
        .then(data =>{
            this.comments = data.comments
            this.comment = data.comments[0]
            this.safecomment = data.comments[0]
        })
        .catch(error => {
            console.error(error)
        })
      }
    }
</script>