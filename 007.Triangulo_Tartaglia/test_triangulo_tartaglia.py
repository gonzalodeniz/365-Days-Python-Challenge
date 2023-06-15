# -*- coding: utf-8 -*-
import pytest
import pytest
from triangulo_tartaglia import triangulo_tartaglia, calcula_fila_siguiente, coeficiente_binomial # Reemplaza 'file' por el nombre de tu archivo

def test_triangulo_tartaglia() -> None:
    assert triangulo_tartaglia(1) == [[1]]
    assert triangulo_tartaglia(2) == [[1], [1,1]]
    assert triangulo_tartaglia(3) == [[1], [1,1], [1,2,1]]
    assert triangulo_tartaglia(4) == [[1], [1,1], [1,2,1], [1,3,3,1]]
    assert triangulo_tartaglia(5) == [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]

def test_calcula_fila_siguiente()  -> None:
    assert calcula_fila_siguiente([1]) == [1,1]
    assert calcula_fila_siguiente([1,1]) == [1,2,1]
    assert calcula_fila_siguiente([1,2,1]) == [1,3,3,1]
    assert calcula_fila_siguiente([1,3,3,1]) == [1,4,6,4,1]
    assert calcula_fila_siguiente([1,4,6,4,1]) == [1,5,10,10,5,1]

def test_coeficiente_binomial()  -> None:
    # Nota: Esta prueba fallará, ya que la función coeficiente_binomial actualmente solo retorna 0
    assert coeficiente_binomial(5, 3) == 10
    assert coeficiente_binomial(6, 2) == 15
    assert coeficiente_binomial(4, 2) == 6
    assert coeficiente_binomial(7, 3) == 35
