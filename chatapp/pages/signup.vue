<template>
<v-app :style="{background: $vuetify.theme.themes[theme].background}">
  <v-card>
    <v-card-title>
      <h1 class="display-1">SignUp</h1>
    </v-card-title>
    <v-card-text v-if="success === false">
      <v-form >
        <v-text-field prepend-icon="mdi-account-circle" 
                      label="username"
                      v-model="username"
                      v-bind:value="username" />
        <v-text-field type="password"
                      prepend-icon="mdi-lock" 
                      append-icon="mdi-eye-off" 
                      label="password"
                      v-model="password" />
        <v-card-actions>
          <v-btn @click="submit">create</v-btn>
        </v-card-actions> 
      </v-form>

    </v-card-text>
      <v-alert v-else type="success">
          you account a success alert.<br>
          <h2>yourname:{{ username }}</h2>
      </v-alert>
  </v-card>
  
</v-app>
</template>

<script>
export default {
  name: 'Login',
  data(){
    return{
      username: [],
      password: null,
      success: false,
    }
  },
  computed: {
    theme() {
      return this.$vuetify.theme.dark ? "dark" : "light";
    }
  },
  methods:{

/*
async submit(){
const data = { 
  'username': this.username,
  'nickname': this.username,
  'password': this.password 
};
const url = "http://0.0.0.0:8000/api-user/register/"
const options = {
  method: 'POST',
  headers: { 'content-type': 'application/x-www-form-urlencoded' },
  data: qs.stringify(data),
  url,
};
console.log(options)
await this.$axios(options);
}
*/


  async submit(){
      const params = new URLSearchParams();
      params.append('username', this.username);
      params.append('nickname', this.username);
      params.append('password', this.password);
      
      await this.$axios.$post('http:' + window.location.hostname +
      ':8000' +
       '/api-user/register/', params)
.then(response => { 
  console.log(response.data)
  console.log(this.success)
  this.success = true
})
.catch(error => {
    console.log('response', error.response.data);
});
  }


  }
}
</script>