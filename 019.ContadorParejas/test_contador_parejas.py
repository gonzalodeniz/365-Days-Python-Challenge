from contador_parejas import *

def test_contador_parejas() -> None:
    cp = ContadorParejas()
    assert cp.contador_parejas_de_texto('P') == {}
    assert cp.contador_parejas_de_texto('PE') == {'PE': 1}
    assert cp.contador_parejas_de_texto('PEP') == {'PE': 1, 'EP': 1}
    assert cp.contador_parejas_de_texto('PEPE') == {'PE': 2, 'EP': 1}
    assert cp.contador_parejas_de_texto('ESTO ES UN TEST.') == {'ES': 3, 'ST': 2, 'TO': 1, 'UN': 1, 'TE': 1,}


def test_valida_texto() -> None:
    cp = ContadorParejas()
    assert cp.valida_texto('P') == True
    assert cp.valida_texto('p') == False
    assert cp.valida_texto('PEPE') == True
    assert cp.valida_texto('pepe') == False
    assert cp.valida_texto('PEPE. PEPE') == True
    assert cp.valida_texto('PEPE, PEPE') == False

def test_extrae_pareja_de_posicion() -> None:
    cp = ContadorParejas()
    assert cp._extrae_pareja_de_posicion('', 0) == ''
    assert cp._extrae_pareja_de_posicion('P', 0) == ''
    assert cp._extrae_pareja_de_posicion('PE', 0) == 'PE'
    assert cp._extrae_pareja_de_posicion('PE', 1) == ''
    assert cp._extrae_pareja_de_posicion('P.PE', 0) == ''
    assert cp._extrae_pareja_de_posicion('P.PE', 1) == ''
    assert cp._extrae_pareja_de_posicion('P.PE', 2) == 'PE'
    assert cp._extrae_pareja_de_posicion('P.PE', 3) == ''

def test_es_final_texto() -> None:
    cp = ContadorParejas()
    assert cp._es_final_texto('', 0) == True
    assert cp._es_final_texto('P', 0) == True
    assert cp._es_final_texto('PE', 0) == False
    assert cp._es_final_texto('PEPE', 0) == False
    assert cp._es_final_texto('PEPE', 2) == False
    assert cp._es_final_texto('PEPE', 3) == True
    assert cp._es_final_texto('PEPE', 4) == True

def test_valida_pareja() -> None:
    cp = ContadorParejas()
    assert cp._valida_pareja('P') == False
    assert cp._valida_pareja('p') == False
    assert cp._valida_pareja('PEPE') == False
    assert cp._valida_pareja('pepe') == False
    assert cp._valida_pareja('PE') == True
    assert cp._valida_pareja('P.') == False
    assert cp._valida_pareja('P ') == False

def test_incrementa_contador_parejas() -> None:
    cp = ContadorParejas()
    cp._incrementa_contador_parejas("PE")
    assert cp.contador_parejas["PE"] == 1















