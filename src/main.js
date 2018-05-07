import Vue from 'vue'
import Router from 'vue-router'
import Cookies from 'vue-cookies'

import Buefy from 'buefy'
import 'buefy/lib/buefy.css'

//Components
import Login from './components/Login.vue'
import App from './App.vue'
import Party from './components/Party.vue'
import Party_Create from './components/Party_Create.vue'
import Party_List from './components/Party_List.vue'

import VueRouter from 'vue-router'

Vue.use(Router)
Vue.use(Buefy)
Vue.use(Cookies)

const routes = [
  { path: "/login", component: Login },
  { path: "/party", component: Party_List },
  { path: "/party/:id", component: Party },
  { path: "/make", component: Party_Create },
]

const router = new VueRouter({
  mode: 'history',
  routes
})

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
