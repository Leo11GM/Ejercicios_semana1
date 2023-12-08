#Diccionario de sinónimos
diccionario = {
    "casa" : "Hogar",
    "generosidad" : "Bondad",
    "restar" : "Reducir",
    "ahorrar" : "Economizar",
    "gastar" : "Desembolsar"
}

palabra = input("Ingrese una palabra: ").lower()
print(palabra)
if palabra in diccionario:
    print(f"El sinónimo de la palabra {palabra} es: {diccionario[palabra]} ") 
else :
    print("Palabra no encontrada")