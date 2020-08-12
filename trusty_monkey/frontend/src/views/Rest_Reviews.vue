<template>
  <div>
    <div class="card bg-info text-white mb-3 w-75 mt-3 mx-auto">

      <div class="card-header row ml-0 mr-0 justify-content-between">
        <div><h2>{{ this.$route.params.name }}</h2></div>
        <div><button @click= "isHidden= !isHidden" class="btn btn-sm btn-success mt-2">Horaires et Accés</button></div>      
      </div>

      <div v-if="isHidden">
        <div class="card-body row justify-content-around">
          <div class="mt-auto">
          <ul style="list-style-type:none">
            <h3>Horaires:</h3>
            <li v-for="item in this.$route.params.opening_hours " :key="item">
            {{ item }}
            </li>
          </ul>
          </div>
          <div>
          <img :src="mapUrl">
          <!-- <iframe width="600" height="450" frameborder="0" style="border:0"
          src="https://www.google.com/maps/embed/v1/place?key=AIzaSyCGmIAISNa4W8KK24eXmH-ly_5k_vpAsos&q=ChIJf9gUSrhZqxIROfbSqVH44Bg" allowfullscreen>
          </iframe> -->
          </div>    
        </div>
      </div>

          <div class="card-footer">
            {{ this.$route.params.adress }}_-|&|-_ {{ this.$route.params.website }}_-|&|-_ {{ this.$route.params.phone }}
        </div>
    </div>
    
    <div class="container mt-3">
      <hr>      
      <div class="row mt-3"
            v-for="review in reviews"
            :key="review.pk">
        <div class="col-8">
          <h3 class="mb-0">Visité par:
            <b>{{ review.review_author }}</b>, le  <i>{{ review.created_at }}</i>
          </h3>          
          <hr class="mb-0">    
        </div>
        <div class="col-4 text-center my-auto">
          <button type="button" class="btn btn -sm btn-outline-info">Consulter</button> 
        </div>   
        <hr>
      </div>
    </div>
  </div>
</template>


<script>
import { apiService } from "@/common/api.service.js"
export default {
  name: "rest_reviews",
  props: {
    maps: { type: String,
            required: true
          }
  },  
  data () {
    return {
      isHidden: false,
      reviews: [],
      lat: this.$route.params.lat,
      lng: this.$route.params.lng,
    }
  },
  computed: {
  mapUrl () {
    const url = "https://maps.googleapis.com/maps/api/staticmap"
    const params = new URLSearchParams({
      center: `${this.$route.params.lat},${this.$route.params.lng}`,
      zoom: 15,
      size: "250x250",
      maptype: "terrain",
      key: "AIzaSyCGmIAISNa4W8KK24eXmH-ly_5k_vpAsos"
    })
    return `${url}?${params}`
   }
  },
  methods: {
    getReviews() {
      let endpoint = `/api/rest_review/${this.maps}/`;
      apiService(endpoint)
        .then(data => {          
          this.reviews.push(...data)
          console.log(this.maps)        
      })
    }
  },
  created() {      
    this.getReviews()
    console.log(this.reviews)
    }  
};
 
</script>

<style>
.naviMenu > ul li { 
    list-style-type: none;
}
</style>