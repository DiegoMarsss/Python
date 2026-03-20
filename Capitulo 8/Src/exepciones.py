def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre 0")
    return a / b


errores = []

for dato in ["10", "0", "hola"]:
    try:
        numero = int(dato)
        resultado = dividir(10, numero)

    except ValueError as e:
        e.add_note(f"Error con el dato: {dato}")
        errores.append(e)

    except Exception as e:
        errores.append(e)

    else:
        print(f"Resultado correcto: {resultado}")

    finally:
        print("Intento terminado\n")


if errores:
    print("Hubo errores:")
    for e in errores:
        print(e)