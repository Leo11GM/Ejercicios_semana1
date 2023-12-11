diccionario = {
    "Nombre" : "Leonardo",
    "Apellido" : "García",
    "Edad" : "23 años"
}

#recorriendo diccionarios con items() para obtener la clave y el valor
for key in diccionario :
    key 
    
    print(f"La clave es: {key} ")
    
#recorriendo diccionarios con items() para obtener la clave y el valor
for datos in diccionario.items() :
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key} y el valor es: {value}")