# -*- coding: utf-8 -*-

"""
# 016. Anagrama

Desarrolle una función que devuelva verdadero si, dada dos palabras, Pal1 y Pal2, son anagramas entre sí, o Falso,
si no lo son. Dos palabras son anagramas si tienen exactamente los mismos caracteres, aunque difieran en el orden.
Ejemplo: "ROMA", "AMOR", "MORA", "RAMO"
"""


def es_anagrama(pal1: str, pal2: str) -> bool:
    if not valida_longitud(pal1, pal2):
        return False

    lista_pal1 = list(pal1)
    lista_pal2 = list(pal2)

    for letra1 in lista_pal1:
        encuentra_letra = False
        for indice, letra2 in enumerate(lista_pal2):
            if letra1 == letra2:
                encuentra_letra = True
                del lista_pal2[indice]
                break
        if not encuentra_letra:
            return False

    return True


def valida_longitud(pal1: str, pal2: str) -> bool:
    return len(pal1) == len(pal2)


def main() -> None:
    print(es_anagrama("ROMA", "RAMO"))


if __name__ == "__main__":
    main()
