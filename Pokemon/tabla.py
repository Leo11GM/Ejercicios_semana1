def tabla_de_multiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:\n")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    try:
        numero = float(input("Ingresa un número para la tabla de multiplicar: "))
        tabla_de_multiplicar(numero)
    except ValueError:
        print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()