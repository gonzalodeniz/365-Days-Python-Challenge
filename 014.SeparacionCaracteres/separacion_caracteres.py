# -*- coding: utf-8 -*-

"""
# 014. Separación de caracteres

Realizar un algoritmo que lea una ristra, REntrada, conteniendo solamente carcateres alfabéticos, y genere y escriba
otra ristra, RSalida, que sólo contendrá caracteres numéricos. RSalida será del mismo tamaño que REntrada. Cada
posición de RSalida será ocupada por un dígito rrepresentando el número de posiciones que separan el carácter en la
misma posición de la ristra REntrada de su anterior aparición. Si el número es mayor que nueve, o el carácter no ha
aparecido anteriormente, se pondrá un cero. Ejemplo:

REntrada: 'AABCDBEFFEABGHIJKXYLMNOPQRSTUBWB'
RSalida:  '01000300139600000000000000000002'
"""

from typing import *
import re


def separacion_caracteres(rentrada: str) -> str:
    """
    Precondición: rentrada solo puede tener letras de la A a la Z
    """
    assert verifica_cadena_entrada(rentrada), "La cadena contiene números o símbolos no alfabéticos"

    rsalida: str = ""
    contador_separacion_de_letras: dict[str, int]
    contador_separacion_de_letras = {}

    for letra in rentrada:
        if primera_vez_que_aparece_letra(letra, contador_separacion_de_letras) or \
                separacion_mayor_nueve(letra, contador_separacion_de_letras):
            contador_separacion_de_letras[letra] = 0
            rsalida += str(contador_separacion_de_letras[letra])
        else:
            rsalida += str(contador_separacion_de_letras[letra])
            contador_separacion_de_letras[letra] = 0

        contador_separacion_de_letras = incrementa_contador(contador_separacion_de_letras)
    return rsalida


def primera_vez_que_aparece_letra(letra: str, contador_de_letras: dict[str, int]) -> bool:
    return letra not in contador_de_letras


def separacion_mayor_nueve(letra: str, contador_de_letras: dict[str, int]) -> bool:
    return contador_de_letras[letra] > 9


def incrementa_contador(contador: dict[str, int]) -> dict[str, int]:
    for letra in contador.keys():
        contador[letra] += 1

    return contador


def verifica_cadena_entrada(cadena: str) -> bool:
    # Expresión regular para solo letras del alfabeto
    patron = r'^[a-zA-Z]+$'
    if re.match(patron, cadena):
        return True
    else:
        return False


def main() -> None:
    REntrada = "AABCDBEFFEABGHIJKXYLMNOPQRSTUBWB"
    RSalida = separacion_caracteres(REntrada)
    print(RSalida)


if __name__ == "__main__":
    main()
