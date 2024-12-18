# -*- coding: utf-8 -*-
"""
Archivo: devops.py
Descripción: Soluciones a las preguntas de la prueba técnica.
"""

# -------------------------------
# Pregunta 1: Contar del 1 al 100
# 

def contar_del_1_al_100() -> None:
    """
    Función que recorre los números del 1 al 100 y evalúa las condiciones:
    - Si el número es divisible por 2 y 3, imprime "fla".
    - Si el número es divisible por 2, imprime "pan".
    - Si el número es divisible por 3, imprime "tu".
    - Si no es divisible por ninguno, imprime el número.
    """
    for i in range(1, 101):
        if i % 2 == 0 and i % 3 == 0:
            print("fla")
        elif i % 2 == 0:
            print("pan")
        elif i % 3 == 0:
            print("tu")
        else:
            print(i)

# Llamada a la función
if __name__ == "__main__":
    contar_del_1_al_100()


