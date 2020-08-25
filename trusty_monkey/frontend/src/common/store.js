export const store = {
    state: {
      pictures: [],
      totalPics: 6,
    },
    addPicture(newPicture) {      
      this.state.pictures.push(newPicture);
    },
    deletePicture(index) {
      this.state.pictures.splice(index,1);
    },
    uploadedPicture() {
      this.state.totalPics -= 1
    },
    deletedPicture() {
      this.state.totalPics += 1
    },
  }