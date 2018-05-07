<template>
    <div class="columns">
        <div class="column is-one-third is-offset-4 is-8-mobile box has-shadow" style="padding: 20px;"> 
            <h1 class="is-size-3 has-text-centered">Login</h1>
            <div class="notification is-danger" v-if="error == true">
                <button class="delete" @click="error = !error"></button> 
                Wrong credentials!
            </div>
            <div class="field">
                <label class="label">Username</label>
                <div class="control">
                    <input type="text" class="input is-medium " placeholder="" v-model="username">
                </div>
            </div> 
            <div class="field">
                <label class="label">Password</label>
                <div class="control">
                    <input type="password" class="input is-medium " placeholder="" v-model="password">
                </div>
            </div> 
            <div class="field">
                <div class="control">
                    <a type="button" class="button  is-success is-medium loginBtn" :class="{'is-loading': isLoading}" @click="login">Login</a>
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
            username: "",
            password: "",
            isLoading: false,
            error: false,
        }
    },

    methods: {
        login() {
            this.$cookies.set("session", "HJHAHAHAH")
            this.isLoading = true
            axios.post("http://192.168.1.2:8000/login/", {
                username: this.username,
                password: this.password
            })

            .then( (res) => {
                console.log(res)
                if(res.data.success == 0){ 
                    this.$toast.open({
                        message: "Invalid credentials",
                        type: "is-danger"
                    })

                    this.isLoading = false
                }else if(res.data.success == 1){ 
                    this.$toast.open({
                        message: "Logged in",
                        type: "is-success"
                    })

                    this.$cookies.set("session", res.data.session)
                }

                this.$cookies.set("session", "HJHAHAHAH")
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
