
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "Leonardo"
numeros = [2,5,8,10]
for fruta in frutas:
    if fruta == "granada" :
        continue
    print(f"Comeré {fruta}")
    
#evitar que el bucle siga ejecutándose
for fruta in frutas:
    if fruta == "pera":
        break
print("Bucle terminado.")

#recorrer una cadena de texto
for letra in cadena:
    print(letra)

#for en una sola línea de código
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero*2)
    
#print(numeros_duplicados)

#Haciendo lo mismo que está arriba pero más corto
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)