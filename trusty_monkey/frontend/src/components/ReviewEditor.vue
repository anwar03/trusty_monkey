<template>
<div class="editor">

  <div>
    <PictureUpload/>    
    <hr/>
  </div>

  <div>    
    
  <div v-show="upUrl != null && this.storeState.submit == false 
                            && this.showCatBut == false" 
                            class="col-md-6 mx-auto mb-3">
    <Resize/>
  </div>

  <div v-show="this.storeState.submit== true" >
    
    <div class="d-flex flex-row justify-content-around mb-3">
      <button class="btn btn-sm btn-success" 
              @click="onUpload"> Ajouter </button>
      <button class="btn btn-sm btn-danger"
              @click="showCatBut= true, submit= false,
              upUrl= null"> Annuler </button>
    </div>
  </div>

  <div v-show="showCatBut== true">
    <div class="d-flex flex-row justify-content-around">
      <div class="mt-3" v-for="(buttonPic, index) in buttonPics"
                        :key="buttonPic">
        <button class="btn btn-sm btn-outline-success" 
                @click="upUrl= index, 
                showCatBut= false"> {{ buttonPic }} </button>          
      </div>
    </div>        
  </div>

  <div>      
        <button class="btn btn-success btn-sm m-3 " 
                @click="goHome">Soumettre</button>
        <p v-if="error" class="text-danger mt-2">{{ error }}</p>
  </div>  

  </div>
</div> 
</template>

<script>
import { store } from "../common/store.js"
import axios from 'axios'
import { CSRF_TOKEN } from "../common/csrf_token.js"
import PictureUpload from "@/components/PictureUpload.vue";
import Resize from "@/components/Resize.vue"

export default {
  name: "ReviewEditor",
  computed:{
    storeState(){
      return store.state;
   }
  },
  data() {
    return {
      error: null,
      selectedFile: null,
      upUrl: null,
      submit: false,
      showCatBut: true,
      endpoint: null,      
      newPictureUrl: null,      
      buttonPics: ['Entrée', 'Plat-principal',
                  'Dessert', 'Menu', 'Extérieur',
                  'Intérieur'],                         
    }
  },
  props: {
    id: {
      type: Number,
      required: true
    },
  },  
  methods: {       
    onUpload() {
      this.selectedFile = this.storeState.file
      store.setSubmit()      
      // this.submit = true     
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
      } else if (this.upUrl == 2) {
          for(var i = 0; i < this.storeState.labels.length; i++) {
            if (this.storeState.labels[i] == 'Dessert') {
              this.endpoint = "dessert_pic"
              this.storeState.labels = []
              this.error = null}
            else {this.error = "Ceci n'est pas la photo d'un dessert",
                  this.storeState.labels = []
                  this.endpoint = false,
                  this.showCatBut = true}
          }
      } else if (this.upUrl == 3) {
          for(var o = 0; o < this.storeState.labels.length; o++) {
            if (this.storeState.labels[o] == 'Text') {
              this.endpoint = "menu_pic"
              this.storeState.labels = []
              this.error = null
              break}
            else {this.error = "Ceci n'est pas la photo d'un menu",
                  this.storeState.labels = []
                  this.endpoint = false,
                  this.showCatBut = true}
          }
      } else if (this.upUrl == 4) {
        this.endpoint = "outside_pic"
      } else if (this.upUrl == 5) {
        this.endpoint = "inside_pic"
      } 
      
      if (this.endpoint != false){
        fd.append('picture_1', this.selectedFile)
        fd.append('restaurant_review', this.id)
        axios.post(`http://127.0.0.1:8000/api/${this.endpoint}/`, fd, axiosConfig)
          .then(res => {                                  
            this.upUrl = null
            this.submit = false
            this.showCatBut = true
            let newPictureUrl = res.data.picture_1
            let newPictureId = res.data.id
            let apiURL = res.config.url
            let addPicDic = {"url": newPictureUrl,
                            "id": newPictureId,
                            "apiUrl": apiURL  }          
            store.addPicture(addPicDic)
        })
      }
    },
    goHome() {
      this.$router.push({name: 'home'})           
    }
  }, 
  components: {
    PictureUpload,
    Resize
    }, 
  }
</script>

<style>
.editor {
  background-color: white;
  border: 1px solid 
}
.custom-file-label {
  background-color: rgb(234, 236, 122);
}
</style>