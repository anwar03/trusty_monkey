import haversine from "haversine"
import axios from "axios"


export default {
  data() {
    return {      
      lat: null,
      lng: null,
      apiKey: "AIzaSyCGmIAISNa4W8KK24eXmH-ly_5k_vpAsos",
      picToCheck: null,    
    }
  },  
  methods: {
    calculateCoordPicture() {     
      var latitudes = []
      var longitudes = []
      var i
      for (i = 0; i < 3; i++){      
        var coord = Object.values(this.image.exif.GPSLatitude[i])[0]      
        latitudes.push(coord)}
      for (i = 0; i < 3; i++){      
        coord = Object.values(this.image.exif.GPSLongitude[i])[0]      
        longitudes.push(coord)}
      var lat = latitudes[0]
              + (latitudes[1] / 60)
              + (latitudes[2] / 3600)
      var lng = longitudes[0]
              + (longitudes[1] / 60)
              + (longitudes[2] / 3600)
      this.lat = lat
      this.lng = lng
      return (this.lat, this.lng)     
    },
    checkIfPicInRange () {
      this.start = {
        latitude: this.storeState.restLat,
        longitude: this.storeState.restLng
      }
      this.end = {
        latitude: this.lat,
        longitude: this.lng
      }        
      this.distance = haversine(this.start, this.end)
      if (this.distance < 0.2) {
        return true}
      else {return false}
    },
    checkImageLabels () {
      this.picToCheck = this.image.dataUrl.replace(/^data:image\/[a-z]+;base64,/, "");
      let axiosConfig = {
        "requests" : [{
          "features": [{
            "type": "LABEL_DETECTION"
          }],
          "image": {
            "content": this.picToCheck
          }
        }]
      }
      axios.post(`https://vision.googleapis.com/v1/images:annotate?key=${this.apiKey}`, axiosConfig)
        .then(response => {
          const labels = []
          let slicedLabelArray = response.data.responses[0].labelAnnotations.slice(0,3)
          slicedLabelArray.forEach(function(label) {
            labels.push(label.description)
          console.log(labels)
          })
        })
    },      
  }
}