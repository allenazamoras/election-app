import Vue from 'vue'
import Router from 'vue-router'
import Cookies from 'vue-cookies'

import Buefy from 'buefy'
import 'buefy/lib/buefy.css'

//Components
import Login from './components/Login.vue'
import App from './App.vue'
import Party from './components/Party/Party_View.vue'
import Party_Create from './components/Party/Party_Create.vue'
import Party_List from './components/Party/Party_List.vue'
import Home_View from './components/Home/Home_View.vue'
import Logout from './components/Logout.vue'

import { store } from './store/store'

// Using modules
Vue.use(Router)
Vue.use(Buefy)

const routes = [
  { path: "/test", component: Home_View},
  { path: "/login", component: Login },
  { path: "/party", component: Party_List },
  { path: "/party/:id", component: Party },
  { path: "/create/party", component: Party_Create },
  { path: "/logout", component: Logout}
]

const router = new Router({
  mode: 'history',
  routes
})

new Vue({
  store: store,
  el: '#app',
  router,
  render: h => h(App)
})