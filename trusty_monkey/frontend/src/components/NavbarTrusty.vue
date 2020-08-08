<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
      <router-link :to="{ name: 'home' }" class="navbar-brand">TrustyMonkey</router-link>

      <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto mr-2">         
          <li class="nav-item active">
            <a v-if="requestUser" class="btn btn-sm btn-danger" href="/accounts/logout/">Se deconnecter</a>
            <a v-else class="btn btn-sm btn-primary" href="/accounts/login/">Se connecter</a>
          </li>          
        </ul>

        <form class="form-inline my-2 my-lg-0">
          <input
            class="form-control mr-sm-2"
            type="search"
            placeholder="Search"
            aria-label="Search"
          />
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent",
  data() {
    return {
      requestUser:null }
      },
      methods: {
        setRequestUser() {     
          this.requestUser = window.localStorage.getItem("username")
          }         
      },
      created() {
        this.setRequestUser()
      }
  
}
</script>

<style scoped>
.my-navbar {
  border-bottom: 1px solid grey;
}
.navbar-brand {
  font-weight: bold;
  font-size: 200%;
}
.navbar-brand:hover {
  color: lightblue !important;
}
</style>