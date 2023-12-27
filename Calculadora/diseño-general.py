def suma(num1, num2):
    return round(num1 + num2, 2)
def resta(num1, num2):
    return(num1 - num2, 2)
def multiplicación(num1, num2):
    return round(num1 * num2, 2)
def division(num1, num2):
    if num2 != 0:
        return round(num1/num2, 2)
    else:
        print("No se puede dividir un número entre cero. No seas 0t.") 
    
def operacion():
    while True:
    
        print("**********************************")
        print("* ¿Qué operación desea realizar? *")
        print("**********************************")
        print("* 1. Suma                        *")
        print("* 2. Resta                       *")
        print("* 3. Multiplicación              *")
        print("* 4. División                    *")
        print("*                                *")
        print("* 5. Salir                       *")
        print("**********************************")

        elegir = int(input("Elija la operación a realizar: "))
        
        if elegir == 5:
            print("Saliendo... ")
            break
        if elegir in [1,2,3,4]:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if elegir == 1:
                total = round(num1 + num2, 2)
                print(f"El resultado de la suma es: {total}")
            elif elegir == 2:
                total = round(num1 - num2, 2)
                print(f"El resultado de la resta es: {total}") 
            elif elegir == 3:
                total = round(num1 * num2, 2)
                print(f"El total de la multiplicación es: {total}")
            elif elegir == 4:
                if num2 != 0:
                    total = round(num1/num2, 2)
                    print(f"El total de la división es: {total}")
                else:
                    print("No se puede dividir un número entre cero. No seas 0t. ")
                    
operacion()