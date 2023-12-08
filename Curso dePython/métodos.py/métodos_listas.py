#creando una lista con list()
lista = list(("Leonardo", "Ernesto", "García", "Monteagudo",23))
lista2 = ([234 , 4532, 753 ,3778 , True , False])
#len: devuelve cantidad de caracteres y en la listas, duelve cantidad de elementos en la lista
cadena = "hola"
resultado =len(lista)

#append: agrega elementos a la lista
lista.append("1.83")
#print(lista) se imprime la lista

#insert: agregando un elemento a la lista en un índice específico
lista.insert(2,"HOLA")
#print(lista)

#extend: agregando varios elementos a la lista
lista.extend(["siuu","ingeniero"])
#print(lista)

#pop: se eliminan elementos de la lista por su índice
lista.pop(0) #si pongo -1 elimino el último
#print(lista)

#remove: remueve un elemento de la lista por su valor
lista.remove("1.83")
#print(lista)

#clear: elimina todos los elementos de la lista
#lista.clear()

#sort: ordena los elementos en forma ascendente
lista2.sort()
#lista2.sort(reverse=True) con esto se invierten los elementos de la lista
#print(lista2)

#reverse: invierte el orden de los elementos
lista2.reverse()
#print(lista2)

#verificando si un elemento se encuentra en la lista
encontrando_elemento = lista2.index(234)
print(encontrando_elemento)
