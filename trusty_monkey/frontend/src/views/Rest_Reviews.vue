<template>
  <div>
    <div class="card bg-info text-white mb-3 w-75 mt-3 mx-auto">
      <div class="card-header row ml-0 mr-0 justify-content-between">
        <div>
          <h2>{{ this.$route.params.name }}</h2>
        </div>
        <div class="row">
          <div>
            <button
              @click="isHidden= !isHidden"
              class="btn btn-sm btn-success mt-2 mr-2"
            >Horaires et Accés</button>
          </div>
          <div>
            <button
              v-show="showEditor== false"
              class="btn btn-sm btn-primary mt-2 mr-2"
              @click="addRestaurant(), showTheEditor()"
            >Ajouter une Review</button>

            <button
              v-show="showEditor== true"
              class="btn btn-sm btn-danger mt-2 mr-2"
              @click="deleteReview"
            >Annuler la Review</button>
          </div>
        </div>
      </div>

      <div v-show="isHidden">
        <div class="card-body row justify-content-around">
          <div class="mt-auto">
            <ul style="list-style-type:none">
              <h3>Horaires:</h3>
              <li v-for="item in this.$route.params.opening_hours " :key="item">{{ item }}</li>
            </ul>
          </div>
          <div>
            <img :src="mapUrl" />
          </div>
        </div>
      </div>
      <div
        class="card-footer"
      >{{ this.$route.params.adress }}_-|&|-_ {{ this.$route.params.website }}_-|&|-_ {{ this.$route.params.phone }}</div>
    </div>

    <div v-if="showEditor" class="container">
      <ReviewEditor :id="review_id" />
    </div>

    <div class="container mt-3">
      <div class="row mt-3" v-for="(review, index) in reviews" :key="review.pk">
        <div class="col-8">
          <h3 class="mb-0">
            Visité par:
            <b>{{ review.review_author }}</b>, le
            <i>{{ review.created_at }}</i>
          </h3>
          <hr class="mb-0" />
        </div>
        <div class="col-4 text-center my-auto">
          <button
            v-show="reviewToShow !== index"
            type="button"
            class="btn btn -sm btn-outline-info"
            @click="reviewToShow= index"
          >Consulter</button>
          <button
            v-show="reviewToShow == index"
            type="button"
            class="btn btn -sm btn-outline-danger"
            @click="reviewToShow= null"
          >Refermer</button>
        </div>
        <hr />

        <div v-show="reviewToShow == index">
          <ReviewDetail :id="review.id" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import ReviewDetail from "@/components/ReviewDetail.vue";
import ReviewEditor from "@/components/ReviewEditor.vue";
import { store } from "../common/store.js";
export default {
  name: "rest_reviews",
  props: {
    maps: { type: String, required: true }
  },
  data() {
    return {
      isHidden: false,
      reviewToShow: null,
      showEditor: false,
      reviews: [],
      review_id: 0,
      lat: this.$route.params.lat,
      lng: this.$route.params.lng,
      error: null,
      storeState: store.state
    };
  },
  components: {
    ReviewDetail,
    ReviewEditor
  },
  computed: {
    mapUrl() {
      const url = "https://maps.googleapis.com/maps/api/staticmap";
      const params = new URLSearchParams({
        center: `${this.$route.params.lat},${this.$route.params.lng}`,
        zoom: 15,
        size: "250x250",
        maptype: "terrain",
        key: "AIzaSyCGmIAISNa4W8KK24eXmH-ly_5k_vpAsos"
      });
      return `${url}?${params}`;
    }
  },
  methods: {
    getReviews() {
      let endpoint = `/api/rest_review/${this.maps}/`;
      apiService(endpoint).then(data => {
        this.reviews.push(...data);
      });
    },
    addRestaurant() {
      this.storeState.pictures = []
      let endpoint = `/api/restaurant/`;
      let method = "POST";
      let config = {
        maps: this.$route.params.maps,
        adress: this.$route.params.adress,
        name: this.$route.params.name
      };

      apiService(endpoint, method, config)
        .then(data => {
          console.log("Restaurant added!" + data);
          this.addReview();
        })
        .catch(error => console.log(error));
    },
    addReview() {
      let endpoint = `/api/restaurant_review/`;
      let method = "POST";
      apiService(endpoint, method, {
        maps: this.$route.params.maps,
        review_author: 1
      }).then(res => {
        this.review_id = res.id;        
      });
    },
    showTheEditor() {
      this.showEditor = true;
    },
    deleteReview() {
      let endpoint = `/api/restaurant_review/${this.review_id}/`;
      let method = "DELETE";
      apiService(endpoint, method);
      this.$router.push({ name: "home" });
    }
  },
  created() {
    this.getReviews();    
  },
  watch: {
    maps: function() {
      if (this.maps) {
        this.reviews = [];        
        this.getReviews();
      }
    }
  }
};
</script>

<style>
.naviMenu > ul li {
  list-style-type: none;
}
</style>