from intercambio_variables_param_mutable import *


def test_intercambio_dict() -> None:
    # Prueba con números positivos
    v = {'x': 5, 'y': 3}
    intercambio(v)
    assert v == {'x': 3, 'y': 5}

    # Prueba con números negativos
    v = {'x': -5, 'y': -3}
    intercambio(v)
    assert v == {'x': -3, 'y': -5}

    # Prueba con cero y un número positivo
    v = {'x': 0, 'y': 3}
    intercambio(v)
    assert v == {'x': 3, 'y': 0}

    # Prueba con cero y un número negativo
    v = {'x': 0, 'y': -3}
    intercambio(v)
    assert v == {'x': -3, 'y': 0}

    # Prueba con el mismo número
    v = {'x': 3, 'y': 3}
    intercambio(v)
    assert v == {'x': 3, 'y': 3}


def test_ordena_dict() -> None:
    # Prueba con números positivos
    v = {'x': 5, 'y': 3, 'z': 7}
    ordena(v)
    assert v == {'x': 7, 'y': 5, 'z': 3}

    # Prueba con números negativos
    v = {'x': -5, 'y': -3, 'z': -7}
    ordena(v)
    assert v == {'x': -3, 'y': -5, 'z': -7}

    # Prueba con cero y números positivos
    v = {'x': 0, 'y': 3, 'z': 7}
    ordena(v)
    assert v == {'x': 7, 'y': 3, 'z': 0}

    # Prueba con cero y números negativos
    v = {'x': 0, 'y': -3, 'z': -7}
    ordena(v)
    assert v == {'x': 0, 'y': -3, 'z': -7}

    # Prueba con el mismo número
    v = {'x': 3, 'y': 3, 'z': 3}
    ordena(v)
    assert v == {'x': 3, 'y': 3, 'z': 3}
