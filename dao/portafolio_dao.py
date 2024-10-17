from models.portafolio import Portafolio

class PortafolioDAO:
    def __init__(self, db_connection):
        self.db = db_connection

    def crear_portafolio(self, portafolio):
        cursor = self.db.connection.cursor()
        sql = """INSERT INTO Portafolio (id_inversor, saldo, total_invertido, rendimiento)
                 VALUES (%s, %s, %s, %s)"""
        values = (portafolio.get_id_inversor(), portafolio.get_saldo(), portafolio.get_total_invertido(), portafolio.get_rendimiento())
        cursor.execute(sql, values)
        self.db.connection.commit()
        cursor.close()

    def obtener_portafolio(self, id_inversor):
        cursor = self.db.connection.cursor()
        sql = "SELECT * FROM Portafolio WHERE id_inversor = %s"
        cursor.execute(sql, (id_inversor,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return Portafolio(*result)
        return None

    def actualizar_portafolio(self, portafolio):
        cursor = self.db.connection.cursor()
        sql = """UPDATE Portafolio 
                 SET saldo = %s, total_invertido = %s, rendimiento = %s 
                 WHERE id_portafolio = %s"""
        values = (portafolio.get_saldo(), portafolio.get_total_invertido(), portafolio.get_rendimiento(), portafolio.get_id_portafolio())
        cursor.execute(sql, values)
        self.db.connection.commit()
        cursor.close()


    def obtener_activos_portafolio(self, id_portafolio):
        cursor = self.db.connection.cursor(dictionary=True)
        sql = """
                SELECT a.id_accion, a.simbolo, a.nombre_empresa, pa.cantidad, a.precio_venta, a.precio_compra
                FROM PortafolioAccion pa
                JOIN Accion a ON pa.id_accion = a.id_accion
                WHERE pa.id_portafolio = %s;
                """
        cursor.execute(sql, (id_portafolio,))
        activos = cursor.fetchall()
        cursor.close()
        return activos
    
    def obtener_cantidad_acciones(self, id_portafolio, id_accion):
        cursor = self.db.connection.cursor()
        sql = "SELECT cantidad FROM PortafolioAccion WHERE id_portafolio = %s AND id_accion = %s"
        cursor.execute(sql, (id_portafolio, id_accion))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0


    def obtener_portafolio_accion(self, id_portafolio, id_accion):
        cursor = self.db.connection.cursor()
        sql = """
        SELECT * FROM portafolioaccion
        WHERE id_portafolio = %s AND id_accion = %s
        """
        cursor.execute(sql, (id_portafolio, id_accion))
        portafolio_accion = cursor.fetchone()
        cursor.close()
        return portafolio_accion

    def insertar_portafolio_accion(self, id_portafolio, id_accion, cantidad):
        cursor = self.db.connection.cursor()
        sql = """
        INSERT INTO portafolioaccion (id_portafolio, id_accion, cantidad)
        VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (id_portafolio, id_accion, cantidad))
        self.db.connection.commit()
        cursor.close()

    def actualizar_portafolio_accion(self, id_portafolio, id_accion, nueva_cantidad):
        cursor = self.db.connection.cursor()
        sql = """
        UPDATE portafolioaccion
        SET cantidad = %s
        WHERE id_portafolio = %s AND id_accion = %s
        """
        cursor.execute(sql, (nueva_cantidad, id_portafolio, id_accion))
        self.db.connection.commit()
        cursor.close()