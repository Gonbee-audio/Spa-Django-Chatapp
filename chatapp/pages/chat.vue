<template>
<v-app>
    <v-app-bar>
        <h1>
            
            name:{{ $auth.user.username }}<br>
            nickname:{{ $auth.user.nickname }}<br>
            <img :src="icon = 'http://0.0.0.0:8000' + $auth.user.icon" width="50" height="50">
            
        </h1>
        <br>
        
    </v-app-bar>
    <v-content>
    <div v-for="u in User" :key=u.nickname align="center">
        <v-card app dark color="blue" style="margin: 10px;">
        {{u.nickname}}<br>
        {{u.text}}
        <a>
            <v-btn class="ma-2" text icon color="blue lighten-2">
                <v-icon>mdi-thumb-up</v-icon>
            </v-btn>
            <v-btn class="ma-2" text icon color="red lighten-2">
                <v-icon>mdi-thumb-down</v-icon>
            </v-btn>
        </a>
        </v-card>
    </div>
    </v-content>
    <v-form>
        <input type="hidden" :value="nickname = $auth.user.nickname">
        <input type="hidden" :value="username = $auth.user.username">

<!--まだchatの写真をimageにしてvue側にを渡すapiが完成していないからimageタグは仮のものを使います-->
        <input type="hidden" v-model="image" value="test">
        <v-text-field prepend-icon="mdi-account-circle" 
            label="text"
            v-model="text" />
        <v-card-actions>
          <v-btn @click="submit">create</v-btn>
        </v-card-actions> 
    </v-form>
</v-app>
</template>


<script>
import Vue from 'vue'
import axios from 'axios'

export default{
    data(){
        return{
            User: [],
            username: [],
            nickname: [],
            image: [],
            icon: [],
        }
    },
    async mounted(){
        //複数データがないとapiがhtmlを拾ってきて動かないのかもしれない。。。
        const url = "http://0.0.0.0:8000/api/chatmessage/"
        const responce = await this.$axios.$get(url)
        this.User = responce
        console.log(this.request)
  },
  methods:{
    async submit(){
        const params = new URLSearchParams();
        params.append('text', this.text);
        params.append('nickname', this.nickname);
        params.append('username', 'tesst');
        params.append('icon', 'test.img');
    //params.append('password', this.password);
        await this.$axios.$post('http://0.0.0.0:8000/api/chatmessage/', params)
        .then(response => { 
             console.log(response.data)
            alert('送信に成功しました！')
        })
        .catch(error => {
             console.log('response', error.response.data);
});
  }
  }
}
</script>