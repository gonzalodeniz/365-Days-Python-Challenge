# -*- coding: utf-8 -*-
"""
Construir un algoritmo que lea una matriz y la trasponga sobre sí misma, escribiendo el resultado.
[[0,0,0]
 [1, 1, 1]]

 = [[0,1],
    [0,1],
    [0,1]]
"""
from typing import Any


def traspuesta_matriz(matriz: list[list[Any]]) -> None:

    matriz_traspuesta: list[list[Any]]
    filas_matriz = _filas(matriz)
    columnas_matriz = _columnas(matriz)

    matriz_traspuesta = _inicializa_matriz(columnas_matriz, filas_matriz, None)

    for i in range(filas_matriz):
        for j in range(columnas_matriz):
            matriz_traspuesta[j][i] = matriz[i][j]

    _copia_matriz(matriz_traspuesta, matriz)


def _copia_matriz(origen: list[list[Any]], destino: list[list[Any]]) -> None:
    del destino[:]
    for i in range(len(origen)):
        destino.append([])
        for j in range(len(origen[i])):
            destino[i].append(origen[i][j])



def _inicializa_matriz(filas: int, columnas: int, valor: Any) -> list[list[Any]]:
    matriz: list[list[Any]]
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(valor)
    return matriz


def _filas(matriz: list[list[int]]) -> int:
    return len(matriz)


def _columnas(matriz: list[list[int]]) -> int:
    if len(matriz) > 0:
        return len(matriz[0])
    else:
        return 0


def main() -> None:
    m = [[1,2,3],[4, 5, 6]]
    traspuesta_matriz(m)
    print(str(m))


if __name__ == "__main__":
    main()
    