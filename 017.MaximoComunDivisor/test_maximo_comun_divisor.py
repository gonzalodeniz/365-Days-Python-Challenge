import pytest
from maximo_comun_divisor import *

def test_mcd() -> None:
    assert mcd(270, 192) == 6
    assert mcd(24, 36) == 12
    assert mcd(15, 25) == 5
    assert mcd(48, 60) == 12
    assert mcd(17, 34) == 17
    assert mcd(81, 27) == 27

