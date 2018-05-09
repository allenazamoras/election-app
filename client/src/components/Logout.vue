<template>
  <div>
      Logging out
  </div>
</template>

<script>
export default {
    created() { 
        localStorage.removeItem("token")
        this.$router.push("/")
    }
}
</script>