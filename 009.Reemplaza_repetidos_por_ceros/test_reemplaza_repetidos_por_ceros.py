import pytest
from reemplaza_repetidos_por_ceros import *


def test_cuenta_numeros_matriz():
    assert cuenta_numeros_matriz([]) == {}
    assert cuenta_numeros_matriz([[1]]) == {1: 1}
    assert cuenta_numeros_matriz([[1, 2, 3]]) == {1: 1, 2: 1, 3: 1}
    assert cuenta_numeros_matriz([[1, 2, 3, 2]]) == {1: 1, 2: 2, 3: 1}


def test_sustituye_repetidos_por_cero():
    assert sustituye_repetidos_por_cero([], {}) == []
    assert sustituye_repetidos_por_cero([[1]], {1: 1}) == [[1]]
    assert sustituye_repetidos_por_cero([[1, 2, 3]], {1: 1, 2: 1, 3: 1}) == [[1, 2, 3]]
    assert sustituye_repetidos_por_cero([[1, 2, 3, 2]], {1: 1, 2: 2, 3: 1}) == [[1, 0, 3, 0]]


def test_calcula_elementos_sin_repetir():
    assert calcula_elementos_sin_repetir({}) == 0
    assert calcula_elementos_sin_repetir({1: 1}) == 1
    assert calcula_elementos_sin_repetir({1: 1, 2: 1, 3: 1}) == 3
    assert calcula_elementos_sin_repetir({1: 1, 2: 2, 3: 1}) == 2


def test_reemplaza_repetidos_por_ceros():
    assert reemplaza_repetidos_por_ceros([]) == []
    assert reemplaza_repetidos_por_ceros([[1]]) == [[1]]
    assert reemplaza_repetidos_por_ceros([[1, 2, 3]]) == [[1, 2, 3]]
    assert reemplaza_repetidos_por_ceros([[1, 2, 3, 2]]) == [[1, 0, 3, 0]]
