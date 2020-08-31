<template>
  <div class="container">   
    <div class="my-8">
      <image-uploader
        :preview="false"
        :className="['fileinput', { 'fileinput--loaded': hasImage }]"
        capture="environment"
        :debug="1"
        :quality="1"
        doNotResize="gif"
        :autoRotate="true"
        outputFormat="verbose"
        @input="setImage"
        >
        <label for="fileInput" slot="upload-label">        
          <span class="upload-caption">
            "Ajouter une photo"
          </span>
        </label>
      </image-uploader>      
    </div>    
  </div>
</template>

<script>
import mixin from "../mixin/mixin.js"
import ImageUploader from 'vue-image-upload-resize'
import { store } from "../common/store.js";

export default {
  name: "Resize",
  mixins: [mixin],
  computed:{
    storeState(){
      return store.state;
   }
  },
  data() {
    return {      
      hasImage: false,
      image: null,      
    }
  },
  methods: {
    setImage: function(output) {
      this.hasImage = true;
      this.image = output;      
      this.calculateCoordPicture();      
      console.log(this.storeState.restLat, this.storeState.restLng);
      console.log(this.lat, this.lng);
      this.checkIfPicInRange()
    },   
  },
  components: {
    ImageUploader
  }
}

</script>


<style>
#fileInput {
  display: none;
}
</style>