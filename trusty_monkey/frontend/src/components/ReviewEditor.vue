<template>
  <div>
    <div style="height:200px">
      <h3>Pics preview</h3>
    </div>
    <hr/>
    <div style="height:250px">    
      <div>  
      <input type="file" @change="onFileSelected">
      <button @click="onUpload">Charger</button>
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
      axios.post('http://127.0.0.1:8000/api/outside_pic/', fd, axiosConfig)
        .then(res => {
          console.log(res)
        })
    }
  },
  created() {
    console.log(this.id)    
  }
}
</script>
<style>
</style>