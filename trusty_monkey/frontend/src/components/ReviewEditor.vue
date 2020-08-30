<template>
<div class="editor">

  <div>
    <PictureUpload/>    
    <hr/>
  </div>

    <div>    
      
      <div v-show="upUrl != null && submit == false" class="col-md-6 mx-auto mb-3">
        <div class="d-flex">          
            <input type="file"
                  class="custom-file-input"
                  @change="onFileSelected">
            <label class="custom-file-label" 
                    for="customFile">Choisir une photo</label>          
        </div>         
      </div>

      <div v-show="submit== true" >
        <div class="d-flex flex-row justify-content-around mb-3">
          <button class="btn btn-sm btn-success" 
                  @click="onUpload"> Soumettre </button>
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
  computed:{
     storeState(){
    return store.state;
   }
  },
  data() {
    return {
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
    onFileSelected(event) {
      this.selectedFile = event.target.files[0]
      this.submit = true                 
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
          this.submit = false
          this.showCatBut = true
          store.uploadedPicture()
          let newPictureUrl = res.data.picture_1
          let newPictureId = res.data.id
          let apiURL = res.config.url
          let addPicDic = {"url": newPictureUrl,
                          "id": newPictureId,
                          "apiUrl": apiURL  }          
          store.addPicture(addPicDic)
        })
    },
    goHome() {
      this.$router.push({name: 'home'});
       
    }
  }, 
  components: {
    PictureUpload
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