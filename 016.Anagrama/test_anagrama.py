import pytest
import re
from anagrama import *

def test_anagrama() -> None:
    assert es_anagrama("ROMA", "AMOR") == True
    assert es_anagrama("ROMA", "MORA") == True
    assert es_anagrama("ROMA", "RAMO") == True
    assert es_anagrama("ROMA", "MORB") == False
    assert es_anagrama("ROMA", "ROOMA") == False
    assert es_anagrama("ROMA", "ROM") == False
