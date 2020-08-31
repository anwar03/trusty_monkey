import haversine from "haversine"

export default {
  data() {
    return {      
      lat: null,
      lng: null,      
    }
  },  
  methods: {
    calculateCoordPicture: function() {     
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
    checkIfPicInRange: function() {
      this.start = {
        latitude: 30.849635,
        longitude: -83.24559
      }
      this.end = {
        latitude: 27.950575,
        longitude: -82.457178
      }        
      console.log(haversine(this.start, this.end))
      console.log("toto rigolos")
    }
  }
}
