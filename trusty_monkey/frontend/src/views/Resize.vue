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
import axios from 'axios'
import { CSRF_TOKEN } from "../common/csrf_token.js"

export default {
  name: "Resize",
  mixins: [mixin],
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
      this.calculateCoordPicture()
      
      const fd = new FormData();
      let axiosConfig = {
        headers: {
          'X-CSRFTOKEN': CSRF_TOKEN,           
        }
      };     
      fd.append('picture_1', this.image)
      fd.append('restaurant_review', 369)
      axios.post(`http://127.0.0.1:8000/api/main_pic/`, fd, axiosConfig)
        .then(res => {  
          console.log(res) })           
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