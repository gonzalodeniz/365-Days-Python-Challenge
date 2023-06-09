import pytest
from intercambio_variables_param_no_mutable import intercambio, ordena


def test_intercambio():
    # Prueba con números positivos
    assert intercambio(5, 3) == (3, 5)

    # Prueba con números negativos
    assert intercambio(-5, -3) == (-3, -5)

    # Prueba con cero y un número positivo
    assert intercambio(0, 3) == (3, 0)

    # Prueba con cero y un número negativo
    assert intercambio(0, -3) == (-3, 0)

    # Prueba con el mismo número
    assert intercambio(3, 3) == (3, 3)

    with pytest.raises(AssertionError):
        # Prueba con no enteros
        intercambio(5.5, 3)

def test_ordena():
    # Prueba con números positivos
    assert ordena(5, 3, 7) == (7, 5, 3)

    # Prueba con números negativos
    assert ordena(-5, -3, -7) == (-3, -5, -7)

    # Prueba con cero y números positivos
    assert ordena(0, 3, 7) == (7, 3, 0)

    # Prueba con cero y números negativos
    assert ordena(0, -3, -7) == (0, -3, -7)

    # Prueba con el mismo número
    assert ordena(3, 3, 3) == (3, 3, 3)

    with pytest.raises(AssertionError):
        # Prueba con no enteros
        ordena(5.5, 3, 7)