def tabla_de_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:\n")
    for factor2 in range(1, 11):
        producto = numero * factor2
        print(f"{numero} x {factor2} = {producto}")

try:
    numero_real = float(input("Introduce un número real: "))
    tabla_de_multiplicar(numero_real)
except ValueError:
    print("¡Debes introducir un número real válido!")