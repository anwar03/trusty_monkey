<template>
<div>
  <div style="height:200px">
    <h3>Pics preview</h3>
  </div>
  <hr/>
  <div style="height:250px">    
    <div class="custom-file">  
    <input type="file" @change="onFileSelected">
    <button @click="onUpload">Charger</button>
</div>
  </div>
</div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  data() {
    return {
      selectedFile: null
    }
  },
  methods: {   
    onFileSelected(event) {
      this.selectedFile = event.target.files[0]
      // console.log(this.selectedFile)
    },
    onUpload () {
      let formData = new FormData();
      formData.append('picture_1', 'this.selectedFile')
      formData.append('restaurant_review', 65)
      console.log(formData);
      let endpoint = `/api/outside_pic/`
      let method = "POST"
      let config = formData
      apiService(endpoint, method, config)      
    }
  }
}
</script>

<style>
</style>