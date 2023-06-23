import pytest
from typing import Dict, Any, List
from matriz import Matriz

def test_init() -> None:
    m: Matriz = Matriz(3, 2, 5)
    assert m.filas == 3
    assert m.columnas == 2
    assert m.m == [[5, 5], [5, 5], [5, 5]]

def test_de_listas() -> None:
    m: Matriz = Matriz.de_listas([[1, 2], [3, 4], [5, 6]])
    assert m.filas == 3
    assert m.columnas == 2
    assert m.m == [[1, 2], [3, 4], [5, 6]]

def test_random() -> None:
    m: Matriz = Matriz.random(3, 2, 10)
    assert m.filas == 3
    assert m.columnas == 2

def test_get() -> None:
    m: Matriz = Matriz.de_listas([[1, 2], [3, 4], [5, 6]])
    assert m.get(1, 1) == 4

def test_set() -> None:
    m: Matriz = Matriz.de_listas([[1, 2], [3, 4], [5, 6]])
    m.set(1, 1, 10)
    assert m.get(1, 1) == 10

def test_copy() -> None:
    m1: Matriz = Matriz.de_listas([[1, 2], [3, 4], [5, 6]])
    m2: Matriz = m1.copy()
    assert m1.m == m2.m
    m1.set(1, 1, 10)
    assert m1.m != m2.m

def test_get_frecuencia_valores() -> None:
    m: Matriz = Matriz.de_listas([[1, 2, 2], [3, 4, 4], [5, 6, 6]])
    assert m.get_frecuencia_valores() == {1: 1, 2: 2, 3: 1, 4: 2, 5: 1, 6: 2}


