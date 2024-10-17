class Accion:
    def __init__(self, id_accion, simbolo, nombre_empresa, precio_venta, precio_compra):
        self.__id_accion = id_accion
        self.__simbolo = simbolo
        self.__nombre_empresa = nombre_empresa
        self.__precio_venta = precio_venta
        self.__precio_compra = precio_compra

    def get_id_accion(self):
        return self.__id_accion

    def get_simbolo(self):
        return self.__simbolo

    def get_nombre_empresa(self):
        return self.__nombre_empresa

    def get_precio_venta(self):
        return self.__precio_venta

    def get_precio_compra(self):
        return self.__precio_compra

