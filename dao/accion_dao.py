from models.accion import Accion

class AccionDAO:
    def __init__(self, db_connection):
        self.db = db_connection

    def obtener_accion(self, id_accion):
        cursor = self.db.connection.cursor()
        sql = "SELECT * FROM Accion WHERE id_accion = %s"
        cursor.execute(sql, (id_accion,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return Accion(*result)
        return None

    def listar_acciones(self):
        cursor = self.db.connection.cursor()
        sql = "SELECT * FROM Accion"
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        return results

    def actualizar_precios(self, id_accion, precio_venta, precio_compra):
        cursor = self.db.connection.cursor()
        sql = """UPDATE Accion 
                 SET precio_venta = %s, precio_compra = %s 
                 WHERE id_accion = %s"""
        cursor.execute(sql, (precio_venta, precio_compra, id_accion))
        self.db.connection.commit()
        cursor.close()