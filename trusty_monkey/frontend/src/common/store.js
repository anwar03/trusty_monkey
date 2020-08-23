export const store = {
    state: {
      pictures: []
    },
    addPicture(newPicture) {      
      this.state.pictures.push(newPicture);
    },
    deletePicture(index) {
      this.state.pictures.splice(index,1);
    },  
  }