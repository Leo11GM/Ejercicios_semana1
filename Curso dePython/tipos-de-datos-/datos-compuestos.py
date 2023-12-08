#list
lista = "Leonardo Ernesto","García Monteagudo",True, 1.83

#tupla: con este no se puede modificar la lista
#tupla = "Leonardo Ernesto","García Monteagudo",True, 1.83

#esto si
#lista[2] = "Siiiiu"
#print(lista[2])

# 1:02:29
#conjuntos: no tienen un orden fijo
conjunto = {"Leonardo Ernesto","García Monteagudo",True, 1.83}
#print(conjunto)
#en un conjunto no puede haber datos duplicados ni se puede acceder por un índice, a menos que se use un bucle

#Creando un diccionario: (la estructura es key : value y separamos con comas)

diccionario ={
    'Nombres' : "Leonardo Ernesto",
    'Apellidos' : "García Monteagudo",
    'está_emocionado' : "True",
    'Altura' : "1.83",
    'Dato_duplicado' : "García Monteagudo"
}
print(diccionario['Nombres'])