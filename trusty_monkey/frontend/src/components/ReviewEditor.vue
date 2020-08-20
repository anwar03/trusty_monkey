<template>
<div>

  <div>
    <PictureUpload/>    
    <hr/>
  </div>

    <div>    
      
      <div v-show="upUrl != null && submit == false" class="custom-file">
        <div class="d-flex flex-row">
          <input type="file" class="custom-file-input" @change="onFileSelected">
          <label class="custom-file-label" for="customFile">Choose file</label>
        </div>         
      </div>

      <div v-show="submit== true" >
        <div class="d-flex flex-row justify-content-around">
          <button class="btn btn-success" @click="onUpload"> Soumettre </button>
          <button class="btn btn-danger" @click="showCatBut= true, submit= false, upUrl= null"> Annuler </button>
        </div>
      </div>

      <div v-show="showCatBut== true">
        <div class="d-flex flex-row justify-content-around">
          <div class="mt-3" v-for="(buttonPic, index) in buttonPics" :key="buttonPic">
            <button class="btn btn-sm btn-outline-success" @click="upUrl= index, showCatBut= false"> {{ buttonPic }} </button>          
          </div>
        </div>
         <div class='mt-3'>          
            <p><i>(Plus que {{ totalPics }} pour términer!)</i></p>          
        </div>
      </div>

      <div v-show="totalPics == 0">
            <h1> Submit button </h1>
      </div>  

    </div>

</div> 
</template>

<script>
import { store } from "../common/store.js"
import axios from 'axios'
import { CSRF_TOKEN } from "../common/csrf_token.js"
import PictureUpload from "@/components/PictureUpload.vue";

export default {
  name: "ReviewEditor",
  data() {
    return {
      selectedFile: null,
      upUrl: null,
      submit: false,
      showCatBut: true,
      endpoint: null,
      totalPics: 6,
      newPicture: null,    
      buttonPics: ['Entrée', 'Plat-principal', 'Dessert', 'Menu', 'Extérieur', 'Intérieur'],                     
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
      this.submit = true                 
    },
    addPicture(newPicture) {
      store.addPicture(String(newPicture))
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
          this.upUrl = null
          this.submit = false
          this.showCatBut = true
          this.totalPics -= 1
          let newPicture = res.data.picture_1
          this.addPicture(newPicture) 
    })
    }
  },
  watch: {
    totalPics: function() {
      if (this.totalPics == 0) {     
        this.upUrl= null,
        this.submit= false,
        this.showCatBut= false        
      }
    }
  },
  components: {
    PictureUpload
    }, 
  }

</script>

<style>

</style>