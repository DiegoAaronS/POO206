while True:
 try:
    numero = (int(input("Introduce un número: ")))
    if numero % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"
    print(f"El número {numero} es {resultado}.")
    break
 except ValueError:
    print("Error: Debes ingresar un número entero válido.")