import axios from 'axios'

const headers = {
  'Content-Type': 'application/json'
}

const userHeaders = {
  'Content-Type': 'application/json',
  'Authorization': localStorage.getItem('userTkn')
}

const userPDFHeaders = {
  'Content-Type': 'application/pdf',
  'Authorization': localStorage.getItem('userTkn'),
  'Accept': 'application/pdf'
}

const userXLSHeaders = {
  'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  'Authorization': localStorage.getItem('userTkn'),
  'Accept': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
}

const multipartsUserHeader = {
  'Content-Type': 'multipart/form-data',
  'Authorization': localStorage.getItem('userTkn')
}


const API_URL = 'http://localhost/colpryst/backend/'

const compl = ['auth/', 'location/', 'formsBuilder/', 'helpers/', 'informes/']

// Usuario
export function login (userData) {
  return axios.post(`${API_URL}${compl[0]}login.php`, userData, {
    headers: headers
  })
}
export function postUser (userData) {
  return axios.post(`${API_URL}${compl[0]}register.php`, userData, {
    headers: userHeaders
  })
}

export function postSubUsers (userData) {
  return axios.post(`${API_URL}${compl[0]}registerSubUsers.php`, userData, {
    headers: userHeaders
  })
}


export function habilitarUsuario (userData) {
  return axios.post(`${API_URL}${compl[0]}habilitarUsuario.php`, userData, {
    headers: userHeaders
  })
}

export function habilitarServicio (userData) {
  return axios.post(`${API_URL}${compl[2]}habilitarServicio.php`, userData, {
    headers: userHeaders
  })
}


export function getServicioDeshabilitados(){
  return axios.get(`${API_URL}${compl[2]}getServicioDeshabilitados.php`, {
    headers: userHeaders
  })
}

export function changePassword (userData) {
  return axios.post(`${API_URL}${compl[0]}changePassword.php`, userData, {
    headers: headers
  })
}

export function infoUser () {
  let userHeadersAct = {
    'Content-Type': 'application/json',
    'Authorization': localStorage.getItem('userTkn')
  }
  return axios.get(`${API_URL}${compl[0]}infoUser.php`, {
    headers: userHeadersAct
  })
}

export function updatePasswordWithOld(data) {
  return axios.post(`${API_URL}${compl[0]}updatePasswordWithOld.php`, data, {
    headers: userHeaders
  })
}


export function getRoles () {
  return axios.get(`${API_URL}${compl[2]}getRoles.php`, {
    headers: headers
  })
}

export function getMenu () {
  return axios.get(`${API_URL}${compl[0]}getMenu.php`, {
    headers: userHeaders
  })
}

export function getEmpresa (id) {
  return axios.get(`${API_URL}${compl[0]}getEmpresa.php?id=`+id, {
    headers: userHeaders
  })
}

export function getEstadosPeticiones () {
  return axios.get(`${API_URL}${compl[2]}getEstadosPeticiones.php`, {
    headers: headers
  })
}

export function getAllUsers () {
  return axios.get(`${API_URL}${compl[0]}getAllUsers.php`, {
    headers: userHeaders
  })
}

export function getAllUsersEmpresa (id) {
  return axios.get(`${API_URL}${compl[0]}getAllUsersEmpresa.php?id=`+id, {
    headers: userHeaders
  })
}


export function getEmpresas () {
  return axios.get(`${API_URL}${compl[0]}getEmpresas.php`, {
    headers: userHeaders
  })
}

export function updateSpecificUser (body) {
  return axios.post(`${API_URL}${compl[0]}updateSpecificUser.php`, body, {
    headers: userHeaders
  })
}

export function getSpecificUser (id) {
  return axios.get(`${API_URL}${compl[0]}getInfoSpecificUser.php?id=`+id, {
    headers: userHeaders
  })
}

export function getClientes () {
  return axios.get(`${API_URL}${compl[0]}getClientes.php`, {
    headers: userHeaders
  })
}

export function getFunProv (id="") {
  return axios.get(`${API_URL}${compl[0]}getFunProv.php?idServicio=`+id, {
    headers: userHeaders
  })
}

export function updateEncargadoSolicitud (body) {
  return axios.post(`${API_URL}${compl[2]}updateEncargadoSolicitud.php`, body, {
    headers: userHeaders
  })
}

export function updateObservacionesAnalistaProveedor (body) {
  return axios.post(`${API_URL}${compl[2]}updateObservacionesAnalistaProveedor.php`, body, {
    headers: userHeaders
  })
}
export function updateCostoAdicional (body) {
  return axios.post(`${API_URL}${compl[2]}updateCostoAdicional.php`, body, {
    headers: userHeaders
  })
}

export function updateObservacionesArchivoInd (body) {
  return axios.post(`${API_URL}${compl[2]}updateObservacionesArchivoInd.php`, body, {
    headers: userHeaders
  })
}


export function getObservacionesAnalista (id) {
  return axios.get(`${API_URL}${compl[2]}getObservacionesAnalista.php?id=` + id, {
    headers: userHeaders
  })
}

export function getCostosAdicionales (id) {
  return axios.get(`${API_URL}${compl[2]}getCostosAdicionales.php?id=` + id, {
    headers: userHeaders
  })
}

export function queryObservacionesAnalistaProveedor (id) {
  return axios.get(`${API_URL}${compl[2]}queryObservacionesAnalistaProveedor.php?id=` + id, {
    headers: userHeaders
  })
}

export function eliminarObservacion (id) {
  return axios.get(`${API_URL}${compl[2]}eliminarObservacion.php?id=` + id, {
    headers: userHeaders
  })
}

export function eliminarCostoAdicional (id) {
  return axios.get(`${API_URL}${compl[2]}eliminarCostoAdicional.php?id=` + id, {
    headers: userHeaders
  })
}

export function updateEstadoSolicitud (body) {
  return axios.post(`${API_URL}${compl[2]}updateEstadoSolicitud.php`, body, {
    headers: userHeaders
  })
}


// Departamentos y Ciudades
export function getDepartamento () {
  return axios.get(`${API_URL}${compl[1]}getDepartamento.php`, {
    headers: headers
  })
}
export function getCiudad (id) {
  return axios.get(`${API_URL}${compl[1]}getCiudad.php?id=` + id, {
    headers: headers
  })
}

// Constructor de formularios
export function getServicio () {
  return axios.get(`${API_URL}${compl[2]}getServicio.php`, {
    headers: headers
  })
}

export function getServicioSpecificUser (idEmpresa) {
  return axios.get(`${API_URL}${compl[2]}getServicioSpecificUser.php?id=`+idEmpresa, {
    headers: headers
  })
}

export function getSubServicioSpecificUser (idServicio, idEmpresa) {
  return axios.get(`${API_URL}${compl[2]}getSubServicioSpecificUser.php?idServicio=`+idServicio+`&idUser=`+idEmpresa, {
    headers: headers
  })
}

export function getSubServicio (id) {
  return axios.get(`${API_URL}${compl[2]}getSubServicio.php?id=` + id, {
    headers: headers
  })
}

export function getAllSubServicio () {
  return axios.get(`${API_URL}${compl[2]}getAllSubServicio.php`, {
    headers: headers
  })
}


export function getSubServicioByName (id) {
  return axios.get(`${API_URL}${compl[2]}getSubServicioByName.php?id=` + id, {
    headers: headers
  })
}

export function getSubServicioByNameSpecificUser (id, idUser) {
  return axios.get(`${API_URL}${compl[2]}getSubServicioByNameSpecificUser.php?idServicio=` + id + `&idUser=`+idUser, {
    headers: headers
  })
}


export function getServicioEspecifico (id) {
  return axios.get(`${API_URL}${compl[2]}getServicioEspecifico.php?id=` + id, {
    headers: headers
  })
}

export function getServicioEspecificoEspecifico (id) {
  return axios.get(`${API_URL}${compl[2]}getServicioEspecificoEspecifico.php?id=` + id, {
    headers: headers
  })
}

export function getDocumento () {
  return axios.get(`${API_URL}${compl[2]}getDocumentos.php`, {
    headers: headers
  })
}

//Envío Formularios
export function newForm (data) {
  return axios.post(`${API_URL}${compl[2]}newForm.php`, data, {
    headers: multipartsUserHeader
  })
}

export function getPeticiones () {
  return axios.get(`${API_URL}${compl[2]}getForms.php`, {
    headers: userHeaders
  })
}

export function getPeticion (id) {
  return axios.get(`${API_URL}${compl[2]}getForm.php?id=` +  id, {
    headers: userHeaders
  })
}

export function getArchivos (id) {
  return axios.get(`${API_URL}${compl[2]}getArchivos.php?id=` +  id , {
    headers: userHeaders
  })
}
export function getArchivosIndividuales (id, descripcion) {
  return axios.get(`${API_URL}${compl[2]}getArchivosEspecificos.php?id=` +  id + `&descripcion=` + descripcion, {
    headers: userHeaders
  })
}

export function subirArchivos (data) {
  return axios.post(`${API_URL}${compl[2]}subirArchivos.php`, data, {
    headers: multipartsUserHeader
  })
}

export function eliminarArchivos (id) {
  return axios.get(`${API_URL}${compl[2]}eliminarArchivo.php?id=`+id, {
    headers: userHeaders
  })
}

export function eliminarArchivosCandidato (id) {
  return axios.get(`${API_URL}${compl[2]}eliminarArchivoCandidato.php?id=`+id, {
    headers: userHeaders
  })
}
export function eliminarArchivosEmpresa (id) {
  return axios.get(`${API_URL}${compl[2]}eliminarArchivosEmpresa.php?id=`+id, {
    headers: userHeaders
  })
}


export function getPeticionCandidato (id) {
  return axios.get(`${API_URL}${compl[2]}getFormCandidato.php?id=` +  id, {
    headers: userHeaders
  })
}

export function getArchivosCandidato (id, tipo="") {
  return axios.get(`${API_URL}${compl[2]}getArchivosCandidato.php?id=` +  id+ `&tipo=`+ encodeURIComponent(tipo), {
    headers: userHeaders
  })
}

export function subirArchivosCandidato (data) {
  return axios.post(`${API_URL}${compl[2]}subirArchivosCandidato.php`, data, {
    headers: multipartsUserHeader
  })
}

export function getArchivosEmpresa (id, tipo="") {
  return axios.get(`${API_URL}${compl[2]}getArchivosEmpresa.php?id=` +  id+ `&tipo=`+ encodeURIComponent(tipo), {
    headers: userHeaders
  })
}

export function subirArchivosEmpresa (data) {
  return axios.post(`${API_URL}${compl[2]}subirArchivosEmpresa.php`, data, {
    headers: multipartsUserHeader
  })
}

export function guardarInformeTemporal (data) {
  return axios.post(`${API_URL}${compl[2]}guardarInformeTemporal.php`, data, {
    headers: userHeaders
  })
}


export function finalizarSubirArchivosCandidato (id) {
  return axios.get(`${API_URL}${compl[2]}finalizarSubirArchivosCandidato.php?id=` +  id, {
    headers: userHeaders
  })
}

export function newServicio (data) {
  return axios.post(`${API_URL}${compl[2]}newServicio.php`, data, {
    headers: userHeaders
  })
}

export function updateServicio (data) {
  return axios.post(`${API_URL}${compl[2]}updateServicio.php`, data, {
    headers: userHeaders
  })
}

export function updateEmpresa (data) {
  return axios.post(`${API_URL}${compl[0]}updateEmpresa.php`, data, {
    headers: userHeaders
  })
}


export function newSubServicio (data) {
  return axios.post(`${API_URL}${compl[2]}newSubServicio.php`, data, {
    headers: userHeaders
  })
}

export function updateSubServicio (data) {
  return axios.post(`${API_URL}${compl[2]}updateSubServicio.php`, data, {
    headers: userHeaders
  })
}

export function getAllCandidatos () {
  return axios.get(`${API_URL}${compl[0]}getAllCandidatos.php`, {
    headers: userHeaders
  })
}

export function getAllInformes () {
  return axios.get(`${API_URL}${compl[4]}getAllInformes.php`, {
    headers: userHeaders
  })
}

export function getCoordinadores () {
  return axios.get(`${API_URL}${compl[0]}getAllCoordinadores.php`, {
    headers: userHeaders
  })
}

export function getCandidatos (id) {
  return axios.get(`${API_URL}${compl[2]}getCandidatos.php?id=` +  id, {
    headers: userHeaders
  })
}

export function downloadFile (filepath) {
  return axios.get(`${API_URL}${compl[3]}downloads.php?path=` +  filepath, {responseType: 'blob'}, {
    headers: userHeaders
  })
}

export function generarCertificadosSolicitudesFuncionario (body) {
  let settings = {
    headers: userPDFHeaders
  }
  if(body.archivo == "excel"){
    settings.responseType = 'blob'
  }
  return axios.post(`${API_URL}${compl[4]}generarCertificadosSolicitudesFuncionario.php`, body, settings)
}

export function generarInformeSolicitud (body) {
  let settings = {
    headers: userPDFHeaders
  }

  return axios.post(`${API_URL}${compl[4]}generarPDFInforme.php`, body, settings)
}

export function previewCertificadosSolicitudes (body) {
  let settings = {
    headers: userHeaders
  }
  return axios.post(`${API_URL}${compl[4]}previewCertificadosSolicitudes.php`, body, settings)
}

export function leerCargaMasivaDeSolicitudes(data) {
  return axios.post(`${API_URL}${compl[4]}leerCargaMasivaDeSolicitudes.php`, data, {
    headers: multipartsUserHeader
  })
}


