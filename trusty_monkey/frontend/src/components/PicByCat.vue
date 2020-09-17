<template>
 
  <div >
      
    <div class="row flex mt-4 bg-light ">        
      <div class="col-md-6 mt-3 mb-3">
        <div class="row" id="grid">
          <div v-for="(catPicture, index) in picByCat"
          :key="catPicture.pk"
          class="col-md-3 my-auto"
          >
            
          <div @click="picShow= index">                 
            <img class="img-thumbnail img-responsive" :src="catPicture.picture_1">
          </div>
          </div>  
        </div>
      </div>

      <div class="col-6 d-flex align-items-center justify-content-center mt-3 mb-3" style="width:450px; height:450px;">        
          <div v-if="picShow!==null">                    
             <img :src="picByCat[picShow].picture_1" class="img-responsive" style="width:auto; height:auto; max-width:450px; max-height:450px;"/>     
          </div>    
      </div>
      
    </div>
  </div>
</template>

<script>
export default {
  name: "PicByCat",
  data () {
    return {   
      picShow: null,               
    }
  },
  props: {
   picByCat: {
      type: Array,
      required: true
    }
  },    
} 
</script>
