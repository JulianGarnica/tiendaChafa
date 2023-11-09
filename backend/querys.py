###Querys to mySQL

insertFichaMedica = "INSERT INTO fichamedica(nombre, apellido, edad, sexo, correo, telefono, sistemaSalud, medicamentos, alimentos, pastillas, otros, grupoSanguineo, observaciones) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
updateFichaMedica = "UPDATE fichamedica SET nombre=%s, apellido=%s, edad=%s, sexo=%s, correo=%s, telefono=%s, sistemaSalud=%s, medicamentos=%s, alimentos=%s, pastillas=%s, otros=%s, grupoSanguineo=%s, observaciones=%s WHERE id=%s"
getAllFichaMedica = "SELECT id, nombre, apellido, correo, sexo FROM fichamedica"
getUniqueFichaMedica = "SELECT * FROM fichamedica WHERE id=%s"
deleteUniqueFichaMedica = "DELETE FROM fichamedica WHERE id=%s"