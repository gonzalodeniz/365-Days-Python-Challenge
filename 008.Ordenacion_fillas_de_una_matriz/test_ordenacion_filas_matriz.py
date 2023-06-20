import pytest

import pytest
from ordenacion_filas_matriz import ordena_filas_matriz, esta_matriz_ordenada

def test_es_matriz_ordenada():
    assert esta_matriz_ordenada([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == True
    assert esta_matriz_ordenada([[4, 5, 6], [1, 2, 3], [7, 8, 9]]) == False
    assert esta_matriz_ordenada([]) == True

def test_ordena_filas_matriz():
    assert ordena_filas_matriz([[4,5,6], [1,2,3], [7,8,9]]) == [[1,2,3], [4,5,6], [7,8,9]]
    assert ordena_filas_matriz([[1,2,3], [4,5,6], [7,8,9]]) == [[1,2,3], [4,5,6], [7,8,9]]
    assert ordena_filas_matriz([]) == []
    assert ordena_filas_matriz([[7,8,9], [4,5,6], [1,2,3]]) == [[1,2,3], [4,5,6], [7,8,9]]
