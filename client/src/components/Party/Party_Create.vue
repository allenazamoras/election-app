<template>
  <div>
      <div class="columns">
          <div class="column is-4 is-offset-4">
              <div class="field">
                  <input class="input is-radiusless" type="text" placeholder="party name" v-model="name">
              </div>
              <div class="field">
                  <input class="input is-radiusless" type="text" v-model="detail">
              </div>
              <div class="field">
                  <input type="button" style="width: 100%" class="button is-medium is-success is-radiusless" value="Create" @click="createParty()">
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
            let config = { 
                headers: {
                    Authorization: "Token 60515ce1fab71f4a8af442f6388f02096c9ee6f9",
                }
            }

            axios.post("http://192.168.1.2:8000/party/", {
                name: this.name,
                detail: this.detail
            }, config)

            .then(res => {
                console.log(res)
            })
        }
    }
}
</script>

<style>
  input[type="text"] { 
    /* border: none; */
  }
</style>

