<template>
  <div>
    <div style="height:200px">
      <h3>Pics preview</h3>
    </div>
    <hr/>

    <div >    
      <div>  
      <input type="file" @change="onFileSelected">
      <button @click="onUpload">Charger</button>
      </div>

      
        <div class="d-flex flex-row justify-content-around">
          <div class="mt-3" v-for="(buttonPic, index) in buttonPics"
              :key="buttonPic">
            <button class="btn btn-sm btn-success"
            @click="upUrl= index">
            {{ buttonPic }} </button>
          </div>
        </div> 
      
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { CSRF_TOKEN } from "../common/csrf_token.js"

export default {
  name: "ReviewEditor",
  data() {
    return {
      selectedFile : null,
      buttonPics : ['Entrée', 'Plat-principal', 'Dessert', 'menu', 'Extérieur', 'Intérieur'],
      upUrl : null,        
    }
  },
  props: {
    id: {
      type: Number,
      required: true
    },
  },  
  methods: {
    onFileSelected(event) {
      this.selectedFile = event.target.files[0]     
    },
    onUpload() {      
      const fd = new FormData();
      let axiosConfig = {
        headers: {
            'X-CSRFTOKEN': CSRF_TOKEN,           
        }
      };
      fd.append('picture_1', this.selectedFile)
      fd.append('restaurant_review', this.id)
      axios.post('http://127.0.0.1:8000/api/main_pic/', fd, axiosConfig)
        .then(res => {
          console.log(res)
        })
    },   
  },   
}
</script>
<style>
</style>