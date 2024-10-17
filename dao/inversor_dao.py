from models.inversor import Inversor

class InversorDAO:
    def __init__(self, db_connection):
        self.db = db_connection

    def crear_inversor(self, inversor):
        cursor = self.db.connection.cursor()
        sql = """INSERT INTO Inversor (nombre, apellido, cuil, correo, contraseña)
                 VALUES (%s, %s, %s, %s, %s)"""
        values = (inversor.get_nombre(), inversor.get_apellido(), inversor.get_cuil(), inversor.get_correo(), inversor.get_contraseña())
        cursor.execute(sql, values)
        id_inversor = cursor.lastrowid
        self.db.connection.commit()
        cursor.close()
        return id_inversor

    def obtener_inversor_por_correo_y_contraseña(self, correo, contraseña):
        cursor = self.db.connection.cursor()
        sql = "SELECT * FROM Inversor WHERE correo = %s and contraseña = %s"
        cursor.execute(sql, (correo, contraseña))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return Inversor(*result)
        return None
