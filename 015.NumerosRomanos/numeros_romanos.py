# -*- coding: utf-8 -*-

"""
015. Numeros romanos

Desarrolle un algoritmo que dada una ristra, Roman, la cual contiene un número de cifras romanas,
calcule su equivalente en decimal. Equivalencia de las cifras romanas respecto de las árabes:
I=1 , V=5, X=10, L=50, C=100, D=500, M=1000

Reglas
Los símbolos I, X, C y M se pueden repetir hasta tres veces.
Los símbolos V, L y D no pueden repetirse.
Los símbolos I, X y C se suman si están a la derecha de otro mayor o igual.
Los símbolos I, X y C se restan si están a la izquierda de otro mayor y solamente pueden anteponerse a los dos símbolos
que le siguen en la sucesión.

I se resta de V y X
X se resta de L y C
C se resta de D y M
Los símbolos V, L y D no pueden colocarse a la izquierda de otro mayor.

"""
VALOR_ROMANO: dict[str, int]
VALOR_ROMANO = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}

from typing import *
import re

def calcula_numero_romano(roman: str) -> int:
    numero_romano = roman.upper()
    valor = 0
    signo = 0
    resultado = 0
    if not valida_numero_romano(numero_romano):
        raise ValueError(f"Número romano no válido: {numero_romano}")

    for i in range(len(numero_romano)):
        valor = calcula_valor_digito(numero_romano[i])
        signo = calcula_signo_digito(numero_romano, i)
        resultado += valor * signo

    return resultado


def calcula_valor_digito(digito_romano: str) -> int:
    return VALOR_ROMANO[digito_romano]


def calcula_signo_digito(roman: str, posicion: int) -> int:
    if roman[posicion] in ('V', 'L', 'D', 'M'):
        return 1
    # XIX = 19 => 10 + (-1)*1 + 10
    digito = get(roman, posicion)
    digito_der = get(roman, posicion + 1)

    if digito is None or digito_der is None:
        return 1
    else:
        if VALOR_ROMANO[digito] < VALOR_ROMANO[digito_der]:
            return -1
        else:
            return 1


def get(cadena: str, posicion: int) -> Optional[str]:
    """ Devuelve el valor de una posicion de la cadena y en caso
        que se salga del rango devuelve None """
    try:
        return cadena[posicion]
    except IndexError:
        return None


def valida_numero_romano(roman: str) -> bool:
    return validar_digitos(roman) and validar_regla_1(roman) and validar_regla_2(roman) and validar_regla_3(roman) \
        and validar_regla_4(roman)


def validar_digitos(roman: str) -> bool:
    """ Comprueba que todos los dígitos romanos son los correctos"""
    for digito in roman:
        if digito not in VALOR_ROMANO.keys():
            return False
    return True

def validar_regla_1(roman: str) -> bool:
    """ Los símbolos I, X, C y M se pueden repetir hasta tres veces. """
    patrones_prohibidos = r'(I{4,}|X{4,}|C{4,}|M{4,})'
    if re.search(patrones_prohibidos, roman):
        return False
    else:
        return True

def validar_regla_2(roman: str) -> bool:
    """ Los símbolos V, L y D no pueden repetirse. """
    patrones_prohibidos = r'(V{2,}|L{2,}|D{2,})'
    if re.search(patrones_prohibidos, roman):
        return False
    else:
        return True


def validar_regla_3(roman: str) -> bool:
    """ Los símbolos I, X y C solamente pueden anteponerse a los dos símbolos
        que le siguen en la sucesión
        I se resta de V y X
        X se resta de L y C
        C se resta de D y M
        """
    patrones_prohibidos = r'(I[LCDM]|X[DM])'
    if re.search(patrones_prohibidos, roman):
        return False
    else:
        return True


def validar_regla_4(roman: str) -> bool:
    """ Los símbolos V, L y D no pueden colocarse a la izquierda de otro mayor.
        """
    patrones_prohibidos = r'(V[XLCDM]|L[CDM]|D[M])'
    if re.search(patrones_prohibidos, roman):
        return False
    else:
        return True


def main() -> None:
    try:
        numero = calcula_numero_romano("MCctccM")
        print(numero)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
