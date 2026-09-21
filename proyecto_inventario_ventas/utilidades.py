def leer_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Ingresa un número igual o mayor a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada no válida. Ingresa un número entero.")


def leer_decimal(mensaje, minimo=None):
    while True:
        try:
            texto = input(mensaje).strip().replace(",", ".")
            valor = float(texto)
            if minimo is not None and valor < minimo:
                print(f"Ingresa un valor igual o mayor a {minimo}.")
                continue
            return round(valor, 2)
        except ValueError:
            print("Entrada no válida. Ingresa un número.")


def pausar():
    input("\nPresiona Enter para continuar...")
