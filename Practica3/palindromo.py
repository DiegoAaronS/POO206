while True:
    try:
        x = input('Escribe una palabra: ').lower()
        if not x.isalpha():
            raise ValueError("Error: Debes ingresar una palabra válida.")
        y = ''.join(reversed(x))
        if y == x:
            print('Es un Palíndromo')
        else:
            print('No es un Palíndromo')
        break
    except ValueError as e:
        print(e)