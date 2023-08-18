def metros_a_kilometros(metros):
    kilometros = metros / 1000
    return kilometros

try:
    metros = float(input("Ingresa una cantidad en metros: "))
    kilometros = metros_a_kilometros(metros)
    print(f"{metros} metros son equivalentes a {kilometros:.2f} kilómetros.")
except ValueError:
    print("¡Debes introducir una cantidad válida en metros!")