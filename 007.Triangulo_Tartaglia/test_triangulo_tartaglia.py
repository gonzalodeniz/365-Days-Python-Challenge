import pytest

from triangulo_tartaglia import *
def test_calcula_fila_siguiente():
    assert calcula_fila_siguiente([1]) == [1, 1]
    assert calcula_fila_siguiente([1, 1]) == [1, 2, 1]
    assert calcula_fila_siguiente([1, 2, 1]) == [1, 3, 3, 1]
    assert calcula_fila_siguiente([1, 3, 3, 1]) == [1, 4, 6, 4, 1]

def test_crea_triangulo_tartaglia():
    assert crea_triangulo_tartaglia(1) == [[1]]
    assert crea_triangulo_tartaglia(2) == [[1], [1, 1]]
    assert crea_triangulo_tartaglia(3) == [[1], [1, 1], [1, 2, 1]]
    assert crea_triangulo_tartaglia(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert crea_triangulo_tartaglia(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

def test_coeficiente_binomial():
    assert coeficiente_binomial(1, 0) == 1
    assert coeficiente_binomial(2, 1) == 2
    assert coeficiente_binomial(4, 2) == 6
    assert coeficiente_binomial(5, 3) == 10
    assert coeficiente_binomial(5, 1) == 5

    # Prueba que debe fallar, ya que n > m
    with pytest.raises(IndexError):
        coeficiente_binomial(2, 3)

    # Prueba que debe fallar, ya que los coeficientes binomiales no están definidos para números negativos
    with pytest.raises(IndexError):
        coeficiente_binomial(-1, 0)

