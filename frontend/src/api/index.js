import axios from 'axios'

const headers = {
  'Content-Type': 'application/json'
}


const API_URL = 'http://localhost:5000/api/v1'

const compl = ['/']


export function getFichasMedicas () {
  return axios.get(`${API_URL}${compl[0]}getFichaMedica`, {
    headers: headers
  })
}

export function getFichaMedica (id) {
  return axios.get(`${API_URL}${compl[0]}getFichaMedica?id=${id}`, {
    headers: headers
  })
}

export function deleteFichaMedica (id) {
  return axios.get(`${API_URL}${compl[0]}deleteFichaMedica?id=${id}`, {
    headers: headers
  })
}

export function insertFichaMedica (body) {
  return axios.post(`${API_URL}${compl[0]}fichaMedica`, body, {
    headers: headers
  })
}

export function updateFichaMedica (body) {
  return axios.post(`${API_URL}${compl[0]}actualizarFichaMedica`, body, {
    headers: headers
  })
}
