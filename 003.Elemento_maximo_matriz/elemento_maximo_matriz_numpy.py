"""
Desarrolle un procedimiento para obtener el elemento máximo de una matriz de ristras y su posición.

Aquí se utiliza la librería NumPy
"""

import numpy as np
from numpy import ndarray
from typing import Any


def elemento_maximo_matriz(matriz: list[list[int]]) -> dict[str, Any]:

    maximo: int
    posicion: tuple[int, int]

    maximo = _valor_maximo(matriz)
    posicion = _posicion_valor_maximo(matriz, maximo)

    return {'maximo': maximo,
            'posicion': posicion}


def _valor_maximo(matriz: list[list[int]]) -> int:
    maximo: int
    arr_matriz: ndarray
    arr_matriz = np.array(matriz)
    maximo = np.max(arr_matriz)
    return maximo


def _posicion_valor_maximo(matriz: list[list[int]], maximo: int) -> tuple[int, int]:
    posicion: tuple[int, int]
    arr_matriz: ndarray

    arr_matriz = np.array(matriz)
    arr_posicion = np.where(arr_matriz == maximo)
    posicion = (arr_posicion[0][0], arr_posicion[1][0])
    return posicion


def main() -> None:
    matriz: list[list[int]] = [
        [1, 2, 3],
        [4, 9, 6],
        [7, 8, 5]
    ]

    resultado = elemento_maximo_matriz(matriz)
    print(str(resultado))


if __name__ == "__main__":
    main()
