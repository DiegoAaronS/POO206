while True:
    try:
        frase = input("Introduce una frase: ").strip()
        if not frase:
            raise ValueError("La frase no puede estar vacía")
        if not all(char.isalpha() or char.isspace() for char in frase):
            raise ValueError("La frase solo puede contener letras y espacios")
        letra = input("Introduce una letra: ").strip()
        if len(letra) != 1 or not letra.isalpha():
            raise ValueError("Debes ingresar una única letra válida")
        cantidad = frase.lower().count(letra.lower())
        print(f"La letra '{letra}' aparece {cantidad} vez/veces en la frase")
        break 
    except ValueError as e:
        print(f"Error: {e}")