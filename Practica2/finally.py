try:
    numero = int(input("Introduce un número entero: "))
    resultado = 10 / numero
    print("El resultado de 10 dividido entre", numero, "es:", resultado)
except ValueError:
    print("Error: Debes ingresar un número entero válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir e0ntre cero.")
finally:
    print("Gracias por usar el programa.")
