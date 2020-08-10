<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
      <router-link :to="{ name: 'home' }" class="navbar-brand">TrustyMonkey</router-link>

      <div class="collapse navbar-collapse flex-row justify-content-end">
        <vue-google-autocomplete
          id="map"
          class="form-control mr-sm-2"
          placeholder="Rechercher un restaurant"
          v-on:placechanged="getAddressData"
          country="fr"
          types="establishment"
        ></vue-google-autocomplete>

        <ul class="navbar-nav mr-2">
          <li class="nav-item active">
            <a v-if="requestUser" class="btn btn-danger" href="/accounts/logout/">Se deconnecter</a>
            <a v-else class="btn btn-primary" href="/accounts/login/">Se connecter</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>


<script>
import VueGoogleAutocomplete from "vue-google-autocomplete";
export default {
  name: "NavbarComponent",
  components: { VueGoogleAutocomplete },
  data() {
    return {
      requestUser: null,
      addressData: ""
    };
  },
  created() {
    this.setRequestUser();
  },
  methods: {
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("username");
    },
    getAddressData(addressData, placeResultData) {
      this.placeResultData = placeResultData;
      this.addressData = addressData;
      console.log(
        this.placeResultData.name,
        this.placeResultData.formatted_address,
        this.placeResultData.place_id
      );
      this.$router.push({ name: "about", params: { id : this.placeResultData.place_id }})
    }
  }
};
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
  color: red !important;
}
#map {
  width: 45%;
}
.form-control {
  border-left: none;
  border-right: none;
  border-top: none;
  border-bottom: 1px solid lightblue;
}
</style>