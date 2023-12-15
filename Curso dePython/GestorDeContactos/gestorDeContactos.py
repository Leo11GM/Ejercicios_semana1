import os

# Diccionario de contactos
contactos = {
    "Juan Pérez": {"email": "juan.perez@gmail.com", "teléfono": "123456789"},
    "María López": {"email": "maria.lopez@hotmail.com", "teléfono": "987654321"},
}

# Menú principal
def menu():
    print("***********************************************")
    print("*       Menú principal")
    print("*    1. Buscar contacto")
    print("*    2. Actualizar contacto")
    print("*    3. Agregar nuevo contacto")
    print("*    4. Eliminar contacto")
    print("*    5. Salir")
    opcion = input("¿Qué deseas hacer? (1-5): ")
    return int(opcion)

# Buscar contacto
def buscar_contacto():
    nombre = input("Introduce el nombre del contacto: ")
    if nombre in contactos:
        contacto = contactos[nombre]
        print("Email:", contacto["email"])
        print("Teléfono:", contacto["teléfono"])
    else:
        print("Contacto no encontrado")

# Actualizar contacto
def actualizar_contacto():
    nombre = input("Introduce el nombre del contacto: ")
    if nombre in contactos:
        contacto = contactos[nombre]
        print("Email actual:", contacto["email"])
        print("Teléfono actual:", contacto["teléfono"])
        email = input("Nuevo email: ")
        if email != "":
            contacto["email"] = email
        telefono = input("Nuevo teléfono: ")
        if telefono != "":
            contacto["teléfono"] = telefono
        contactos[nombre] = contacto
        print("Contacto actualizado")
    else:
        print("Contacto no encontrado")

# Agregar nuevo contacto
def agregar_nuevo_contacto():
    nombre = input("Introduce el nombre del contacto: ")
    email = input("Introduce el email del contacto: ")
    telefono = input("Introduce el teléfono del contacto: ")
    contactos[nombre] = {"email": email, "teléfono": telefono}
    print("Contacto agregado")

# Eliminar contacto
def eliminar_contacto():
    nombre = input("Introduce el nombre del contacto: ")
    if nombre in contactos:
        del contactos[nombre]
        print("Contacto eliminado")
    else:
        print("Contacto no encontrado")

# Bucle principal
while True:
    opcion = menu()
    os.system("cls")
    if opcion == 1:
        buscar_contacto()
    elif opcion == 2:
        actualizar_contacto()
    elif opcion == 3:
        agregar_nuevo_contacto()
    elif opcion == 4:
        eliminar_contacto()
    elif opcion == 5:
        break