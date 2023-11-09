import config
from flask import jsonify
from flask_mysqldb import MySQL, MySQLdb

class conn():

    def __init__(self, app):

        self.HOST = config.MYSQL_HOST
        self.USERNAME = config.MYSQL_USER
        self.PASSWORD = config.MYSQL_PASSWORD
        self.BD_NAME = config.MYSQL_DB
        self.PORT = config.MYSQL_PORT
        self.mysql = MySQL(app)

    def createConnection(self):
        self.conn = MySQLdb.connect(host=self.HOST,
                                    user=self.USERNAME,
                                    passwd=self.PASSWORD,
                                    db=self.BD_NAME,
                                    port=self.PORT)
        return self.conn

    def createCursor(self):
        return self.conn.cursor()
    
    def returnQuery(self, cursor):
        row_headers=[x[0] for x in cursor.description]
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
                json_data.append(dict(zip(row_headers,result)))
        return jsonify(json_data)
        

    def closeConnection(self):
        self.conn.close()
