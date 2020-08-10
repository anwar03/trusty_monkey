<template>
  <div>
    <div class="card bg-info text-white mb-3 w-75 mt-3 mx-auto">
      <div class="card-header">{{ this.$route.params.name }}</div>
        <div class="card-body">
          <ul style="list-style-type:none mb-0">
            <li v-for="item in this.$route.params.opening_hours " :key="item">
            {{ item }}
            </li>
          </ul>    
        </div>
          <div class="card-footer">
            {{ this.$route.params.adress }}|       {{ this.$route.params.website }}| {{ this.$route.params.phone }}
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
      reviews: []
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