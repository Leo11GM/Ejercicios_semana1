#Diccionario de sinónimos
diccionario = {
    "Casa" : "Hogar",
    "Generosidad" : "Bondad",
    "Restar" : "Reducir",
    "Ahorrar" : "Economizar",
    "Gastar" : "Desembolsar"
}
palabra = input("Ingrese una palabra: ")
if palabra in diccionario:
    print(f"El sinónimo de la palabra {palabra} es: {diccionario[palabra]} ") 
else :
    print("Palabra no encontrada")