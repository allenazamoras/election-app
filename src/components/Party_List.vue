<template>
    <div>
        <div class="columns">
            <div class="column is-4" v-for="item in list" v-bind:key="item.id">
                {{ item.name }} {{ item.detail }}
                <div class="card">

                <div class="card-content">
                    <div class="content">
                        {{ item.detail }}
                    <br>
                    </div>
                </div>
                </div>                
            </div>                       
        </div>
    </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css?family=Slabo+27px');
</style> 

<style scoped>
    * { 
        font-family: 'Slabo 27px', serif;        
    }
</style>


<script>
import axios from 'axios'

export default {
    data() { 
        return { 
            list: undefined
        }
    },
    created: function() { 
        axios.get("http://192.168.1.2:8000/party/")
        .then( (res) => {
            console.log(res.data)
            this.list = res.data
        })
        .catch( (res) => { 
            console.log(res)
        })
    }
}
</script>

