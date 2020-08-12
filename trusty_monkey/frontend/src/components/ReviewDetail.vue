<template>
  <div>
    <div v-for="picture in pictures"
         :key="picture.pk">
         <h3>{{ picture.name_1 }}</h3>
         <h4>{{ picture.picture_1 }}</h4>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "ReviewDetail",
  data () {
    return {      
      pictures: [],           
    }
  },
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  methods: {
    getPictures() {
      let endpoint = `/api/every_review_pics/${this.id}/`;            
      apiService(endpoint)        
        .then(data => {          
          this.pictures.push(...data)                   
      })      
     },
  },
  
  created() {      
    this.getPictures()
    // console.log(this.pictures)   
  } 
};
</script>

<style>
</style>