from dao.inversor_dao import InversorDAO
from models.inversor import Inversor
from dao.portafolio_dao import PortafolioDAO
from models.portafolio import Portafolio

class AuthService:
    def __init__(self, db_conexion):
        self.inversor_dao = InversorDAO(db_conexion)
        self.portafolio_dao = PortafolioDAO(db_conexion)

    def registrar_inversor(self, nombre, apellido, cuil, correo, contrasenia):
        nuevo_inversor = Inversor(None, nombre, apellido, cuil, correo, contrasenia)
        id_inversor = self.inversor_dao.crear_inversor(nuevo_inversor)
    # Creación del portafolio para el nuevo inversor.
        nuevo_portafolio = Portafolio(id_portafolio=None, id_inversor=id_inversor, saldo=1000000.0, total_invertido=0, rendimiento=0)
        self.portafolio_dao.crear_portafolio(nuevo_portafolio)
        

    def iniciar_sesion(self, correo, contrasenia):
            inversor = self.inversor_dao.obtener_inversor_por_correo_y_contrasenia(correo, contrasenia)
            return inversor
