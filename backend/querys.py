###Querys to mySQL

insertFichaMedica = "INSERT INTO productos(nombre, descripcion, costo, cantidad) VALUES (%s,%s,%s,%s)"
updateFichaMedica = "UPDATE productos SET nombre=%s, descripcion=%s, costo=%s, cantidad=%s WHERE id=%s"
getAllFichaMedica = "SELECT * FROM productos"
getUniqueFichaMedica = "SELECT * FROM productos WHERE id=%s"
deleteUniqueFichaMedica = "DELETE FROM productos WHERE id=%s"


insertUser = "INSERT INTO usuarios(nombre, correo, password) VALUES (%s, %s, %s)"
getUniqueUser = "SELECT id, nombre, correo, createdOn FROM usuarios WHERE id=%s"
updateUser = "UPDATE usuarios SET nombre=%s, correo=%s WHERE id=%s"
getAllUsers = "SELECT id, nombre, correo, createdOn AS creadoEl FROM usuarios"
deleteUsuario = "DELETE FROM usuarios WHERE id=%s"

getLogin = "SELECT COUNT(id) AS cantidad FROM usuarios WHERE correo=%s AND password=%s"