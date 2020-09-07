<template>
  <div class="container" style="text-align: center">   
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
            <i class='fas fa-camera-retro' style='font-size:40px;color:blue'></i>
          </span>
        </label>        
      </image-uploader>
      <p v-if="error" class="text-danger mt-2">{{ error }}</p>     
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
      error: null,    
    }
  },
  methods: {
    setImage: function(output) {
      this.hasImage = true;
      this.image = output;
      console.log (this.image)
      if (this.image.exif.GPSLatitude) {
        this.calculateCoordPicture();  
        this.checkIfPicInRange()
        if(this.checkIfPicInRange()) {
          this.error = null
          this.checkImageLabels()                  
          this.imageConversion()
                    
        } else {this.error = "Votre photo ne semble pas avoir été prise dans ce restaurant"}
      } else {this.error = "Avez vous activé la géolocalisation sur votre téléphone?"}        
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