#Convertidor de temperatura
tipo_de_temperatura = input("Escriba C si el dato que desea ingresar es en grados Celsius o F si es en Fahrenheit: ")
if tipo_de_temperatura == "C" :
    dato = float(input("Escriba la temperatura a convertir:  °C "))
    celsius_a_fahrenheit = (dato * 1.8) + 32
    redondeo = round(celsius_a_fahrenheit,1)
    print(f"{dato} °C en Fahrenheit son: {redondeo} F")
elif tipo_de_temperatura == "F" :
    dato = float(input("Escriba la temperatura a convertir: F "))
    fahrenheit_a_celsius = (dato - 32) / 1.8
    redondeo = round(fahrenheit_a_celsius,1)
    print(f"{dato} F en Celsius son: {redondeo} °C")
elif tipo_de_temperatura  != "C" and "F":
    print("Unidad de medida no disponible.")


