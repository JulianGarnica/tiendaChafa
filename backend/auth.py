import sys
import os
import jwt
import datetime

from datetime import date, timedelta
from functools import wraps
from ..functions import  cod_random, encript_passw
from werkzeug.security import check_password_hash
from flask import jsonify, request, abort, current_app

class Auth():

  def __init__(self, app):
    self.appVar = app
      
  # The actual decorator function
  def methods(self):
    app = self.appVar

    def require_appkey(view_function):
      @wraps(view_function)
      # the new, post-decoration function. Note *args and **kwargs here.
      def decorated_function(*args, **kwargs):
        with open(self.apiKey, 'r') as apikey:
          key = apikey.read().replace('\n', '')
        # if request.args.get('key') and request.args.get('key') == key:
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') == key:
          return view_function(*args, **kwargs)
        else:
          abort(401)
      return decorated_function

    ## Registro de usuarios ##


    @app.route('/auth/v0.1/register/', methods=['POST'])
    @require_appkey
    def register():
        try:
            try:
                new_user = {
                    "tipo_doc": request.json['tipo_doc'],
                    "documento": str(request.json['documento']),
                    "nombre": request.json['nombre'],
                    "username": request.json['username'],
                    "correo": request.json['correo'],
                    "password": str(request.json['password']),
                    "telefono": str(request.json['telefono']),
                    "rol": str(request.json['rol']),
                    "ult_con": str(datetime.datetime.utcnow())
                }
            except:
              return jsonify({'result': "Invalid data"}), 406

            if not new_user['correo'] or not new_user['password'] or not new_user['nombre']:
                return jsonify({'result': "Not enough data"}), 406
            else:

                if "@" in new_user['correo']:
                    id_empresa = cod_random(5)
                    # Validar correo:
                    result_email = self.connection.query('SELECT * FROM tb_usuarios WHERE correo = "' + new_user['correo'] + '"')
                                        
                    if(result_email == []):
                        result_documento = self.connection.query('SELECT * FROM tb_usuarios WHERE documento = "' + new_user['documento'] + '"')
                        
                        if(result_documento == []):
                            # Validar username
                            result_username = self.connection.query('SELECT * FROM tb_usuarios WHERE username = "' + new_user['username'] + '"')
                            
                            if(result_username == []):

                                password = encript_passw(new_user['password'])

                                columns = ("id_empresa", "tipo_doc", "documento", "nombre", "username", "correo", "password", "rol", "telefono", "ult_con")
                                val = (id_empresa, new_user['tipo_doc'], new_user['documento'], new_user['nombre'], new_user['username'], new_user['correo'], password, new_user['rol'], new_user['telefono'], new_user['ult_con'])
                                self.connection.insert("tb_usuarios", columns, val)

                                basedir = str(app.config['UPLOAD_FOLDER'])+str('/clients/')+str(id_empresa)
                                if(os.path.isdir(basedir)):
                                    pass
                                else: os.mkdir(basedir)
                                
                                self.connectionDBgtPool.create_databases(basedir, id_empresa, "bd_gtpool")
                                """
                                
                                columns = ("id_empresa")
                                val = (id_empresa)
                                self.connection.insert("tb_empresas", columns, val)

                                """
                                return jsonify({'result': 'Added successfully', 'id_medica': id_empresa}), 201
                            else:
                                return jsonify({'result': "Username already registered"}), 406
                        else:
                            return jsonify({'result': "Document already registered"}), 406
                    else:
                        return jsonify({'result': "Email already registered"}), 406

                else:
                    return jsonify({'result': "Email verification error"}), 406
        except:
            return jsonify({'result': "Error adding user", 'error': sys.exc_info()[0]}), 405
        externo.close()

      ## Login de Usuarios ##

    @app.route('/auth/v0.1/login/', methods=['POST'])
    @require_appkey
    def login():
      try:
        user = {
          "correo": request.json['correo'],
          "password": request.json['password'],
        }

        if not user['correo'] or not user['password']:
          return jsonify({'result': "Datos sin completar"}), 406
        else:

          result =self.connection.query('SELECT documento, nombre, correo, username, password, rol FROM tb_usuarios WHERE correo="' + user['correo'] + '"')
          if(result == []):
            return jsonify({'result': 'Correo electrónico o código de empresa no válido'}), 405

          else:
            password_bd = result[0]['password']
            if(check_password_hash(password_bd, user['password'])):
              token = jwt.encode({
                'sub': user['correo'],
                'name': result[0]['nombre'],
                'username': result[0]['username'],
                'documento': str(result[0]['documento']),
                'rol': result[0]['rol'],
                'iat': datetime.datetime.utcnow(),
                'exp': datetime.datetime.utcnow() + timedelta(minutes=400)},
                # 'exp': 1478773621},
                current_app.config['SECRET_KEY']
              )
              return jsonify({'token': token}), 201
            else:
              return jsonify({'result': 'Contraseña errónea'}), 405

      except:
        return jsonify({'result': 'none', 'error': sys.exc_info()[0]}), 405
      
    @app.route('/auth/v0.1/updateUser/', methods=['POST'])
    @require_appkey
    def updateUser():
      id_empresa = request.json['id_empresa']
      basedir = str(app.config['UPLOAD_FOLDER'])+str('/clients/')+str(id_empresa)
      if(os.path.isdir(basedir)):
          pass
      else: os.mkdir(basedir)
      response = self.connectionDBgtPool.create_databases(basedir, id_empresa, "bd_gtpool")
      return jsonify({'result': response})
      