animales = {"gato","perro","loro","tortuga"}
numeros = {12,134,64,70}

#recorriendo la conjunto animales
for animal in animales :
    print(f"Ahora la variable animal es: {animal}")

#recorriendo la conjunto numeros y multiplicándolo por 10    
for numero in numeros :
    resultado = numero * 10
    print(resultado)    

#iterando dos conjuntos del mismo tamaño al mismo tiempo
for animal,numero in zip(animales,numeros) :
    print(f"recorrido conjunto 1: {animal} ")
    print(f"recorrido conjunto 2: {numero}")
    
for num in range(10,20):
    print(num) 
    
#forma correcta de recorrer una conjunto con su índice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el índice es: {indice}  y el valor es: {valor}")
    
#usando el else
for numero in numeros :
    print(f"ejecutando el último bucle, valor actual: {numero}")
else:
    print("El bucle terminó.")