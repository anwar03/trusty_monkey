<template>
  <div id="app">
    <NavbarComponent />
    <router-view />
  </div>
</template>

<script>
import NavbarComponent from "@/components/Navbar.vue";
export default {
  name: "App",
  components: {
    NavbarComponent
  },  
}
</script>



<style>
html, body {
    height: 100%;
    font-family: "Montserrat", serif;           
}
</style>
