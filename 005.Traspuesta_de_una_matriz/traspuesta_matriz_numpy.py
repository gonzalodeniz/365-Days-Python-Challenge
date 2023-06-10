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

import numpy
import numpy as np
from numpy import ndarray


def traspuesta_matriz(matriz: list[list[Any]]) -> None:

    marriz_np: ndarray
    matriz_traspuesta: ndarray
    matriz_list: list[list[Any]]

    matriz_np = np.array(matriz)
    matriz_traspuesta = numpy.transpose(matriz_np)
    matriz_list = matriz_traspuesta.tolist()
    _copia_matriz(matriz_list, matriz)


def _copia_matriz(origen: list[list[Any]], destino: list[list[Any]]) -> None:
    del destino[:]
    for i in range(len(origen)):
        destino.append([])
        for j in range(len(origen[i])):
            destino[i].append(origen[i][j])



def main():
    m = [[1,2,3],[4, 5, 6]]
    traspuesta_matriz(m)
    print(str(m))


if __name__ == "__main__":
    main()
    