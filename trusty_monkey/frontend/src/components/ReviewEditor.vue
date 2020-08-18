<template>
  <div>
    <div style="height:200px">
      <h3>Pics preview</h3>
    </div>
    <hr/>

    <div >    
      <div class="d-flex flex-row">
      <div v-show="upUrl != null" class="custom-file">
        <input type="file" class="custom-file-input" @change="onFileSelected">
        <label class="custom-file-label" for="customFile">Choose file</label>
      </div>
      <button v-if="showPost= true" class="btn btn-sm btn-danger" @click="onUpload"> Soumettre </button>       
      </div>
      
      <div class="d-flex flex-row justify-content-around">
        <div class="mt-3" v-for="(buttonPic, index) in buttonPics" :key="buttonPic">
          <button class="btn btn-sm btn-outline-success" @click="upUrl= index"> {{ buttonPic }} </button>
          
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
      selectedFile: null,
      upUrl: null,
      endpoint: null,
      showPost: false,      
      buttonPics: ['Entrée', 'Plat-principal', 'Dessert', 'menu', 'Extérieur', 'Intérieur'],              
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
      if (this.upUrl == 0) {
        this.endpoint = "starter_pic"
      } else if (this.upUrl == 1) {
        this.endpoint = "main_pic"
      }  else if (this.upUrl == 2) {
        this.endpoint = "dessert_pic"
      } else if (this.upUrl == 3) {
        this.endpoint = "menu_pic"
      } else if (this.upUrl == 4) {
        this.endpoint = "outside_pic"
      } else if (this.upUrl == 5) {
        this.endpoint = "inside_pic"
      } 
      fd.append('picture_1', this.selectedFile)
      fd.append('restaurant_review', this.id)
      axios.post(`http://127.0.0.1:8000/api/${this.endpoint}/`, fd, axiosConfig)
        .then(res => {
          console.log(res)
          this.upUrl = null
        })
    },   
  },   
}
</script>

<style>

</style>