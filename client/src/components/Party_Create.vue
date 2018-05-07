<template>
  <div>
      <div class="columns">
          <div class="column is-4 is-offset-4">
              <div class="field">
                  <input class="input" type="text" placeholder="party name" v-model="name">
              </div>
              <div class="field">
                  <input class="input" type="text" v-model="detail">
              </div>
              <div class="field">
                  <input type="button" class="button is-success" value="Create" @click="createParty()">
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
            name: "",
            detail: ""
        }
    },
    methods: { 
        createParty(){ 
            // const data = {name: this.name, detail: this.detail}
            // const opt = {
            //     method: "POST",
            //     headers: {
            //         'cookies'
            //     }
            // }
            axios("http://192.168.1.2:8000/party/", { 
                method: "POST",
                data: { 
                    name: this.name,
                    detail: this.detail
                },
                withCredentials: true
            })

        }
    }
}
</script>

