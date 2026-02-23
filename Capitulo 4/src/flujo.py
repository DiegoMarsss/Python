def clasificar_nota(nombre, calificacion, mostrar_mensaje=True):
    if calificacion >= 90:
        resultado = "Excelente"
    elif calificacion >= 70:
        resultado = "Aprobado"
    elif calificacion >= 60:
        resultado = "Suficiente"
    else:
        resultado = "Reprobado"

    match resultado:
        case "Excelente":
            emoji = "🏆"
        case "Aprobado":
            emoji = "✅"
        case "Suficiente":
            emoji = "⚠️"
        case "Reprobado":
            emoji = "❌"

    if mostrar_mensaje:  
        print(f"{nombre} obtuvo {calificacion}: {resultado} {emoji}")

    return resultado


for i in range(5):
    if i == 3:
        continue  
    if i == 4:
        break  
    print("Número:", i)

print("\n--- Resultados ---\n")

clasificar_nota("Diego", 95)
clasificar_nota(nombre="Ana", calificacion=72)
clasificar_nota("Luis", 58, mostrar_mensaje=False)
