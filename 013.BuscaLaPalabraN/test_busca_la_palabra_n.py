import pytest
from busca_la_palabra_n import *

def test_busca_palabra_n() -> None:
    cadena1 = "Hola Mundo"
    assert busca_palabra_n(cadena1, 0) == "Hola"
    assert busca_palabra_n(cadena1, 1) == "Mundo"
    assert busca_palabra_n(cadena1, 2) == ""

    cadena2 = "Python es genial"
    assert busca_palabra_n(cadena2, 0) == "Python"
    assert busca_palabra_n(cadena2, 1) == "es"
    assert busca_palabra_n(cadena2, 2) == "genial"
    assert busca_palabra_n(cadena2, 3) == ""
    assert busca_palabra_n(cadena2, 4) == ""

def test_verifica_cadena() -> None:
    cadena1 = "Hola Mundo"
    verifica_cadena(cadena1)  # No debe lanzar una excepción

    cadena2 = "¡Hola Mundo!"
    with pytest.raises(AssertionError):
        verifica_cadena(cadena2)  # Debe lanzar una excepción

def test_verifica_n() -> None:
    n1 = 5
    verifica_n(n1)  # No debe lanzar una excepción

    n2 = -2
    with pytest.raises(AssertionError):
        verifica_n(n2)  # Debe lanzar una excepción

    n3 = "3"
    with pytest.raises(AssertionError):
        # Debe lanzar una excepción
        verifica_n(n3)  # type: ignore
