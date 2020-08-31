export const store = {
    state: {
      pictures: [],
      restLat: null,
      restLng: null,
    },
    addPicture(newPicture) {      
      this.state.pictures.push(newPicture);
    },
    deletePicture(index) {
      this.state.pictures.splice(index,1);
    },
    setRestLat(lat) {
      this.state.restLat = lat
    },
    setRestLng(lng) {
      this.state.restLng = lng
    }
  }