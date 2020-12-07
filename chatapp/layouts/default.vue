<template>
  <v-app :style="{background: $vuetify.theme.themes[theme].background}">
    <v-navigation-drawer
      app dark color="blue darken-2"
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
    >
      <v-switch
        v-model="landscape"
        :prepend-icon="themeIcon"
        color="white--text"
      ></v-switch>

      <v-list app dark color="blue darken-2 white--text">
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      app dark color="blue darken-2"
      :clipped-left="clipped"
      fixed
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-btn
        icon
        @click.stop="miniVariant = !miniVariant"
      >
        <v-icon>mdi-{{ `chevron-${miniVariant ? 'right' : 'left'}` }}</v-icon>
      </v-btn>
      <v-btn
        icon
        @click.stop="clipped = !clipped"
      >
        <v-icon>mdi-application</v-icon>
      </v-btn>
      <v-btn
        icon
        @click.stop="fixed = !fixed"
      >
        <v-icon>mdi-minus</v-icon>
      </v-btn>
      <v-toolbar-title v-text="title" />
      <v-spacer />
      
      <v-btn
        v-if ="this.$auth.loggedIn == true"
        icon
        @click.stop="rightDrawer = !rightDrawer"
      >
        <v-icon>mdi-menu</v-icon>
      </v-btn>

    </v-app-bar>
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
  
<!-- After  Login menu-->
    <v-navigation-drawer
      v-model="rightDrawer"
      :right="right"
      temporary
      fixed
    >
      <v-list>

        <v-list-item @click.native="right = !right">
          <v-list-item-action>
            <v-icon light>
              mdi-repeat
            </v-icon>
          </v-list-item-action>
          <v-list-item-title>Switch drawer (click me)</v-list-item-title>
        </v-list-item>

      <v-list-item line>
        <v-list-item-content>
          <a>YourLoginState:{{this.$auth.loggedIn}}</a>
        </v-list-item-content>
      </v-list-item>

      <v-list-item  two-line>
        <v-list-item-content>
          <v-list-item-title>Two-line item</v-list-item-title>
          <v-btn @click="chatPage">Chat Page</v-btn>
        </v-list-item-content>
      </v-list-item>

      <!--<a v-else>test</a>-->
      <v-list-item three-line>
        <v-list-item-content>
          <v-btn @click="logoutSheet = !logoutSheet">Logout</v-btn>
        </v-list-item-content>
      </v-list-item>

<!-- Open v-btn sheet-->
    <v-bottom-sheet v-model="logoutSheet">
      <v-sheet class="text-center" height="200px" color="green lighten-5">
        <div>want you to logout?</div>
        <v-btn
          class="mt-6"
          text
          color="blue"
          @click="logoutSheet = !logoutSheet"
        >close</v-btn>
        <v-btn
          class="mt-6"
          text
          color="red" 
          @click="logout"
        >logout</v-btn>
      </v-sheet>
    </v-bottom-sheet>



      </v-list>
    </v-navigation-drawer>

    <v-footer
      :absolute="!fixed"
      app
    >
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data () {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      logoutSheet: false,
      landscape: false,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Login',
          to: '/'
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Signup',
          to: '/signup'
        },
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Django-Vue-Spa-ChatApp'
    }
  },
  computed: {
    themeIcon(){
      return this.landscape ? 'mdi-weather-night' : 'mdi-weather-sunny'
    },
    theme() {
      return this.$vuetify.theme.dark ? "dark" : "light";
    }
  },
  watch: {
    landscape() {
      console.log(this.landscape)
      this.$vuetify.theme.dark = this.landscape
    }
  },
  methods: {
    chatPage(){
      if(this.$auth.loggedIn == true){
        this.$router.push('/chat')
      } else {
        alert('login')
      }
    },
    logout() {
      if(this.$auth.loggedIn == false){
      } else {
        this.$auth.logout();
        this.$router.push('/')
      }
    },
  }
}

</script>
