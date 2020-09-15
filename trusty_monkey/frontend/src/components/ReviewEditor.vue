<template>
<div class="editor">

  <div>
    <PictureUpload/>    
    <hr/>
  </div>

  <div>

  <div class="container text-center" v-show="this.storeState.preLoader">
    <div>
      <img src="https://media.giphy.com/media/pFwRzOLfuGHok/giphy.gif" class="w-25">
    </div>
    <div class="border border-success rounded w-50 mx-auto mt-3">
      <p class="text-success my-auto">Nos ingénieurs inspectent votre photo.</p>
    </div>
  </div>

  <div v-show="upUrl != null && this.storeState.showCatBut == false
                            && this.storeState.preLoader == false" 
                            class="col-md-6 mx-auto mb-3">
    <Resize/>
  </div>

  <div v-show="this.storeState.showCatBut== true">
    <div class="d-flex flex-row justify-content-around">
      <div class="mt-3" v-for="(buttonPic, index) in buttonPics"
                        :key="buttonPic">
        <button class="btn btn-sm btn-outline-success" 
                @click="upUrl= index, 
                setShowCatBut()"> {{ buttonPic }} </button>          
      </div>
    </div>        
  </div>

  <div class="d-flex flex-row ">      
        <button class="btn btn-success btn-sm m-3 " 
                @click="goHome">Soumettre</button>
        <div v-show="this.storeState.upError != null"
              class="container border border-danger rounded w-50 h-50 m-auto text-center">
          <p  class="text-danger my-auto">{{ this.storeState.upError }}</p>
        </div>
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
      if (this.storeState.labels) { 
        this.selectedFile = this.storeState.file            
        const fd = new FormData();
        let axiosConfig = {
          headers: {
            'X-CSRFTOKEN': CSRF_TOKEN,           
          }
        };
        
        if (this.upUrl == 0) {        
          if (this.storeState.labels.includes ('Food')) {
                this.endpoint = "starter_pic"                
                this.storeState.upError = null}
              else {store.setUpError("Ceci n'est pas la photo d'une entrée"),                    
                    this.endpoint = false,
                    store.setShowCatBut ()}
        } else if (this.upUrl == 1) {
          if (this.storeState.labels.includes ('Food')) {
                this.endpoint = "main_pic"                
                this.storeState.upError = null}
              else {store.setUpError("Ceci n'est pas la photo d'un plat"),                    
                    this.endpoint = false,
                    store.setShowCatBut ()}
        } else if (this.upUrl == 2) {          
              if (this.storeState.labels.includes ('Dessert')) {
                this.endpoint = "dessert_pic"                
                this.storeState.upError = null}
              else {store.setUpError("Ceci n'est pas la photo d'un dessert"),                    
                    this.endpoint = false,
                    store.setShowCatBut ()}
        } else if (this.upUrl == 3) {          
              if (this.storeState.labels.includes ('Text')) {
                this.endpoint = "menu_pic"                
                this.storeState.upError = null}
              else {store.setUpError("Ceci n'est pas la photo d'un menu"),                    
                    this.endpoint = false,
                    store.setShowCatBut()}
        } else if (this.upUrl == 4) {
          if (this.storeState.labels.includes ('Building')) {
                this.endpoint = "outside_pic"                
                this.storeState.upError = null}
              else {store.setUpError("Ceci n'est pas une photo de l'extérieur du restaurant"),                    
                    this.endpoint = false,
                    store.setShowCatBut ()}
        } else if (this.upUrl == 5) {
          if (this.storeState.labels.includes ('Restaurant')) {
                this.endpoint = "inside_pic"                
                this.storeState.upError = null}
              else {store.setUpError("Ceci n'est pas une photo de l'interieur du restaurant"),                    
                    this.endpoint = false,
                    store.setShowCatBut ()}
        } 
        
        if (this.endpoint != false){
          fd.append('picture_1', this.selectedFile)
          fd.append('restaurant_review', this.id)
          axios.post(`http://127.0.0.1:8000/api/${this.endpoint}/`, fd, axiosConfig)
            .then(res => {                                  
              this.upUrl = null              
              store.setShowCatBut()              
              let newPictureUrl = res.data.picture_1
              let newPictureId = res.data.id
              let apiURL = res.config.url
              let addPicDic = {"url": newPictureUrl,
                              "id": newPictureId,
                              "apiUrl": apiURL  }          
              store.addPicture(addPicDic)
              
          })
        }
      } else {console.log('pass le oinj')}
    },
    goHome() {
      this.$router.push({name: 'home'})           
    },
    setShowCatBut() {
      store.setShowCatBut()
      this.storeState.upError = null
    }
  }, 
  components: {
    PictureUpload,
    Resize
    },
  watch: {
    "storeState.labels": function () {
      this.onUpload()
      } 
    } 
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