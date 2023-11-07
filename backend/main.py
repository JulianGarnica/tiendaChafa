
from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask ( __name__ )
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)

@app.route ( "/crearFichaMedica", methods = ['POST'] )
def crearFichaMedica():
  cuerpoConsulta = request.get_json()
  print(cuerpoConsulta['test'])
  return cuerpoConsulta['test']

app.run(debug=True)