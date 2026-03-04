
def ejemplo_listas():
    print("\n--- Listas ---")
    frutas = ["manzana", "banana", "cereza"]
    print("Original:", frutas)

    frutas.append("kiwi")
    print("Después de append:", frutas)

    frutas[1] = "plátano"
    print("Después de modificar:", frutas)

    frutas.sort()
    print("Ordenada:", frutas)

def ejemplo_tuplas():
    print("\n--- Tuplas ---")
    coordenadas = (10, 20)
    print("Tupla:", coordenadas)

def ejemplo_diccionarios():
    print("\n--- Diccionarios ---")
    persona = {
        "nombre": "Ana",
        "edad": 30,
        "ciudad": "Toluca"
    }
    print("Diccionario:", persona)

    persona["edad"] = 31
    persona["email"] = "ana@mail.com"
    print("Modificado:", persona)

    for clave, valor in persona.items():
        print(clave, "->", valor)

def ejemplo_conjuntos():
    print("\n--- Conjuntos ---")
    a = {1, 2, 3, 3, 2}
    b = {3, 4, 5}

    print("Conjunto a:", a)
    print("Conjunto b:", b)

    print("Unión:", a | b)
    print("Intersección:", a & b)
    print("Diferencia:", a - b)

def ejemplo_compresion_listas():
    print("\n--- Compresión de listas ---")
    cuadrados = [x**2 for x in range(10)]
    print("Cuadrados:", cuadrados)

def main():
    ejemplo_listas()
    ejemplo_tuplas()
    ejemplo_diccionarios()
    ejemplo_conjuntos()
    ejemplo_compresion_listas()

if __name__ == "__main__":
    main()