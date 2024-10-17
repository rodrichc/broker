from dao.accion_dao import AccionDAO

class AccionService:
    def __init__(self, db_connection):
        self.accion_dao = AccionDAO(db_connection)

    def armar_listado_acciones(self):
        lista_acciones = self.accion_dao.listar_acciones()
        for accion in lista_acciones:
            print(f"ID: {accion[0]} / Simbolo: {accion[1]} / Empresa: {accion[2]} / Precio de compra: {accion[4]}")
        