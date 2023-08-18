def encontrar_mayor_menor(numero1, numero2):
    if numero1 > numero2:
        mayor = numero1
        menor = numero2
    else:
        mayor = numero2
        menor = numero1
    return mayor, menor

try:
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
    
    mayor, menor = encontrar_mayor_menor(numero1, numero2)
    
    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")
except ValueError:
    print("¡Debes introducir números válidos!")