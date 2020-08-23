<template>
  <div>
    <div class="row">
      <div v-for="(picture, index) in storeState.pictures"
          :key="index"
          class="col-md-2 my-auto">   
          <div >                 
            <img class="img-thumbnail img-responsive" 
                :src="picture.url"
                @click="deleteMe(picture, picToDelete = index)">                           
          </div>          
      </div>      
    </div>    
	</div>
</template>

<script>
import { store } from "../common/store.js"
import { apiService } from "@/common/api.service.js";

export default {
  name:"PictureUpload",
  data () {
    return {
      picToDelete: null,
    }
  },
  computed:{
    storeState(){
      return store.state;
   }
  },
  methods: {
    deleteMe(picture) {     
      let endpoint = picture.apiUrl + picture.id +"/"
      let method = "DELETE";
      apiService(endpoint, method);
      console.log(this.picToDelete)
      store.deletePicture(this.picToDelete)
    }
  }
}
</script>


<style lang="stylus" scoped>
img: hover {

}
</style>
