import colors from 'vuetify/es5/util/colors'

export default {
  /*
  ** Nuxt rendering mode
  ** See https://nuxtjs.org/api/configuration-mode
  */
  mode: 'spa',
    server: {
    port: 3000,
    host: '0.0.0.0',  
  },
  /*
  ** Nuxt target
  ** See https://nuxtjs.org/api/configuration-target
  */
  target: 'server',
  /*
  ** Headers of the page
  ** See https://nuxtjs.org/api/configuration-head
  */
  head: {
    titleTemplate: '%s - ' + process.env.npm_package_name,
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  /*
  ** Global CSS
  */
  css: [
  ],
  /*
  ** Plugins to load before mounting the App
  ** https://nuxtjs.org/guide/plugins
  */
  plugins: [
  ],
  /*
  ** Auto import components
  ** See https://nuxtjs.org/api/configuration-components
  */
  components: true,
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
    '@nuxtjs/vuetify',
  ],
  /*
  ** Nuxt.js modules
  */
  /*
  ** vuetify module configuration
  ** https://github.com/nuxt-community/vuetify-module
  */
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: true,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    }
  },
  /*
  ** Build configuration
  ** See https://nuxtjs.org/api/configuration-build/
  */
  build: {
    }, //追記の際はカンマを忘れずに
    watchers: {
    webpack: {
      poll: 3000
    },
  },
    modules: [
      '@nuxtjs/axios',
      '@nuxtjs/auth',
      '@nuxtjs/proxy'
    ],
    axios: {

      baseURL: "http://0.0.0.0:8000"
      //proxy: true
    },
    //proxy: {
    //  'api/':'http://0.0.0.0:8000'
    //  }
    auth: {
      redirect: {
        login: { url: '/chat', method: 'post', propertyName: 'token' },
        logout: { url: '/', method: 'post' },
        callback: false,   // Oauth認証等で必要となる コールバックルート
        home: '/chat',         // ログイン後のリダイレクトURL
      },
      strategies: {
        local: {
          endpoints: {
            login: { url: '/api/login/', method: 'post', propertyName: 'token' },
            user: { url: '/api/users/', method: 'get', propertyName: false},
            logout: false
          },
          // tokenRequired: true,
          // tokenType: 'bearer'
        }
      }
    }
}
