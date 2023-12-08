#2:31:06
diccionario = {
    "Nombre" : 'Leonardo',
    "Apellido" : 'García',
    "Edad" : "23 años"
}

#obteniendo un elemento con get() (si no encuentra el elemento no me tira una excepción, dice "none")
claves = diccionario.get("Edad")

#pop: se eliminan elementos del diccionario 
diccionario.pop("Edad") 

print(diccionario)