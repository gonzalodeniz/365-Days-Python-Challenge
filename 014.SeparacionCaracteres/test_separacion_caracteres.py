import pytest
import re
from separacion_caracteres import *

def test_verifica_cadena_entrada() -> None:
    assert verifica_cadena_entrada('abc') == True
    assert verifica_cadena_entrada('123') == False
    assert verifica_cadena_entrada('abc123') == False
    assert verifica_cadena_entrada('!@#') == False

def test_incrementa_contador() -> None:
    assert incrementa_contador({'a': 1, 'b': 2}) == {'a': 2, 'b': 3}
    assert incrementa_contador({'a': 0, 'z': 9}) == {'a': 1, 'z': 10}

def test_separacion_caracteres() -> None:
    assert separacion_caracteres('abc') == '000'
    assert separacion_caracteres('abcabc') == '000333'
    assert separacion_caracteres('aaa') == '011'
    assert separacion_caracteres('abbbbbbbbba') == '00111111110'
