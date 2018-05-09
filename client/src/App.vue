<template>
  <div id="app" class="container is-fluid">
    <app-nav></app-nav>

    <router-view></router-view>

  </div>
</template>

<script>
import appNav from './components/Nav.vue'

export default {
  name: 'app',
  data () {
    return {
    }
  },
  components: { 
    appNav
  },
}
</script>

<style>
  #app { 
    padding: 0;
    margin: 0;
  }

  * { 
    font-family: "Arvo", serif;
  }

  input:text { 
    border: none;
  }
</style>

<style>
    @import url('https://fonts.googleapis.com/css?family=Roboto+Slab:700|Arvo');
</style> 
