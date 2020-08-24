<template>
  <v-card width="400px" class="mx-auto mt-5">
    <v-form> 
      <v-card-title>
        <h1 class="display-1">Login</h1>
      </v-card-title>
      <v-text-field v-model="form.username" prepend-icon="mdi-account-circle" label="username"/>
      <v-text-field type="password" v-model="form.password" prepend-icon="mdi-lock" append-icon="mdi-eye-off" label="password"/>
      <v-card-actions>
        <v-btn @click="loginUser">Login</v-btn>
      </v-card-actions> 
    </v-form>
  </v-card>
</template>

<script>
export default {
  
  //  middleware({ store, redirect }) {
  //  if(store.$auth.loggedIn) {
  //    redirect('/');
  //  }
  //},
  data(){
    return{
      form:{
        username: '',
        password: ''
      }
    }
  },
  methods:{
    async loginUser(){
      try{
        await this.$auth.loginWith('local',{
          data: this.form
      });
      } catch(error) {
        console.log(error);
        alert('エラーが発生しました')
      }
    }
  }
}
</script>
