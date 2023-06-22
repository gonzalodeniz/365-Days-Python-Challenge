# -*- coding: utf-8 -*-

import pytest
from contador_submatrices import *


def test_inicializacion_matriz():
    m = Matriz(3, 3, 0)
    assert m.m == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert m.filas == 3
    assert m.columnas == 3


def test_matriz_de_listas():
    m = Matriz.de_listas([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert m.m == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert m.filas == 3
    assert m.columnas == 3


def test_get_set():
    m = Matriz(3, 3, 0)
    m.set(1, 1, 5)
    assert m.get(1, 1) == 5


def test_contador_submatrices():
    ma = Matriz.de_listas([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    mb = Matriz.de_listas([[1, 2]])
    assert contador_submatrices(ma, mb) == 3

    ma = Matriz.de_listas([[1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3]])
    mb = Matriz.de_listas([[1, 2, 3]])
    assert contador_submatrices(ma, mb) == 4

    ma = Matriz.de_listas([[1, 2, 3], [1, 2, 3]])
    mb = Matriz.de_listas([[1, 2, 3, 4]])
    assert contador_submatrices(ma, mb) == 0

def test_validacion():
    with pytest.raises(AssertionError):
        Matriz('a', 3)
    with pytest.raises(AssertionError):
        Matriz(3, 'b')
    with pytest.raises(AssertionError):
        Matriz.de_listas([1, 2, 3])
    m = Matriz(3, 3, 0)
    with pytest.raises(AssertionError):
        m.get(3, 3)
    with pytest.raises(AssertionError):
        m.set(3, 3, 5)
