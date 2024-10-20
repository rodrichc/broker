from database.database import ConexionBaseDeDatos
from services.auth_service import AuthService
from services.portafolio_service import PortafolioService
from services.operacion_service import OperacionService
from services.accion_service import AccionService
from utils.validacion_inversor import validar_datos

def mostrar_menu_principal():
    print("\n1. Ver datos de la cuenta")
    print("2. Listar activos del portafolio")
    print("3. Comprar acciones")
    print("4. Vender acciones")
    print("5. Cerrar sesión")

def main():
    db = ConexionBaseDeDatos()
    db.conectar()

    auth_service = AuthService(db)
    portafolio_service = PortafolioService(db)
    operacion_service = OperacionService(db)
    accion_service = AccionService(db)

    print("\n\n----BIENVENIDO A ARGBROKER----")

    while True:
        print("\n1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            datos = validar_datos()
            auth_service.registrar_inversor(*datos)
            print("\nInversor creado correctamente. Inicie sesión para operar.")

        elif opcion == "2":
            correo = input("\nCorreo: ")
            contrasenia = input("Contraseña: ")
            inversor = auth_service.iniciar_sesion(correo, contrasenia)
            
            if inversor:
                print(f"\n\n¡Bienvenido, {inversor.get_nombre()}!\n\n")
                while True:
                    mostrar_menu_principal()
                    opcion_menu = input("\nSeleccione una opción: ")
                    
                    if opcion_menu == "1":
                        datos_cuenta = portafolio_service.obtener_datos_cuenta(inversor.get_id_inversor())
                        print(f"\n\nSaldo: {datos_cuenta['saldo']}")
                        print(f"Total invertido: {datos_cuenta['total_invertido']}")
                        print(f"Valor actual: {datos_cuenta['valor_total_actual']}")
                        print(f"Rendimiento: {datos_cuenta['rendimiento_total']}")

                    elif opcion_menu == "2":
                        #FALTA EL PRECIO
                        activos = portafolio_service.listar_activos(inversor.get_id_inversor())
                        if activos:
                            for activo in activos:
                                print("\n Empresa: %s / Simbolo: %s / Cantidad: %s / Precio actual: %s / Valor total: %s / Rendimiento: %s" % 
                                    (activo['nombre_empresa'], activo['simbolo'], activo['cantidad'], activo['precio_actual'], activo['valor_total'], 
                                    activo['rendimiento']))
                        else:
                            print("\n¡Todavía no haz realizado ninguna compra de acciones!")
                    
                    elif opcion_menu == "3":
                        accion_service.armar_listado_acciones()
                        id_accion = int(input("\nID de la acción a comprar: "))
                        cantidad = int(input("Cantidad de acciones: "))
                        try:
                            operacion_service.realizar_compra(inversor.get_id_inversor(), id_accion, cantidad)
                            print("\n¡Compra realizada con éxito!\n")
                        except ValueError as e:
                            print(f"\nError: {str(e)}")
                    
                    elif opcion_menu == "4":
                        activos = portafolio_service.listar_activos(inversor.get_id_inversor())
                        if activos: 
                            for activo in activos:
                                #Lista las acciones
                                print("\n ID Accion: %s / Empresa: %s / Simbolo: %s / Cantidad: %s / Precio actual: %s" % 
                                    (activo['id_accion'], activo['nombre_empresa'], activo['simbolo'], activo['cantidad'], activo['precio_actual']))
                            #Inputs para elegir que comprar y cuanto
                            id_accion = int(input("\nID de la acción a vender: "))
                            cantidad = int(input("Cantidad de acciones: "))
                            try:
                                operacion_service.realizar_venta(inversor.get_id_inversor(), id_accion, cantidad)
                                print("\n¡Venta realizada con éxito!")
                            except ValueError as e:
                                print(f"\nError: {str(e)}")
                                # pass
                        else: 
                            print("\n¡Todavía no haz realizado ninguna compra de acciones!")

                        
                    
                    elif opcion_menu == "5":
                        break
            else:
                print("\n¡El correo o contraseña incorrectos!.")

        elif opcion == "3":
            break

    db.desconectar()

if __name__ == "__main__":
    main()