import mysql.connector

class ConexionBaseDeDatos:
    def __init__(self):
        self.conexion = None

    def conectar(self):
        self.connection = mysql.connector.connect(
            host='bi201yksz8ubhfjv7dyb-mysql.services.clever-cloud.com',
            user='uihujxs4xmhkdvi3',
            password='tp5pvzvCEPOye6QVmYAQ',
            database='bi201yksz8ubhfjv7dyb',
            port='3306'
        )

    def desconectar(self):
        if self.connection:
            self.connection.close()
