def ordenar_descendente(lista_numeros):
    for i in range(len(lista_numeros)):
        for j in range(i + 1, len(lista_numeros)):
            if lista_numeros[j] > lista_numeros[i]:
                lista_numeros[i], lista_numeros[j] = lista_numeros[j], lista_numeros[i]

try:
    lista_numeros = []
    for i in range(5):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        lista_numeros.append(numero)
    
    ordenar_descendente(lista_numeros)
    
    print("Números ordenados de forma descendente:")
    for numero in lista_numeros:
        print(numero)
except ValueError:
    print("¡Debes introducir números válidos!")