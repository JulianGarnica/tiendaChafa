import config
from flask_mysqldb import MySQL, MySQLdb

class conn():

    def __init__(self):

        self.HOST = config.MYSQL_HOST
        self.USERNAME = config.MYSQL_USER
        self.PASSWORD = config.MYSQL_PASSWORD
        self.BD_NAME = config.MYSQL_DB
        self.PORT = config.MYSQL_PORT
        print(self.USERNAME)

    def createConnection(self):
        self.conn = MySQLdb.connect(host=self.HOST,
                                    user=self.USERNAME,
                                    passwd=self.PASSWORD,
                                    db=self.BD_NAME,
                                    port=self.PORT)
        self.cursor = self.conn.cursor()

    def getCursor(self):
        return self.cursor

    def closeConnection(self):
        self.conn.close()
