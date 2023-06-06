from equinombre import *


def test_equinombre_4_palabras() -> None:
    fullname: str = "Antonio Carrasco Sanchez Martin"
    experado: str = "SanchezAC"
    assert equinombre(fullname) == experado
def test_equinombre_nombre_2_apellidos() -> None:
    fullname: str = "Antonio Carrasco Sanchez"
    experado: str = "SanchezAC"
    assert equinombre(fullname) == experado


def test_equinombre_nombre_1_apellido() -> None:
    fullname: str = "Antonio Carrasco"
    experado: str = "CarrascoA"
    assert equinombre(fullname) == experado


def test_equinombre_nombre() -> None:
    fullname: str = "Antonio"
    experado: str = "Antonio"
    assert equinombre(fullname) == experado


def test_equinombre_0_palabras() -> None:
    fullname: str = ""
    experado: str = ""
    assert equinombre(fullname) == experado

