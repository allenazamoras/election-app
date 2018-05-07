<template>
    <div>
        {{ partyList }}
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() { 
        return { 
            partyList: undefined
        }
    },

    methods: { 
        getParty(){

            // return this.partyList
        }
    },

    created: function() { 
        axios.get(`http://192.168.1.2:8000/party/${this.$route.params.id}/`)
        .then( (res) => {
            console.log(res)
            this.partyList = res
        })        
    },
}
</script>

