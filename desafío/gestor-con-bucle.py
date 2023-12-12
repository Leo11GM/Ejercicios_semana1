#Creando gestor de contactos con while
contactos = {
    "Leonardo" : {
        "Correo" : "leogarciam11@gmail.com",
        "Teléfono" : "1234-5678"
    },
    "Josué" : {
        "Correo" : "josueavalos@gmail.com",
        "Teléfono" : "4321-5678"
    },
    "Diego" : {
        "Correo" : "diegoarias@gmail.com",
        "Teléfono" : "2314-8765"
    }
}
while True:
    buscar = input("Ingrese el nombre de contacto o 'salir' para salir: ").capitalize()

    if buscar == 'Salir':
        print("Saliendo...")
        break

    if buscar in contactos:
        print(f"Información del contacto: {contactos[buscar]} ")
        actualizar = input("¿Desea actualizar el contacto? (si/no): ").lower()

        if actualizar == "si":
            nuevo_correo = input("Escriba el correo nuevo: ").lower()
            nuevo_telefono = input("Escriba el teléfono nuevo:")
            print("Información actualizada del usuario.")
            print(f"Correo: {nuevo_correo} ")
            print(f"Teléfono: {nuevo_telefono} ")
        else:
            print("No se realizaron actualizaciones.")
    else:
        print("Usuario no encontrado.")
        agregar_contacto = input("¿Desea agregar un contacto? (si/no): ").lower()

        if agregar_contacto == "si":
            nombre_contacto = input("Ingrese el nombre del contacto nuevo: ").capitalize()
            correo_contacto = input("Ingrese el correo del contacto nuevo: ").lower()
            telefono_contacto = input("Ingrese el número de teléfono del contacto nuevo: ")

            contactos[nombre_contacto] = {
                "Correo": correo_contacto,
                "Teléfono": telefono_contacto
            }

            print(f"Contacto {nombre_contacto} añadido.")
        else:
            print("No se agregaron nuevos contactos.")

borrar = input("¿Desea eliminar algún contacto? (si/no): ").lower()

if borrar == "si":
    contacto_borrar = input("¿Qué contacto desea eliminar? ")

    if contacto_borrar in contactos:
        contactos.pop(contacto_borrar)
        print(f"Contacto {contacto_borrar} eliminado.")
    else:
        print("Contacto no encontrado.")
else:
    print("Saliendo...")
    
     