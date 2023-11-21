
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from flask_cors import CORS
import querys
import bd
import json

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
  descripcion = cuerpoConsulta['descripcion']
  costo = cuerpoConsulta['costo']
  cantidad = cuerpoConsulta['cantidad']
  
  data = (nombre, descripcion, costo, cantidad)
  cursor.execute(querys.insertFichaMedica, data)
  
  connection.commit()
  bdObject.closeConnection()

  return "Ok!"

@app.route ( f"{apiName}/actualizarFichaMedica", methods = ['POST'] )
def actualizarFichaMedica():
  connection = bdObject.createConnection()
  cursor = bdObject.createCursor()
  
  cuerpoConsulta = request.get_json()
  
  idFicha = str(cuerpoConsulta['id'])
  nombre = cuerpoConsulta['nombre']
  descripcion = cuerpoConsulta['descripcion']
  costo = cuerpoConsulta['costo']
  cantidad = cuerpoConsulta['cantidad']
  
  data = (nombre, descripcion, costo, cantidad, idFicha)
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
      idQuery = int(request.args.get("id"))
      cursor.execute(querys.deleteUniqueFichaMedica, (idQuery,))
      
    connection.commit()
    bdObject.closeConnection()
  finally:
    return response
  
#  Auth EndPoints

@app.route ( f"{apiName}/register", methods = ['POST'] )
def registerUser():
  connection = bdObject.createConnection()
  cursor = bdObject.createCursor()
  
  cuerpoConsulta = request.get_json()
  
  nombre = cuerpoConsulta['nombre']
  correo = cuerpoConsulta['correo']
  password = cuerpoConsulta['password']
  
  data = (nombre, correo, password)
  cursor.execute(querys.insertUser, data)
  
  connection.commit()
  bdObject.closeConnection()

  return "Ok!"  

@app.route ( f"{apiName}/getUsuarios", methods = ['GET'] )
def getUsuarios():
  connection = bdObject.createConnection()
  cursor = bdObject.createCursor()
  
  response = None
  
  if 'id' in request.args:
    idQuery = str(request.args.get("id"))
    cursor.execute(querys.getUniqueUser, (idQuery,))
    response = bdObject.returnQuery(cursor)
    
  else:
    cursor.execute(querys.getAllUsers)
    response = bdObject.returnQuery(cursor)
    
  connection.commit()
  bdObject.closeConnection()
  return response

@app.route ( f"{apiName}/updateUser", methods = ['POST'] )
def updateUser():
  connection = bdObject.createConnection()
  cursor = bdObject.createCursor()
  
  cuerpoConsulta = request.get_json()
  
  idFicha = str(cuerpoConsulta['id'])
  nombre = cuerpoConsulta['nombre']
  correo = cuerpoConsulta['correo']
  
  data = (nombre, correo, idFicha)
  cursor.execute(querys.updateUser, data)
  
  connection.commit()
  bdObject.closeConnection()

  return "Ok!"


@app.route ( f"{apiName}/deleteUsuario", methods = ['GET'] )
def deleteUsuario():
  response = "Ok!"
  try:
    connection = bdObject.createConnection()
    cursor = bdObject.createCursor()
        
    if 'id' in request.args:
      idQuery = str(request.args.get("id"))
      cursor.execute(querys.deleteUsuario, (idQuery,))
      
    connection.commit()
    bdObject.closeConnection()
  finally:
    return response

@app.route ( f"{apiName}/login", methods = ['POST'] )
def login():
  connection = bdObject.createConnection()
  cursor = bdObject.createCursor()
  
  cuerpoConsulta = request.get_json()
  
  correo = cuerpoConsulta['user']
  password = cuerpoConsulta['password']
  
  data = (correo, password)
  cursor.execute(querys.getLogin, data)
  response = bdObject.returnQuery(cursor)
  
  
  connection.commit()
  bdObject.closeConnection()

  return response

app.run(debug=True)