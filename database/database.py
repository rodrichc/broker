import mysql.connector

class ConexionBaseDeDatos:
    def __init__(self):
        self.conexion = None

    def conectar(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345',
            database='argbroker',
            port='3306'
        )

    def desconectar(self):
        if self.connection:
            self.connection.close()
