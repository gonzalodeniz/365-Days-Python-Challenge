# -*- coding: utf-8 -*-

"""
Desarrolle un procedimiento que calcule m sobre n a partir de la construción del triángulo de Tartaglia

Triángulo de Tartaglia
1
11
121
1331
14641
"""

def coeficiente_binomial(m: int, n: int) -> int:

    triangulo: list[list[int]]
    triangulo = crea_triangulo_tartaglia(m+1)
    return triangulo[m][n]


def crea_triangulo_tartaglia(numero_de_filas: int) -> list[list[int]]:
    triangulo: list[list[int]]

    triangulo = []
    for i in range(numero_de_filas):
        if i == 0:
            triangulo.append([1])
        else:
            fila_anterior = triangulo[i-1]
            fila_siguiente = calcula_fila_siguiente(fila_anterior)
            triangulo.append(fila_siguiente)

    return triangulo


def calcula_fila_siguiente(fila: list[int]) -> list[int]:
    if len(fila) == 1:
        return [1,1]
    else:
        siguiente_fila = [1]
        for i in range(len(fila) - 1):
            siguiente_numero = fila[i] + fila[i+1]
            siguiente_fila.append(siguiente_numero)
        siguiente_fila.append(1)
        return siguiente_fila



def main():
    resultado = coeficiente_binomial(4, 2)
    print(resultado)


if __name__ == "__main__":
    main()
