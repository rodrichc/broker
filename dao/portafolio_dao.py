from models.portafolio import Portafolio

class PortafolioDAO:
    def __init__(self, db_conexion):
        self.db = db_conexion

    def crear_portafolio(self, portafolio):
        try:
            with self.db.connection.cursor() as cursor:
                sql = """INSERT INTO Portafolio (id_inversor, saldo, total_invertido, rendimiento)
                        VALUES (%s, %s, %s, %s)"""
                values = (portafolio.get_id_inversor(), portafolio.get_saldo(), portafolio.get_total_invertido(), portafolio.get_rendimiento())
                cursor.execute(sql, values)
                self.db.connection.commit()
        except Exception as e:
            print(f"Error al crear portafolio: {e}")
            self.db.connection.rollback()


    def obtener_portafolio(self, id_inversor):
        try:
            with self.db.connection.cursor() as cursor:
                sql = "SELECT * FROM Portafolio WHERE id_inversor = %s"
                cursor.execute(sql, (id_inversor,))
                portafolio = cursor.fetchone()
            if portafolio:
                return Portafolio(*portafolio)
            return None
        except Exception as e:
            print(f"Error al obtener portafolio: {e}")
            return None

    def actualizar_portafolio(self, portafolio):
        try:
            with self.db.connection.cursor() as cursor:
                sql = """UPDATE Portafolio 
                        SET saldo = %s, total_invertido = %s, rendimiento = %s 
                        WHERE id_portafolio = %s"""
                values = (portafolio.get_saldo(), portafolio.get_total_invertido(), portafolio.get_rendimiento(), portafolio.get_id_portafolio())
                cursor.execute(sql, values)
                self.db.connection.commit()
        except Exception as e:
            print(f"Error al actualizar el portafolio: {e}")
            self.db.connection.rollback()


    def obtener_activos_portafolio(self, id_portafolio):
        try:
            with self.db.connection.cursor(dictionary=True) as cursor:
                sql = """
                        SELECT a.id_accion, a.simbolo, a.nombre_empresa, pa.cantidad, a.precio_venta, a.precio_compra
                        FROM PortafolioAccion pa
                        JOIN Accion a ON pa.id_accion = a.id_accion
                        WHERE pa.id_portafolio = %s;
                        """
                cursor.execute(sql, (id_portafolio,))
                activos = cursor.fetchall()
            return activos
        except Exception as e:
            print(f"Error al obtener los activos en portafolio: {e}")
            return None
    

    def obtener_cantidad_acciones(self, id_portafolio, id_accion):
        try:
            with self.db.connection.cursor() as cursor:
                sql = "SELECT cantidad FROM PortafolioAccion WHERE id_portafolio = %s AND id_accion = %s"
                cursor.execute(sql, (id_portafolio, id_accion))
                cantidad = cursor.fetchone()
            return cantidad[0] if cantidad else 0
        except Exception as e:
            print(f"Error al obtener la cantidad de acciones: {e}")
            return None


    def obtener_portafolio_accion(self, id_portafolio, id_accion):
        try:
            with self.db.connection.cursor() as cursor:
                sql = """
                SELECT * FROM portafolioaccion
                WHERE id_portafolio = %s AND id_accion = %s
                """
                cursor.execute(sql, (id_portafolio, id_accion))
                portafolio_accion = cursor.fetchone()
            return portafolio_accion
        except Exception as e:
            print(f"Error al obtener la tabla PortafolioAccion: {e}")
            return None


    def insertar_portafolio_accion(self, id_portafolio, id_accion, cantidad):
        try:
            with self.db.connection.cursor() as cursor:
                sql = """
                INSERT INTO portafolioaccion (id_portafolio, id_accion, cantidad)
                VALUES (%s, %s, %s)
                """
                cursor.execute(sql, (id_portafolio, id_accion, cantidad))
                self.db.connection.commit()
        except Exception as e:
            print(f"Error al insertar datos en tabla PortafolioAccion: {e}")
            self.db.connection.rollback()


    def actualizar_portafolio_accion(self, id_portafolio, id_accion, nueva_cantidad):
        try:
            with self.db.connection.cursor() as cursor:
                sql = """
                UPDATE portafolioaccion
                SET cantidad = %s
                WHERE id_portafolio = %s AND id_accion = %s
                """
                cursor.execute(sql, (nueva_cantidad, id_portafolio, id_accion))
                self.db.connection.commit()
        except Exception as e:
            print(f"Error al actualizar la tabla PortafolioAccion: {e}")
            self.db.connection.rollback()
