<template>
<div>
    {{User}}
    <div v-for="u in User" :key=u.nickname align="center">
        <h2>
        {{u.nickname}}<br>
        {{u.text}}
        </h2>
    </div>
</div>
</template>


<script>
import Vue from 'vue'
import axios from 'axios'

export default{
    data(){
        return{
            User: []
        }
    },
    async mounted(){
        //複数データがないとapiがhtmlを拾ってきて動かないのかもしれない。。。
        const url = "http://0.0.0.0:8000/api/chatmessage/"
        const responce = await this.$axios.$get(url)
        this.User = responce
        console.log(this.request)
  }
}
</script>