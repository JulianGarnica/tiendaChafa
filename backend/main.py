
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import bd

app = Flask ( __name__ )
connection = bd.conn()
 
mysql = MySQL(app)

@app.route ( "/crearFichaMedica", methods = ['POST'] )
def crearFichaMedica():
  cursor = connection.createConnection()
  cuerpoConsulta = request.get_json()

  print(cuerpoConsulta['test'])
  return cuerpoConsulta['test']

app.run(debug=True)