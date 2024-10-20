class Inversor:
    def __init__(self, id_inversor, nombre, apellido, cuil, correo, contrasenia):
        self.__id_inversor = id_inversor
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cuil = cuil
        self.__correo = correo
        self.__contrasenia = contrasenia

    def get_id_inversor(self):
        return self.__id_inversor
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_cuil(self):
        return self.__cuil
    
    def get_correo(self):
        return self.__correo
    
    def get_contrasenia(self):
        return self.__contrasenia