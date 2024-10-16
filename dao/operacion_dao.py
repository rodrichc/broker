class OperacionDAO:
    def __init__(self, db_connection):
        self.db = db_connection

    def obtener_cantidad_acciones(self, id_portafolio, id_accion):
        cursor = self.db.connection.cursor()
        sql = "SELECT cantidad FROM PortafolioAccion WHERE id_portafolio = %s AND id_accion = %s"
        cursor.execute(sql, (id_portafolio, id_accion))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0

    def registrar_operacion(self, id_portafolio, id_tipo, id_accion, fecha_operacion, precio, cantidad, total_accion, comision):
        cursor = self.db.connection.cursor()
        sql = """INSERT INTO Operacion (id_portafolio, id_tipo, id_accion, fecha_operacion, precio, cantidad, total_accion, comision)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (id_portafolio, id_tipo, id_accion, fecha_operacion, precio, cantidad, total_accion, comision)
        cursor.execute(sql, values)
        self.db.connection.commit()
        cursor.close()

    def obtener_operaciones_accion(self, id_portafolio, id_accion):
        cursor = self.db.connection.cursor(dictionary=True)
        sql = """
        SELECT *
        FROM Operacion
        WHERE id_portafolio = %s AND id_accion = %s
        ORDER BY fecha_operacion
        """
        cursor.execute(sql, (id_portafolio, id_accion))
        operaciones = cursor.fetchall()
        cursor.close()
        return [
            {**op, 'tipo': 'compra' if op['id_tipo'] == 1 else 'venta'}
            for op in operaciones
        ]   