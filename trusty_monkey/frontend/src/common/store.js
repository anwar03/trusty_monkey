export const store = {
    state: {      
      pictures: [],
      labels: [],
      restLat: null,
      restLng: null,
      file: null,
      submit: false,
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
    },
    setFile(file) {
      this.state.file = file
    },
    setSubmit() {
      this.state.submit = !this.state.submit
    },
    addLabels(label) {
      this.state.labels.push(label)
    }   
  }