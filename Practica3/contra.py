import string
def validar_contraseña(contra):
    if len(contra) < 10:
        raise ValueError("Contraseña demasiado corta")
    if not any(char.isdigit() for char in contra):
        raise ValueError("Debe contener al menos un número")
    if not any(char in string.punctuation for char in contra):
        raise ValueError("Debe contener al menos un carácter especial")
    return
while True:
    try:
        contraseña = input("Introduce una contraseña: ").strip()
        if contraseña == "":
            raise ValueError("La contraseña no puede estar vacía.")
        validar_contraseña(contraseña)
        print("Contraseña válida.")
        break
    except ValueError as e:
        print(f"Error: {e}")