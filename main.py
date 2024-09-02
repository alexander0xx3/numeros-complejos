def obtener_numero_complejo(mensaje):
    """Obtiene un número complejo desde la entrada del usuario."""
    while True:
        try:
            entrada = input(mensaje)
            partes = entrada.split(',')
            real = float(partes[0])
            imaginario = float(partes[1])
            return complex(real, imaginario)
        except ValueError:
            print("Entrada inválida. Por favor, ingrese el número en el formato 'parte_real,parte_imaginaria'.")


def elegir_operacion():
    """Permite al usuario elegir una operación matemática."""
    print("Elija una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo")
    print("6. Conjugado")
    print("7. Parte real e imaginaria")

    while True:
        opcion = input("Ingrese el número de la operación deseada (1-7): ")
        if opcion in {'1', '2', '3', '4', '5', '6', '7'}:
            return int(opcion)
        else:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 7.")


def realizar_operacion(z1, z2, operacion):
    """Realiza la operación matemática seleccionada."""
    if operacion == 1:  # Suma
        resultado = z1 + z2
        print(f"Suma: {z1} + {z2} = {resultado}")
    elif operacion == 2:  # Resta
        resultado = z1 - z2
        print(f"Resta: {z1} - {z2} = {resultado}")
    elif operacion == 3:  # Multiplicación
        resultado = z1 * z2
        print(f"Multiplicación: {z1} * {z2} = {resultado}")
    elif operacion == 4:  # División
        if z2 != 0:
            resultado = z1 / z2
            print(f"División: {z1} / {z2} = {resultado}")
        else:
            print("No se puede dividir por cero.")
    elif operacion == 5:  # Módulo
        modulo_z1 = abs(z1)
        modulo_z2 = abs(z2)
        print(f"Módulo de {z1}: {modulo_z1}")
        print(f"Módulo de {z2}: {modulo_z2}")
    elif operacion == 6:  # Conjugado
        conjugado_z1 = z1.conjugate()
        conjugado_z2 = z2.conjugate()
        print(f"Conjugado de {z1}: {conjugado_z1}")
        print(f"Conjugado de {z2}: {conjugado_z2}")
    elif operacion == 7:  # Parte real e imaginaria
        print(f"Parte real de {z1}: {z1.real}")
        print(f"Parte imaginaria de {z1}: {z1.imag}")
        print(f"Parte real de {z2}: {z2.real}")
        print(f"Parte imaginaria de {z2}: {z2.imag}")


def main():
    print("Bienvenido al programa de operaciones con números complejos.")

    z1 = obtener_numero_complejo("Ingrese el primer número complejo (formato 'parte_real,parte_imaginaria'): ")
    z2 = obtener_numero_complejo("Ingrese el segundo número complejo (formato 'parte_real,parte_imaginaria'): ")

    operacion = elegir_operacion()

    realizar_operacion(z1, z2, operacion)


if __name__ == "__main__":
    main()
