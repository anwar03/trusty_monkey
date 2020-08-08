<template>
  <div class="home">
    <div class="container mt-3">      
      <div class="row mt-3"
            v-for="review in reviews"
            :key="review.pk">
        <div class="col-8">
          <p class="mb-0">Visité par:
            <span><b>{{ review.review_author }}</b>, le  <i>{{ review.created_at }}</i></span>
          </p>
          <h2><b>{{ review.restaurant_name }}</b></h2>
          <p>{{ review.restaurant_adress }}</p> 
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
  name: "home",
  data () {
    return {
      reviews: []
    }
  },
  methods: {
    getReviews() {
      let endpoint = "/api/restaurant_review/";
      apiService(endpoint)
        .then(data => {          
          this.reviews.push(...data)          
      })
    }
  },
  created() {      
    this.getReviews()
    console.log(this.reviews) 
    }  
};
</script>
