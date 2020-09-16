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
        <!-- <label for="fileInput" slot="upload-label"> -->
        <div>
          <span>
            <i class='fas fa-camera-retro' style='font-size:40px;color:blue'></i> 
          </span>
        </div>
        <!-- </label> -->
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
      error: null,   
    }
  },
  methods: {
    setImage: function(output) {
      store.setPreloader()
      this.hasImage = true;
      this.image = output;
      // if (this.image.exif != null) {
      // console.log (this.image)
      //   if (this.image.exif.GPSLatitude) {
      //     this.calculateCoordPicture();  
      //     this.checkIfPicInRange()
      //     if(this.checkIfPicInRange()) {
      //       this.error = null
      //       this.checkImageLabels()                               
      //       this.imageConversion()                    
      //     } else {store.setUpError("Votre photo ne semble pas avoir été prise dans ce restaurant")
      //             store.setShowCatBut()}
      //   } else {store.setUpError("Avez vous activé la géolocalisation sur votre téléphone?")
      //           store.setShowCatBut()}
      // } else {store.setUpError("Avez vous activé la géolocalisation sur votre téléphone?")
      //         store.setShowCatBut()}
      this.checkImageLabels()                               
      this.imageConversion() 
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