animales = ["gato","perro","loro","tortuga"]
numeros = [12,134,64,70]

#recorriendo la lista animales
for animal in animales :
    print(f"Ahora la variable animal es: {animal}")

#recorriendo la lista numeros y multiplicándolo por 10    
for numero in numeros :
    resultado = numero * 10
    print(resultado)    

#iterando dos listas del mismo tamaño al mismo tiempo
for animal,numero in zip(animales,numeros) :
    print(f"recorrido lista 1: {animal} ")
    print(f"recorrido lista 2: {numero}")
    
for num in range(10,20):
    print(num) 
    
#forma correcta de recorrer una lista con su índice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el índice es: {indice}  y el valor es: {valor}")