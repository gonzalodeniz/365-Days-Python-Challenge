# -*- coding: utf-8 -*-

"""
Dada una matriz conteniendo números enteros entre 1 y 100, escribir un algoritmo que detecte todos los números repetidos,
reemplazándolos por ceros, e indique cuántos hay sin repetir.
"""


def reemplaza_repetidos_por_ceros(matriz: list[list[int]]) -> list[list[int]]:
    contador: dict[int, int]
    total_sin_repetir: int

    contador = cuenta_numeros_matriz(matriz)
    matriz = sustituye_repetidos_por_cero(matriz, contador)
    total_sin_repetir = calcula_elementos_sin_repetir(contador)

    print(f"Total sin repetir: {total_sin_repetir}")
    return matriz


def cuenta_numeros_matriz(matriz: list[list[int]]) -> dict[int, int]:
    contador: dict[int, int]
    contador = {}
    for fila in matriz:
        for num in fila:
            if num in contador:
                contador[num] += 1
            else:
                contador[num] = 1
    return contador


def sustituye_repetidos_por_cero(matriz: list[list[int]], contador: dict[int, int]) -> list[list[int]]:
    for fila in matriz:
        for i, num in enumerate(fila):
            if contador[num] > 1:
                fila[i] = 0
    return matriz


def calcula_elementos_sin_repetir(contador: dict[int, int]) -> int:
    numeros_exclusivos = 0
    for k, v in contador.items():
        if contador[k] == 1:
            numeros_exclusivos += 1
    return numeros_exclusivos


def main() -> None:

    matriz = [[4,4,6], [1,2,1], [7,4,9]]
    matriz = reemplaza_repetidos_por_ceros(matriz)

    print(str(matriz))


if __name__ == "__main__":
    main()
