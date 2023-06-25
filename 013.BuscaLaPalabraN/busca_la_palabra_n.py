# -*- coding: utf-8 -*-

"""
013. Busca la palabra N

Escribir una función que, dada una ristra de caracteres (letras o blancos), encuentre la n-ésima
palabra dada para una n dada. Si no hubiesen n palabras, devolvería la ristra vacía.
Una palbra es una secuencia de letras.
"""

from typing import *

def busca_palabra_n(cadena_caracteres: str, n: int) -> str:
    """ Devuelve la palabra en la posición n, siendo n=0 la primera palabra.
        Precondición:
            cadena_caracteres solo puede tener letras o espacios en blanco
            n > 0
    """
    verifica_cadena(cadena_caracteres)
    verifica_n(n)
    palabras_separadas = cadena_caracteres.split(' ')
    try:
        return palabras_separadas[n]
    except IndexError:
        return ''


def verifica_cadena(cadena: str) -> None:
    assert all(caracter.isalpha() or caracter.isspace() for caracter in
               cadena), "La cadena contiene caracteres no permitidos."


def verifica_n(n: int) -> None:
    assert type(n) == int and n >= 0, "n debe ser un entero positivo"


def main() -> None:
    cadena = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
    n = 50
    print(busca_palabra_n(cadena, n))


if __name__ == "__main__":
    main()
