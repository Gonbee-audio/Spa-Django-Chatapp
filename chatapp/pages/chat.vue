<template>
<v-app :style="{background: $vuetify.theme.themes[theme].background}">

    <v-content>
    <v-card app color="white" style="margin-bottom: 10px;">
        <h1>
            
            name:{{ $auth.user.username }}<br>
            nickname:{{ $auth.user.nickname }}<br>
            <img :src="icon = 'http://0.0.0.0:8000' + $auth.user.icon" width="50" height="50">
            
        </h1>
    <br>
    </v-card>

    <div v-for="(u, index) in Message2" :key="'info2-' + index" >
        <v-card :id="u.id" app color="blue" style="margin-bottom: 10px;">
        <div align="center"><a class="black--text">{{u.text}}</a></div><br>
        <a>
            <a style="margin-left: 2%;" class="black--text">name:{{u.nickname}}</a>
            <v-btn class="ma-2" text icon color="blue lighten-2">
                <v-icon>mdi-thumb-up</v-icon>
            </v-btn>
            <v-btn class="ma-2" text icon color="red lighten-2">
                <v-icon>mdi-thumb-down</v-icon>
            </v-btn>
            <button
                class="btn btn-danger btn-sm ml-1"
                v-on:click="deleteSubscription(u)">
                Delete
            </button>
        </a>
        </v-card>
    </div>

    <div id="chat-log">
        
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
          <v-btn @click.enter="submit" >send</v-btn>
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
    async mounted(){
        //複数データがないとapiがhtmlを拾ってきて動かないのかもしれない。。。
        const url = "http://0.0.0.0:8000/api/chatmessage/"
        const responce =  await this.$axios.$get(url)
        console.log(responce)
        this.Message2 = responce
        
        this.websocket.onmessage = function(e){ 
                const data = JSON.parse(e.data)
                const mes = document.createElement('div');
                mes.className = "v-sheet theme--light blue v-toolbar v-app-bar v-app-bar--is-scrolled";
                mes.style.marginBottom = "10px"

                const messageHTML = '<div>' + data.message.text + '</div>'
                const text = document.createElement('a');
                text.className = "black--text"        
                text.innerHTML = messageHTML;
                text.style.textAlign = 'center'

                const name = document.createElement('a');
                const usernameHTML = 'name:' + data.message.username
                name.className = "black--text"
                name.innerHTML = usernameHTML
                name.style.marginLeft = "2%"
                //name.style.textAlign = 'center'


                const goodiconimg = document.createElement('i');
                goodiconimg.className = "v-icon notranslate mdi mdi-thumb-up theme--light"
                goodiconimg.style.color = "#64B5F6"
                goodiconimg.style.marginLeft = "20px"

                const badiconimg = document.createElement('i');
                badiconimg.className = "v-icon notranslate mdi mdi-thumb-down theme--light"
                badiconimg.style.color = "#E57373"
                badiconimg.style.marginLeft = "20px"

                const icon = document.createElement('button');
                icon.className = "ma-2 v-btn v-btn--flat v-btn--icon v-btn--round v-btn--text theme--light v-size--default blue--text text--lighten-2"

                let element = document.getElementById('chat-log');
                element.appendChild(mes).appendChild(text).appendChild(name).appendChild(icon).appendChild(goodiconimg).appendChild(badiconimg)
        }
        
  },

  created: function(){
      console.log("Starting WebSocket Connect!!")
      const webapi = new WebSocket(
            "ws://0.0.0.0:8000/api/ws/"
      );
      webapi.onopen = function(event) {
      //console.log(event)
      //console.log(webapi)
      console.log("Successfully connected to the echo websocket server...")
    }
    this.websocket = webapi
  },
  methods:{
    submit: function (e) {
        console.log(e)
        const message = {
            "text": this.text,
            "username": this.username
        }
        console.log(message)
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
    deleteSubscription(subscr) {
        console.log(subscr)
    if (confirm('Delete ' + subscr.username)) {
        console.log(subscr.id)
        axios.delete('http://0.0.0.0:8000/api/chatmessage/' + subscr.id)
            .then( response => {
                let parent = document.getElementById(subscr.id)
                parent.remove()
            });
    }
},
  }
}
</script>