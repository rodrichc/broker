from dao.operacion_dao import OperacionDAO
from dao.portafolio_dao import PortafolioDAO
from dao.accion_dao import AccionDAO
from datetime import date

class OperacionService:
    def __init__(self, db_conexion):
        self.operacion_dao = OperacionDAO(db_conexion)
        self.portafolio_dao = PortafolioDAO(db_conexion)
        self.accion_dao = AccionDAO(db_conexion)


    def realizar_compra(self, id_inversor, id_accion, cantidad):
        portafolio = self.portafolio_dao.obtener_portafolio(id_inversor)
        accion = self.accion_dao.obtener_accion(id_accion)
        
        costo_total = accion.get_precio_compra() * cantidad
        comision = costo_total * 0.015  #comision del 1.5%
        costo_total_con_comision = costo_total + comision

        if portafolio.get_saldo() < costo_total_con_comision:
            raise ValueError("Saldo insuficiente para realizar la compra")

    #se puede mejorar el codigo dividiendo lo de aca para abajo
        # Registro de la operación
        self.operacion_dao.registrar_operacion(
            portafolio.get_id_portafolio(), 1, id_accion, date.today(),
            accion.get_precio_compra(), cantidad, costo_total, comision
        )
        # Se actualiza la cantidad de accion en el portafolio
        self.actualizar_cantidad_acciones(portafolio.get_id_portafolio(), id_accion, cantidad)

        # Se actualiza el portafolio
        nuevo_saldo = portafolio.get_saldo() - costo_total_con_comision
        portafolio.set_saldo(nuevo_saldo)

        nuevo_total_invertido = portafolio.get_total_invertido() + costo_total
        portafolio.set_total_invertido(nuevo_total_invertido)

        self.portafolio_dao.actualizar_portafolio(portafolio)


    def realizar_venta(self, id_inversor, id_accion, cantidad):
        portafolio = self.portafolio_dao.obtener_portafolio(id_inversor)
        accion = self.accion_dao.obtener_accion(id_accion)
        
        # Se Verifica si el inversor tiene suficientes acciones para vender
        acciones_en_portafolio = self.portafolio_dao.obtener_cantidad_acciones(portafolio.get_id_portafolio(), id_accion)
        if acciones_en_portafolio < cantidad:
            raise ValueError("No tienes suficientes acciones para realizar esta venta")

        valor_venta = accion.get_precio_venta() * cantidad
        comision = valor_venta * 0.015  # comisión del 1.5%
        valor_venta_neto = valor_venta - comision

        # Registrar la operación
        self.operacion_dao.registrar_operacion(
            portafolio.get_id_portafolio(), 2, id_accion, date.today(),
            accion.get_precio_venta(), cantidad, valor_venta, comision
        )

        # Actualizar la cantidad de acciones en el portafolio
        self.actualizar_cantidad_acciones(portafolio.get_id_portafolio(), id_accion, -cantidad)

        # Actualizar el portafolio
        nuevo_saldo = portafolio.get_saldo() + valor_venta_neto
        portafolio.set_saldo(nuevo_saldo)
        
            # Calcular el nuevo total invertido
        costo_promedio = self.calcular_costo_promedio(portafolio.get_id_portafolio(), id_accion)
        nuevo_total_invertido = portafolio.get_total_invertido() - (costo_promedio * cantidad)
        portafolio.set_total_invertido(nuevo_total_invertido)

        self.portafolio_dao.actualizar_portafolio(portafolio)


    def actualizar_cantidad_acciones(self, id_portafolio, id_accion, cantidad):
        portafolio_accion = self.portafolio_dao.obtener_portafolio_accion(id_portafolio, id_accion)
        
        if portafolio_accion:
            # Actualizar la cantidad de acciones si ya existe
            nueva_cantidad = int(portafolio_accion[-1]) + cantidad
            self.portafolio_dao.actualizar_portafolio_accion(id_portafolio, id_accion, nueva_cantidad)
        else:
            # Insertar una nueva entrada si no tiene la acción
            self.portafolio_dao.insertar_portafolio_accion(id_portafolio, id_accion, cantidad)


    def calcular_costo_promedio(self, id_portafolio, id_accion):
        operaciones = self.operacion_dao.obtener_operaciones_accion(id_portafolio, id_accion)

        total_costo = sum(op['precio'] * op['cantidad'] for op in operaciones if op['id_tipo'] == 1)
        total_cantidad = sum(op['cantidad'] for op in operaciones if op['id_tipo'] == 1)

        return total_costo / total_cantidad if total_cantidad > 0 else 0