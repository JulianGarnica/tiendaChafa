###Querys to mySQL

insertFichaMedica = "INSERT INTO fichamedica(nombre, apellido, edad, sexo, correo, telefono, sistemaSalud, medicamentos, alimentos, pastillas, otros, grupoSanguineo, observaciones) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
updateFichaMedica = "UPDATE fichamedica SET nombre=%s, apellido=%s, edad=%s, sexo=%s, correo=%s, telefono=%s, sistemaSalud=%s, medicamentos=%s, alimentos=%s, pastillas=%s, otros=%s, grupoSanguineo=%s, observaciones=%s WHERE id=%s"
getAllFichaMedica = "SELECT id, nombre, apellido, correo, sexo FROM fichamedica"
getUniqueFichaMedica = "SELECT * FROM fichamedica WHERE id=%s"
deleteUniqueFichaMedica = "DELETE FROM fichamedica WHERE id=%s"


insertUser = "INSERT INTO usuarios(nombre, correo, password) VALUES (%s, %s, %s)"
getUniqueUser = "SELECT id, nombre, correo, createdOn FROM usuarios WHERE id=%s"
updateUser = "UPDATE usuarios SET nombre=%s, correo=%s WHERE id=%s"
getAllUsers = "SELECT id, nombre, correo, createdOn AS creadoEl FROM usuarios"
deleteUsuario = "DELETE FROM usuarios WHERE id=%s"

getLogin = "SELECT COUNT(id) AS cantidad FROM usuarios WHERE correo=%s AND password=%s"