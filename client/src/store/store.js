import Vue from 'vue'
import Vuex from 'vuex'
import { SSL_OP_COOKIE_EXCHANGE } from 'constants';

Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        isLoggedIn: true
    },

    mutations: { 
        changeIsLoggedIn: state => { 
            console.log("hello")
            if (localStorage.getItem("token") != null) { 
                state.isLoggedIn = true

            } else { 
                state.isLoggedIn = false
                console.log("true")
            }
        }
    },

    getters: { 
        checkIfLoggedIn: state => { 
            return state.isLoggedIn
        }
    }
})