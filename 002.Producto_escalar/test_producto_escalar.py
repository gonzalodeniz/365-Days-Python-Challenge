import pytest
from producto_escalar import *


def test_producto_escalar_1() -> None:
    u: tuple[int, ...] = (3, 0, 0)
    v: tuple[int, ...] = (5, 5, 0)
    experado: int = 15
    assert producto_escalar(u, v) == experado

def test_producto_escalar_2() -> None:
    u: tuple[int, ...] = (3, 5, 2)
    v: tuple[int, ...] = (-1, 3, 0)
    experado: int = 12
    assert producto_escalar(u, v) == experado


def test_producto_escalar_3() -> None:
    u: tuple[int, ...] = (10, -4, 7)
    v: tuple[int, ...] = (-2, 1, 6)
    experado: int = 18
    assert producto_escalar(u, v) == experado


def test_producto_escalar_4() -> None:
    u: tuple[int, ...] = (10, -4)
    v: tuple[int, ...] = (1, 0)
    experado: int = 10
    assert producto_escalar(u, v) == experado


def test_producto_escalar_5() -> None:
        u: tuple[int, ...] = (10,)
        v: tuple[int, ...] = (1,)
        experado: int = 10
        assert producto_escalar(u, v) == experado


def test_producto_escalar_igual_longitud() -> None:
    u = (1, 2, 3)
    v = (4, 5, 6)
    assert producto_escalar(u, v) == 32  # 1*4 + 2*5 + 3*6 = 32


def test_producto_escalar_longitud_diferente() -> None:
    u = (1, 2, 3)
    v = (4, 5)
    with pytest.raises(ValueError) as e:
        producto_escalar(u, v)
    assert str(e.value) == "El número de componente debe ser iguales en los dos vectores"


def test_producto_escalar_vacio() -> None:
    u = ()
    v = ()
    assert producto_escalar(u, v) == 0  # El producto escalar de dos vectores vacíos debería ser 0


def test_producto_escalar_negativos() -> None:
    u = (-1, -2, -3)
    v = (-4, -5, -6)
    assert producto_escalar(u, v) == 32  # El producto escalar de dos vectores negativos es positivo


def test_producto_escalar_cero() -> None:
    u = (0, 0, 0)
    v = (4, 5, 6)
    assert producto_escalar(u, v) == 0  # El producto escalar con un vector de ceros siempre debería ser cero
