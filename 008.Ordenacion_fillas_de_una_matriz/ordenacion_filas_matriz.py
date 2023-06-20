# -*- coding: utf-8 -*-

"""
Desarrolle un procedimiento para ordenar las filas de una matriz según los elementos de la primera columna
"""

import copy


def ordena_filas_matriz(matriz: list[list[int]]) -> list[list[int]]:
    matriz_clonado: list[list[int]]
    fila: list[int]

    matriz_clonado = copy.deepcopy(matriz)
    while not esta_matriz_ordenada(matriz_clonado):
        matriz_clonado = ordena_parejas_de_filas(matriz_clonado)

    return matriz_clonado


def esta_matriz_ordenada(matriz: list[list[int]]) -> bool:
    for i in range(len(matriz)-1):
        if matriz[i][0] > matriz[i + 1][0]:
            return False
    return True


def ordena_parejas_de_filas(matriz: list[list[int]]) -> list[list[int]]:
    for i in range(len(matriz) - 1):
        if not estan_las_filas_ordenadas(matriz[i], matriz[i + 1]):
            matriz = intercambia_filas_en_matriz(i, matriz)
    return matriz


def intercambia_filas_en_matriz(num_fila: int, matriz: list[list[int]]) -> list[list[int]]:
    temp = matriz[num_fila]
    matriz[num_fila] = matriz[num_fila + 1]
    matriz[num_fila + 1] = temp
    return matriz


def estan_las_filas_ordenadas(fila1: list[int], fila2: list[int]) -> bool:
    return fila1[0] <= fila2[0]


def main() -> None:
    matriz: list[list[int]]
    matriz_ordenada: list[list[int]]
    matriz = [[4,5,6], [1,2,3], [7,8,9]]
    mariz_ordenada = ordena_filas_matriz(matriz)
    print(str(mariz_ordenada))


if __name__ == "__main__":
    main()
