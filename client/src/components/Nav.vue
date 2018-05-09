<template>
    <div>
        <nav class="navbar" role="navigation" aria-label="main navigation">
        <div class="narbar-menu is-dark">
            <div class="navbar-start">
                <router-link class="navbar-item" to="/">Home</router-link>
                <router-link class="navbar-item" to="/create/party">Create Party</router-link>
                <router-link class="navbar-item" to="/login" v-if="!isLoggedIn">Login</router-link>
                <router-link class="navbar-item" to="/logout" v-if="isLoggedIn">Logout</router-link>
                
            </div>
            <div class="navbar-end">
            </div>
        </div>
        </nav>

        <nav class="main navbar">
            <div class="navbar-brand is-vcentered">
                <router-link to="/" class="name is-size-1">VOTE</router-link>
                <!-- <router-link to="/login" class="navbar-item is-size-5">Login</router-link> -->
            </div>
        </nav>   
    </div>
</template>

<script>
export default {
    data(){ 
        return { 
            test: "penis"
        }
    },

    computed: { 
        isLoggedIn() { 
            return this.$store.isLoggedIn
        }
    }
}
</script>


<style scoped>
.name {
  font-family: "Roboto Slab", serif;
}
.main {
  padding-top: 3vh;
  padding-bottom: 3vh;
  /* background: black; */
}
.main,
.main > .navbar-brand {
  text-align: center;
  display: block;
  width: 100%;
  font-family: "Arvo", serif;
}

.main > .navbar-brand > .name {
  color: white;
  background: black;
  padding: 0;
  padding-left: 1%;
  padding-right: 1%;
}

.main, .main > .navbar-brand > .navbar-item,
.navbar .navbar-brand .navbar-link {
  display: inline-block;
}

.navbar-item:hover {
  /* display: none; */
  text-decoration: underline;
  background: none;
}
</style>