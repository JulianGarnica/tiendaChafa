
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from flask_cors import CORS
import querys
import bd

app = Flask ( __name__ )
CORS(app)
bdObject = bd.conn(app)

apiName = "/api/v1"

@app.route ( f"{apiName}/fichaMedica", methods = ['POST'] )
def crearFichaMedica():
  connection = bdObject.createConnection()
  cursor = bdObject.createCursor()
  
  cuerpoConsulta = request.get_json()
  
  nombre = cuerpoConsulta['nombre']
  apellido = cuerpoConsulta['apellido']
  edad = cuerpoConsulta['edad']
  sexo = cuerpoConsulta['sexo']
  correo = cuerpoConsulta['correo']
  telefono = cuerpoConsulta['telefono']
  sistemaSalud = cuerpoConsulta['sistemaSalud']
  medicamentos = cuerpoConsulta['medicamentos']
  alimentos = cuerpoConsulta['alimentos']
  pastillas = cuerpoConsulta['pastillas']
  otros = cuerpoConsulta['otros']
  grupoSanguineo = cuerpoConsulta['grupoSanguineo']
  observaciones = cuerpoConsulta['observaciones']
  
  data = (nombre, apellido, edad, sexo, correo, telefono, sistemaSalud, medicamentos, alimentos, pastillas, otros, grupoSanguineo, observaciones)
  cursor.execute(querys.insertFichaMedica, data)
  
  connection.commit()
  bdObject.closeConnection()

  return "Ok!"

@app.route ( f"{apiName}/actualizarFichaMedica", methods = ['POST'] )
def actualizarFichaMedica():
  connection = bdObject.createConnection()
  cursor = bdObject.createCursor()
  
  cuerpoConsulta = request.get_json()
  
  idFicha = cuerpoConsulta['id']
  nombre = cuerpoConsulta['nombre']
  apellido = cuerpoConsulta['apellido']
  edad = cuerpoConsulta['edad']
  sexo = cuerpoConsulta['sexo']
  correo = cuerpoConsulta['correo']
  telefono = cuerpoConsulta['telefono']
  sistemaSalud = cuerpoConsulta['sistemaSalud']
  medicamentos = cuerpoConsulta['medicamentos']
  alimentos = cuerpoConsulta['alimentos']
  pastillas = cuerpoConsulta['pastillas']
  otros = cuerpoConsulta['otros']
  grupoSanguineo = cuerpoConsulta['grupoSanguineo']
  observaciones = cuerpoConsulta['observaciones']
  
  data = (nombre, apellido, edad, sexo, correo, telefono, sistemaSalud, medicamentos, alimentos, pastillas, otros, grupoSanguineo, observaciones, idFicha)
  cursor.execute(querys.updateFichaMedica, data)
  
  connection.commit()
  bdObject.closeConnection()

  return "Ok!"

@app.route ( f"{apiName}/getFichaMedica", methods = ['GET'] )
def getFichasMedicas():
  connection = bdObject.createConnection()
  cursor = bdObject.createCursor()
  
  response = None
  
  if 'id' in request.args:
    idQuery = str(request.args.get("id"))
    cursor.execute(querys.getUniqueFichaMedica, (idQuery,))
    response = bdObject.returnQuery(cursor)
    
  else:
    cursor.execute(querys.getAllFichaMedica)
    response = bdObject.returnQuery(cursor)
    
  connection.commit()
  bdObject.closeConnection()
  return response

@app.route ( f"{apiName}/deleteFichaMedica", methods = ['GET'] )
def deleteFichasMedicas():
  response = "Ok!"
  try:
    connection = bdObject.createConnection()
    cursor = bdObject.createCursor()
        
    if 'id' in request.args:
      idQuery = str(request.args.get("id"))
      cursor.execute(querys.deleteUniqueFichaMedica, (idQuery,))
      
    connection.commit()
    bdObject.closeConnection()
  finally:
    return response

app.run(debug=True)