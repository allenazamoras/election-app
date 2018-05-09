<template>
    <div class="columns">
        <div class="column is-one-third is-offset-4 is-8-mobile" style="padding: 20px;"> 
            <h1 class="is-size-3 has-text-centered">Login</h1>
            <div class="notification is-danger" v-if="error == true">
                <button class="delete" @click="error = !error"></button> 
                Wrong credentials!
            </div>
            <div class="field">
                <label class="label">Username</label>
                <div class="control">
                    <input type="text" class="is-radiusless input is-medium " placeholder="" v-model="username">
                </div>
            </div> 
            <div class="field">
                <label class="label">Password</label>
                <div class="control">
                    <input type="password" class="is-radiusless input is-medium " placeholder="" v-model="password">
                </div>
            </div> 
            <div class="field">
                <div class="control">
                    <a type="button" class="is-radiusless button is-dark is-medium loginBtn" :class="{'is-loading': isLoading}" @click="login">Login</a>
                </div>
            </div> 
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() { 
        return { 
            username: "admin",
            password: "password123",
            isLoading: false,
            error: false,
        }
    },

    methods: {
        login() {
            let config = { 
                headers: {"token": "60515ce1fab71f4a8af442f6388f02096c9ee6f9"}
            }
            this.isLoading = true
            axios.post("http://192.168.1.2:8000/api-token-auth/", {
                username: this.username,
                password: this.password
            })
            .then( (res) => {
                console.log(res)
                if(res.data.token.length == 0){ 
                    this.$toast.open({
                        message: "Invalid credentials",
                        type: "is-danger"
                    })

                    this.isLoading = false
                }else if(res.data.token.length != 0){ 
                    this.$toast.open({
                        message: "Logged in",
                        type: "is-success"
                    })

                    localStorage.setItem("token", res.data.token);
                    this.$store.commit("changeIsLoggedIn")
                }
            })

            .catch ( (res) => {
                console.log(res)

                this.$toast.open({
                    message: "Network error.",
                    type: "is-danger"
                })

                this.isLoading = false
            })
        },
    },
}
</script>

<style>
    /* html, body{ 
        background: #01b4bc;
    } */
</style>


<style scoped>
    .loginBtn{ 
        display: block;
        width: 100%;
    }
</style>
