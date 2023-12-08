#Calculadora de índice de masa corporal
peso = float(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / altura ** 2
redondeo = round(imc,2)
print(f"Su índice de masa corporal es: {redondeo} %")