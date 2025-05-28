while True:
    try:
        numero = int(input("Introduce un número entero positivo: "))
        if numero <= 0:
            raise ValueError("El número debe ser positivo y mayor que cero")
        print(", ".join(str(i) for i in range(numero, -1, -1)))
        break
    except ValueError as e:
        print(f"Error: {e}")
