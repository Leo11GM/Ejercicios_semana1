#Realizar sistema de calificaciones
diccionario = {
    "Ana" : [7 , 9 , 5],
    "José" : [10 , 9 , 10],
    "Diego" : [3 , 5 , 2],
    "Pepito" : [6 , 7 , 5]   
}
nombre = input("Nombre de alumno: ")

if nombre in diccionario :
    promedio = sum(diccionario[nombre]) / len(diccionario[nombre])
    redondeo = round(promedio , 2)
    if promedio >= 9:
        print("Excelente")
    elif 7 <= promedio < 9:
        print("Bueno")
    elif 6 <= promedio < 7:
        print("Aprobado")
    elif promedio < 6:
        print("Reprobado")
    
    print(f"El estudiante {nombre} tiene un promedio de: {redondeo} ")
else:
    print("El estudiante no se encuentra en el sistema")
