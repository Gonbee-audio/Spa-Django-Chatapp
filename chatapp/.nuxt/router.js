import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _53774028 = () => interopDefault(import('../pages/chat.vue' /* webpackChunkName: "pages/chat" */))
const _92761abe = () => interopDefault(import('../pages/detail.vue' /* webpackChunkName: "pages/detail" */))
const _142fad63 = () => interopDefault(import('../pages/private.vue' /* webpackChunkName: "pages/private" */))
const _53cee030 = () => interopDefault(import('../pages/signup.vue' /* webpackChunkName: "pages/signup" */))
const _e542f99c = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

// TODO: remove in Nuxt 3
const emptyFn = () => {}
const originalPush = Router.prototype.push
Router.prototype.push = function push (location, onComplete = emptyFn, onAbort) {
  return originalPush.call(this, location, onComplete, onAbort)
}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: decodeURI('/'),
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/chat",
    component: _53774028,
    name: "chat"
  }, {
    path: "/detail",
    component: _92761abe,
    name: "detail"
  }, {
    path: "/private",
    component: _142fad63,
    name: "private"
  }, {
    path: "/signup",
    component: _53cee030,
    name: "signup"
  }, {
    path: "/",
    component: _e542f99c,
    name: "index"
  }],

  fallback: false
}

export function createRouter () {
  return new Router(routerOptions)
}
