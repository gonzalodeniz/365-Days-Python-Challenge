import pytest
from elemento_maximo_matriz_numpy import *


def test_elemento_maximo_matriz() -> None:
    matriz: list[list[int]] = [
        [1, 2, 3],
        [4, 9, 6],
        [7, 8, 5]
    ]
    resultado_esperado: dict[str, int | tuple[int, int]] = {'maximo': 9, 'posicion': (1, 1)}
    assert buscar_maximo_y_posicion(matriz) == resultado_esperado

    matriz = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
    resultado_esperado = {'maximo': 90, 'posicion': (2, 2)}
    assert buscar_maximo_y_posicion(matriz) == resultado_esperado

    matriz = [
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5]
    ]
    resultado_esperado = {'maximo': 5, 'posicion': (0, 0)}
    assert buscar_maximo_y_posicion(matriz) == resultado_esperado

    matriz = [
        [-1, -2, -3],
        [-4, -9, -6],
        [-7, -8, -5]
    ]
    resultado_esperado = {'maximo': -1, 'posicion': (0, 0)}
    assert buscar_maximo_y_posicion(matriz) == resultado_esperado