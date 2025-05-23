while True:
    try:
        año = int(input("Introduce un año: "))
        if año < 0:
            raise ValueError
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            resultado = "bisiesto"
        else:
            resultado = "no bisiesto"
        print(f"Es {resultado}.")
        break
    except ValueError:
        print("Error: Ingrese un numero entero valido.")
