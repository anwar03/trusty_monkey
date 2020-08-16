import { CSRF_TOKEN } from "./csrf_token.js"

function handleResponse(response) {
  if (response.status === 204) {
    throw new Error("No data")
  } else if (response.status === 404) {
    throw new Error("Wrong URL")
  } else if (response.status === 400) {
    throw new Error("Restaurant allready added!")    
  } else {
    return response.json();    
  }
}


function apiService(endpoint, method, data) {
  const config = {
    method: method || "GET",
    body:data,
    // body: data !== undefined ? JSON.stringify(data) : null,
    headers: {
      // 'content-type': 'application/json',
      // 'content-type': 'multipart/form-data',
      // 'X-CSRFTOKEN': CSRF_TOKEN
      Accept: 'application/json',
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods':
      'GET, POST, PATCH, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers':
      'Origin, Content-Type, X-Auth-Token',
      'X-CSRFTOKEN': CSRF_TOKEN
    }
  };
  return fetch(endpoint, config)
          .then(handleResponse)
          .catch(error => console.log(error))
}

export { apiService };