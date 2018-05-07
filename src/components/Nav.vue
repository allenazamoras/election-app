<template>
    <div>
        <div class="columns">
            <div class="column is-12 has-text-centered">
                <span class="is-size-1">
                    <router-link to="/" style="color: white;">VOTE</router-link>
                </span>
            </div>
        </div>

        <!-- <div class="navbar is-dark">
            <div class="navbar-menu">
                <router-link to="/" class="navbar-item">Home</router-link>
            </div>
        </div> -->

        <!-- <nav class="navbar is-dark has-shadow">
        <div class="navbar-brand">
            <router-link class="navbar-item" to="/">
                ELECT
            </router-link>
            <div class="navbar-burger burger" data-target="navbarExampleTransparentExample">
            <span></span>
            <span></span>
            <span></span>
            </div>
        </div>

        <div class="navbar-menu">
            <div class="navbar-start">
            <router-link to="/" class="navbar-item">Home</router-link>
            <router-link to="/party" class="navbar-item">Parties</router-link>

            <div class="navbar-item has-dropdown is-hoverable">
                <!-- <router-link to="/"></router-link> -->
                <!-- <a class="navbar-link" href="">
                Docs
                </a> -->
                <!-- <div class="navbar-dropdown is-boxed">
                <a class="navbar-item" href="/documentation/overview/start/">
                    Overview
                </a>
                <a class="navbar-item" href="https://bulma.io/documentation/modifiers/syntax/">
                    Modifiers
                </a>
                <a class="navbar-item" href="https://bulma.io/documentation/columns/basics/">
                    Columns
                </a>
                <a class="navbar-item" href="https://bulma.io/documentation/layout/container/">
                    Layout
                </a>
                <a class="navbar-item" href="https://bulma.io/documentation/form/general/">
                    Form
                </a>
                <hr class="navbar-divider">
                <a class="navbar-item" href="https://bulma.io/documentation/elements/box/">
                    Elements
                </a>
                <a class="navbar-item is-active" href="https://bulma.io/documentation/components/breadcrumb/">
                    Components
                </a>
                </div>
            </div>
            </div>

            <div class="navbar-end">
            <div class="navbar-item">
                <div class="field is-grouped">
                    <p class="control">
                        <router-link 
                            class="button  is-info"
                            to="/register">
                            REGISTER
                        </router-link>
                    </p>
                    <p class="control">
                        <router-link 
                            class="button  is-info is-outlined"
                            to="/login">
                            LOGIN
                        </router-link>
                    </p>                    
                </div>
            </div>
            </div>
        </div>
        </nav>         -->
    </div>
</template>

<style>
    @import url('https://fonts.googleapis.com/css?family=Roboto+Slab:700');
</style> 
<style scoped>
    .columns{ 
        font-family: 'Roboto Slab', serif;
        margin-top: 5vh;
    }

    span { 
        padding-left: 0.5%;
        padding-right: 0.5%;
        background: black;
        color: white;
        /* text-decoration: none; */
    }
</style>

