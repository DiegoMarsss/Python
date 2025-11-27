limite = 100  
multiplicador = 2.5 

fibonacci = [0, 1]  

a, b = 0, 1

while a < limite:
    a, b = b, a + b 
    if a < limite:
        fibonacci.append(a)  

mensaje_inicial = "Serie de Fibonacci hasta " + str(limite) + ":"  
mensaje_lista = "Lista completa: " + str(fibonacci) 
mensaje_slice = "Últimos 3 elementos: " + str(fibonacci[-3:])  # Slicing de lista

suma = sum(fibonacci)  
promedio = suma / len(fibonacci)  
mensaje_numeros = f"El promedio es {promedio:.2f} y la suma es {suma}."  

detalles = [
    fibonacci,  
    [suma, promedio],  
    ["Mensaje", mensaje_inicial]  
]

print(mensaje_inicial)
for num in fibonacci:
    print(num, end=', ')  
print("\n")  

print(mensaje_lista)
print(mensaje_slice)
print(mensaje_numeros)

print("Acceso a sublista de cálculos:", detalles[1])
print("Primer elemento de la sublista de mensaje:", detalles[2][0])