export const store = {
    state: {
      pictures: []
    },
    addPicture(newPicture) {      
      this.state.pictures.push(newPicture);
    }  
  }