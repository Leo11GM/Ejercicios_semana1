#crear un gestor de contactos
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
#pidiendole al usuario que ingrese el nombre de contacto
buscar = input("Ingrese el nombre de contacto: ").capitalize()
if buscar in contactos:
    print(f"Información del contacto: {contactos[buscar]} ")
    actualizar = input("¿Desea actualizar el contacto? ").lower()
    if actualizar == "si":
        nuevo_correo = input("Escriba el correo nuevo: ").lower()
        nuevo_telefono = input("Escriba el teléfono nuevo:")
        print("Información actualizada del usuario.")
        print(f"Correo: {nuevo_correo} ")
        print(f"Teléfono: {nuevo_telefono} ")
    else:
        print("Saliendo...")
#si el contacto no se encuentra, se le da opción al usuario a agregar uno
else:
    print("Usuario no encontrado.")
    agregar_contacto = input("¿Desea agregar un contacto? ").lower()
    if agregar_contacto == "si" :
        #pidiendo datos del nuevo contacto
        nombre_contacto = input("Ingrese el nombre del contacto nuevo: ").capitalize()
        correo_contacto = input("Ingrese el correo del contacto nuevo: ").lower()
        telefono_contacto = input("Ingrese el número de teléfono del contacto nuevo: ")
        #añadiendo contacto
        contactos[nombre_contacto] = {
            "Correo" : correo_contacto ,
            "Teléfono" : telefono_contacto
        }
        print(contactos)
        print("Contacto añadido.")   
    else :
        print("Saliendo...")
borrar = input("¿Desea eliminar algún contacto? ").lower()
if borrar == "si" :
    contacto_borrar = input("¿Qué contacto desea eliminar? ")
    if contacto_borrar in contactos :
        contactos.pop(contacto_borrar)
        print(contactos)
        print("Contacto eliminado.")
    else:
        print("Contacto no encontrado, saliendo...")       
else:
        print("Saliendo...")
