import re

def validar_nombre(nombre):
    if len(nombre) > 30:
        return False, "No puede tener más de 30 caracteres.\n"
    
    if not all(caracter.isalpha() or caracter.isspace() for caracter in nombre):
        return False, "Solamente puede contener letras.\n"
    
    if len(nombre.strip()) == 0:
        return False, "No puede ser nulo.\n"

    if nombre[0].isspace() or nombre[-1].isspace():
        return False, "No puede empezar ni terminar con un espacio.\n"
    
    return True, " "


def validar_apellido(apellido):
    return validar_nombre(apellido)


def validar_cuil(cuil):
    partes = cuil.split("-")

    if len(partes) != 3:
        return False, "El CUIL debe tener el formato XX-XXXXXXXX-X\n"
    
    parte_inicial, numero_dni, digito_verificador = partes

    if not (parte_inicial.isdigit() and numero_dni.isdigit() and digito_verificador.isdigit()):
        return False, "El CUIL solamente debe tener números\n"

    if parte_inicial not in ["20", "23", "24", "27"]:
        return False, "El CUIL debe comenzar con 20, 23, 24 o 27\n"

    if len(parte_inicial + numero_dni + digito_verificador) != 11:
        return False, "El CUIL debe tener un total de 11 dígitos.\n"

    return True, " "


def validar_correo(correo):
    patron = r'^[a-zA-Z][a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(patron, correo):
        return True, " "
    else:
        return False, "El correo no cumple con el formato.\n"


def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres.\n"
    
    if not any(caracter.isupper() for caracter in contraseña):
        return False, "La contraseña debe contener al menos una letra mayúscula.\n"
    
    if not any(caracter.islower() for caracter in contraseña):
        return False, "La contraseña debe contener al menos una letra minúscula.\n"
    
    if not any(caracter.isdigit() for caracter in contraseña):
        return False, "La contraseña debe contener al menos un número.\n"
    
    caracteres_especiales = "!@#$%^&*()-_+=<>?/{}[]|"
    if not any(caracter in caracteres_especiales for caracter in contraseña):
        return False, "La contraseña debe contener al menos un carácter especial.\n"
    
    return True, " "


def validar_datos():
    validacion_nombre = False
    while not validacion_nombre:
        nombre = input("Introduzca su nombre: ")
        validacion_nombre, mensaje = validar_nombre(nombre)
        print(mensaje)

    validacion_apellido = False
    while not validacion_apellido:
        apellido = input("Introduzca su apellido: ")
        validacion_apellido, mensaje = validar_apellido(apellido)
        print(mensaje)
            
    validacion_cuil = False
    while not validacion_cuil:
        cuil = input("Introduzca su cuil: ")
        validacion_cuil, mensaje = validar_cuil(cuil)
        print(mensaje)
        
    validacion_correo = False
    while not validacion_correo:
        correo = input("Introduzca su correo eléctronico: ")
        validacion_correo, mensaje = validar_correo(correo)
        print(mensaje)
        
    validacion_contraseña = False
    while not validacion_contraseña:
        contraseña = input("Introduzca su contraseña: ")
        validacion_contraseña, mensaje = validar_contraseña(contraseña)
        print(mensaje)

    return (nombre, apellido, cuil, correo, contraseña)