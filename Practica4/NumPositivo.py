while True:
    try:
        numero = int(input("Introduce un número entero positivo mayor de 10: "))
        if numero <= 10:
            raise ValueError
        print(", ".join(str(i) for i in range(3, numero + 1, 2)))
        break
    except ValueError:
        print("Error: Debes ingresar un número entero válido mayor a 10")