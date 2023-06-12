# -*- coding: utf-8 -*-
import pytest
from invertir_vector import *


def test_invertir_vector():
    # Caso de prueba 1: Vector vacío
    vector = []
    vector_invertido = invertir_vector(vector)
    assert vector_invertido == []

    # Caso de prueba 2: Vector de 2
    vector = [1, 2]
    vector_invertido = invertir_vector(vector)
    assert vector_invertido == [2, 1]

    # Caso de prueba 3: Vector de 5
    vector = [1, 2, 3, 4, 5]
    vector_invertido = invertir_vector(vector)
    assert vector_invertido == [5, 4, 3, 2, 1]
