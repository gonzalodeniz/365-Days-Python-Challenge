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

from typing import Any, List, cast

def coeficiente_binomial(m: int, n: int) -> int:

    triangulo: list[list[int]]
    triangulo = crea_triangulo_tartaglia(m+1, [])
    return triangulo[m][n]


def crea_triangulo_tartaglia(numero_de_filas: int, triangulo_previo:  list[Any]) -> list[list[int]]:
    fila_siguiente: list[int]

    if numero_de_filas == 0:
        return triangulo_previo
    else:
        ultima_fila_triangulo = calcula_ultima_fila_triangulo(triangulo_previo)
        fila_siguiente = calcula_fila_siguiente(ultima_fila_triangulo)
        triangulo_previo.append(fila_siguiente)
        return crea_triangulo_tartaglia(numero_de_filas - 1, triangulo_previo)


def calcula_ultima_fila_triangulo(triangulo: list[Any]) -> list[Any]:
    if len(triangulo) == 0:
        return []
    else:
        return cast(List[Any], triangulo[-1])

def calcula_fila_siguiente(fila: list[int]) -> list[int]:
    if len(fila) == 0:
        return [1]
    elif len(fila) == 1:
        return [1, 1]
    else:
        siguiente_fila = [1]
        for i in range(len(fila) - 1):
            siguiente_numero = fila[i] + fila[i+1]
            siguiente_fila.append(siguiente_numero)
        siguiente_fila.append(1)
        return siguiente_fila



def main() -> None:

    resultado = coeficiente_binomial(4, 2)
    print(resultado)



if __name__ == "__main__":
    main()
