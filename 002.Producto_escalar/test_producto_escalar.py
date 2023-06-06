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