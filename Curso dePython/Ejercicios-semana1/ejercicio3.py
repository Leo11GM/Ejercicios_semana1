#Calcular promedio
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer número: "))
sum = num1 + num2 + num3
promedio = sum / 3
redondeo = round(promedio , 2)
print(f"El promedio de los tres valores es: {redondeo} ")