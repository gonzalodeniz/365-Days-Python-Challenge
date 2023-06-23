import pytest
from traspuesta_matriz_numpy import *
from typing import Any


def test_traspuesta_matriz() -> None:
    # Caso de prueba 1: Matriz vacía
    matriz: list[list[Any]] = []
    traspuesta_matriz(matriz)
    assert matriz == []

    # Caso de prueba 2: Matriz de 2x2
    matriz = [[1, 2], [3, 4]]
    traspuesta_matriz(matriz)
    assert matriz == [[1, 3], [2, 4]]

    # Caso de prueba 3: Matriz rectangular de 3x2
    matriz = [[1, 2], [3, 4], [5, 6]]
    traspuesta_matriz(matriz)
    assert matriz == [[1, 3, 5], [2, 4, 6]]
