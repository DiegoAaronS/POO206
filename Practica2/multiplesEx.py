try:
    num = int(input("Introduce un número: "))
    print(10 / num)
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
