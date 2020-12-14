<template>
<v-app :style="{background: $vuetify.theme.themes[theme].background}">

    <v-content>
    <v-card app color="blue lighten-5" style="margin-bottom: 10px;">
        <h1>
            
            name:{{ $auth.user.username }}<br>
            nickname:{{ $auth.user.nickname }}<br>
            <img :src="icon = 
                 'http://' + this.hostname + ':8000' + 
                 $auth.user.icon" width="50" height="50">
            
        </h1>
    <br>
    </v-card>

    <div v-for="(u, index) in Message2" :key="'info2-' + index" >
        <v-card :id="u.id" app color="teal accent-1" style="margin-bottom: 10px;">
        <div align="center"><a class="black--text">{{u.text}}</a></div><br>
        <a>
            <a style="margin-left: 2%;" class="black--text">name:{{u.nickname}}</a>
            <v-btn class="ma-2" text icon color="blue lighten-2">
                <v-icon>mdi-thumb-up</v-icon>
            </v-btn>
            <v-btn class="ma-2" text icon color="red lighten-2">
                <v-icon>mdi-thumb-down</v-icon>
            </v-btn>
            <v-btn color="pink lighten-3"
                   @click="deleteSubscription(u)"
                   >
                Delete
            </v-btn>
        </a>
        </v-card>
    </div>

    <templates id="chat-log">
        
    </templates>

    </v-content>
    <v-form>
        <input type="hidden" :value="nickname = $auth.user.nickname">
        <input type="hidden" :value="username = $auth.user.username">
        <input type="hidden" v-model="image" value="test">
        <v-text-field prepend-icon="mdi-account-circle" 
            label="text"
            v-model="text">
            
<!-- 　写真をデプロイするためのinput
                    <v-file-input label="File input"
                      slot="append"
                      outlined
                      dense
                      hide-input
                      @change="submit"
                      accept="image/*"
                      >
                      </v-file-input>
-->

        </v-text-field>

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
            hostname: window.location.hostname,
            Message2: null,
            username: [],
            nickname: [],
            image: "",
            uploadImageUrl: [],
            fileName: [],
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
        //console.log(window.location)
        const url = "http://" +  
                    this.hostname + 
                    ":8000" + 
                    "/api/chatmessage/"
        const responce =  await this.$axios.$get(url)
        this.Message2 = responce
        
        this.websocket.onmessage = function(e){ 
                const data = JSON.parse(e.data)
                console.log(data)

                const mescard = document.createElement('div');
                mescard.className = "v-card v-sheet theme--light teal accent-1";
                mescard.style.marginBottom = "10px"
                mescard.setAttribute("id", data.id);

                const mescardText = document.createElement('div')
                mescardText.style.textAlign = "center"

                const messageHTML = '<div>' + data.message.text + '</div>' + "<br>"
                const text = document.createElement('a');
                text.className = "black--text"        
                text.innerHTML = messageHTML;

                const other_base = document.createElement('a')
                other_base.setAttribute("id", "other" + data.id);
                other_base.style.marginLeft = "2%"

                const name = document.createElement('a');
                const usernameHTML = 'name:' + data.message.username
                name.className = "black--text"
                name.innerHTML = usernameHTML

                const good_button = document.createElement('button')
                good_button.className = "ma-2 v-btn v-btn--flat v-btn--icon v-btn--round v-btn--text theme--light v-size--default red--text text--lighten-2"

                const bad_button = document.createElement('button')
                bad_button.className = "ma-2 v-btn v-btn--flat v-btn--icon v-btn--round v-btn--text theme--light v-size--default red--text text--lighten-2"

                const delete_button = document.createElement('button')
                delete_button.className = "v-btn v-btn--contained black--text theme--light v-size--default pink lighten-3"
                delete_button.style.color = "#E57373"
                //delete_button.setAttribute("onclick", "deleteSubscription(u)");
                delete_button.onclick = function() {
                    if (confirm('Delete')) {
                            axios.delete('http://0.0.0.0:8000/api/chatmessage/' + data.id)
                               .then( response => {
                               let parent = document.getElementById(data.id)
                            parent.remove()
                        });
                    }}
                
                //@click="deleteSubscription(u)

                const v_btn__content_1 = document.createElement('span')
                v_btn__content_1.className = "v-btn__content"

                const v_btn__content_2 = document.createElement('span')
                v_btn__content_2.className = "v-btn__content"

                const deleteHTML = "delete"
                const v_btn__content_3 = document.createElement('span')
                v_btn__content_3.className = "v-btn__content"
                v_btn__content_3.innerHTML = deleteHTML

                const goodiconimg = document.createElement('i');
                goodiconimg.className = "v-icon notranslate mdi mdi-thumb-up theme--light"
                goodiconimg.style.color = "#64B5F6"

                const badiconimg = document.createElement('i');
                badiconimg.className = "v-icon notranslate mdi mdi-thumb-down theme--light"
                badiconimg.style.color = "#E57373"

                let element = document.getElementById('chat-log');
                element.appendChild(mescard).appendChild(mescardText).appendChild(text)
                element.appendChild(mescard).appendChild(other_base).appendChild(name)

                let other_element = document.getElementById('other' + data.id);
                other_element.appendChild(name)
                other_element.appendChild(good_button).appendChild(v_btn__content_1).appendChild(goodiconimg)
                other_element.appendChild(bad_button).appendChild(v_btn__content_2).appendChild(badiconimg)
                other_element.appendChild(delete_button).appendChild(v_btn__content_3)

}},
  created: function(){
      console.log("Starting WebSocket Connect!!")
      const webapi = new WebSocket(
            "ws://0.0.0.0:8000/api/ws/"
      );
      webapi.onopen = function(event) {
      console.log("Successfully connected to the echo websocket server...")
    }
    this.websocket = webapi
  },
  methods:{
    submit: function (file) {
        const message = {
            "text": this.text,
            "username": this.username,
        }
        console.log(message)
        const webapi = new WebSocket(
            "ws://0.0.0.0:8000/api/ws/"
        );
        console.log(message.text)
        if(message.text != ""){
            webapi.onopen = () => 
            webapi.send(
                JSON.stringify({
                    "message": message
            }),);
            this.text = ""
        }else{
            alert("error !!")
        }   
    },
    deleteSubscription: function(subscr) {
    if (confirm('Delete')) {
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