# Pregunta 2: Encontrar al pasajero más cercano en un mapa


def detectar_pasajero_mas_cercano(A, B, C):
   
    (ax, ay), (bx, by), (cx, cy) = A, B, C

    # Calcular las distancias Manhattan
    distancia_a_b = abs(ax - bx) + abs(ay - by)
    distancia_a_c = abs(ax - cx) + abs(ay - cy)

    # Comparación de las distancias
    if distancia_a_b < distancia_a_c:
        return "El pasajero más cercano es B"
    elif distancia_a_c < distancia_a_b:
        return "El pasajero más cercano es C"
    else:
        return "Ambos pasajeros están a la misma distancia"

# Definir las coordenadas
A = (0, 0)
B = (1, 2)
C = (3, 1)


resultado = detectar_pasajero_mas_cercano(A, B, C)
print(resultado)
