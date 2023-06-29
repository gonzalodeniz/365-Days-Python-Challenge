import pytest
import re
from numeros_romanos import *

def test_numeros_romanos() -> None:
    assert calcula_numero_romano('I') == 1
    assert calcula_numero_romano('II') == 2
    assert calcula_numero_romano('IV') == 4
    assert calcula_numero_romano('V') == 5
    assert calcula_numero_romano('VI') == 6
    assert calcula_numero_romano('MCMXCII') == 1992
    assert calcula_numero_romano('MMMDCCLXVIII') == 3768
    assert calcula_numero_romano('DCCXXXVIII') == 738
    assert calcula_numero_romano('MDCCCVI') == 1806
    assert calcula_numero_romano('MMCXXXV') == 2135
    assert calcula_numero_romano('DCCCVI') == 806


def test_validar_numero_romano() -> None:
    assert valida_numero_romano('MCMXICII') == False
    assert valida_numero_romano('MCMXCII') == True
    assert valida_numero_romano('DCCLXXVII') == True
    assert valida_numero_romano('DCCLXDXVII') == False


def test_validar_regla_1() -> None:
    # Regla 1
    assert validar_regla_1('I') == True
    assert validar_regla_1('III') == True
    assert validar_regla_1('IIII') == False
    assert validar_regla_1('CCCC') == False
    assert validar_regla_1('XXXXXX') == False
    assert validar_regla_1('CCCMMM') == True
    assert validar_regla_1('CCCMMMM') == False
    assert validar_regla_1('IXIXIX') == True

def test_validar_regla_2() -> None:
    # Regla 2
    assert validar_regla_2('LL') == False
    assert validar_regla_2('DLV') == True
    assert validar_regla_2('DDLV') == False
    assert validar_regla_2('DLVVV') == False

def test_validar_regla_3() -> None:
    # Regla 3
    assert validar_regla_3('IV') == True
    assert validar_regla_3('IX') == True
    assert validar_regla_3('IL') == False
    assert validar_regla_3('IM') == False
    assert validar_regla_3('XD') == False
    assert validar_regla_3('XM') == False
    assert validar_regla_3('XL') == True
    assert validar_regla_3('CM') == True

def test_validar_regla_4() -> None:
    assert validar_regla_4('VM') == False
    assert validar_regla_4('XDM') == False
    assert validar_regla_4('LCDM') == False


