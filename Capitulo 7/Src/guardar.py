import json

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

print(f"Hola {nombre}, tienes {edad} años")
print("Hola {}, tienes {} años".format(nombre, edad))

datos = {
    "nombre": nombre,
    "edad": edad
}

with open("datos.json", "w", encoding="utf-8") as f:
    json.dump(datos, f)

with open("datos.json", "r", encoding="utf-8") as f:
    contenido = json.load(f)

print("Datos guardados:", contenido)

print("str:", str(contenido))
print("repr:", repr(contenido))