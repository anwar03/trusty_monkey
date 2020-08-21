<template>
  <div>
    <div>
          <div v-for="picture in storeState.pictures"
          :key="picture"
          class="col-md-4 my-auto">   
          <div >                 
            <img class="img-thumbnail img-responsive" :src="picture">
          </div>
          </div>  
    </div>
	</div>
</template>

<script>
import { store } from "../common/store.js"

export default {
	name:"PictureUpload",
	data() {
		return {
		storeState: store.state
		};
	}
}
</script>

<style>

</style>