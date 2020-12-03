<template>
<v-app :style="{background: $vuetify.theme.themes[theme].background}">
    <v-app-bar>
        <h1>
            
            name:{{ $auth.user.username }}<br>
            nickname:{{ $auth.user.nickname }}<br>
            <img :src="icon = 'http://0.0.0.0:8000' + $auth.user.icon" width="50" height="50">
            
        </h1>
        <br>
        
    </v-app-bar>
    <v-content>

    <div v-for="(u, index) in Message2" :key="'info2-' + index" align="center">
        <v-card app color="blue" style="margin: 10px;">
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

    <textarea id="chat-log">
        
    </textarea>

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
          <v-btn @click="submit" >send</v-btn>
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
            Message2: null,
            username: [],
            nickname: [],
            image: [],
            icon: [],
            text: "",
            websocket: [],
        }
    },
    computed: {
    theme() {
      return this.$vuetify.theme.dark ? "dark" : "light";
    }
  },
    mounted(){
        //複数データがないとapiがhtmlを拾ってきて動かないのかもしれない。。。
        const url = "http://0.0.0.0:8000/api/chatmessage/"
        const responce = this.$axios.$get(url)
        this.Message2 = responce
        this.websocket.onmessage = function(e){ 
                const data = JSON.parse(e.data)
                document.querySelector('#chat-log').value += (data.message + '\n');
        }
        
  },

  created: function(){
      console.log("Starting WebSocket Connect!!")
      const webapi = new WebSocket(
            "ws://0.0.0.0:8000/api/ws/"
      );
      
      console.log(webapi)

      webapi.onopen = function(event) {
      //console.log(event)
      console.log(webapi)
      console.log("Successfully connected to the echo websocket server...")
    }
    this.websocket = webapi
  },
  methods:{
    submit: function (e) {
        const message = this.text
        const webapi = new WebSocket(
            "ws://0.0.0.0:8000/api/ws/"
        );
        webapi.onopen = () => 
        webapi.send(
            JSON.stringify({
                "message": message
        }),
        );


        this.text = ""
    },
    






        /*
        const url2 = new WebSocket("wss://" + "0.0.0.0:8000" + "/ws/")
        url2.onmessage = function(evt) { responseData(evt); };
        console.log(document)
        const params = new URLSearchParams(url2);
        params.append('text', this.text);
        params.append('nickname', this.nickname);
        params.append('username', 'tesst');
        params.append('icon', 'test.img');
        
    //params.append('password', this.password);
        await this.$axios.$post(url2, params)
        .then(response => { 
             console.log(response.data)
            alert('送信に成功しました！')
        })
        .catch(error => {
             console.log('response', error.response.data);
    
});
*/
  }
}
</script>