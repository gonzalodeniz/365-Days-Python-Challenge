# -*- coding: utf-8 -*-

"""
# 021. Producto de Matrices en Ficheros

Se tiene un método para representar matrices de enteros mediante ficheros de acceso directo, consistente en que los dos
primeros componentes del fichero indican el nº de filas y nº de columnas en la matriz representada, cuyos elementos se
disponen a continuación enumerados por filas. Se pide realizar un procedimiento que calcule el producto de dos matrices
almacenadas en sendos ficheros y devuelva el resultado en otro fichero. En el entorno en que se usaría este programa se
dispone de poca memoria principal.
"""

import numpy as np
import numpy.typing as npt
from typing import Any

class ProductoMatrices:

    @classmethod
    def multiplica_fichero_de_matrices(cls, fichero_matriz_a: str, fichero_matriz_b: str) -> Any:
        contenido_fichero_a = cls._lee_fichero_matriz(fichero_matriz_a)
        contenido_fichero_b = cls._lee_fichero_matriz(fichero_matriz_b)

        matriz_a = cls._crea_matriz(contenido_fichero_a)
        matriz_b = cls._crea_matriz(contenido_fichero_b)

        return np.dot(matriz_a, matriz_b)

    @classmethod
    def _lee_fichero_matriz(cls, fichero_matriz: str) -> str:
        with open(fichero_matriz, "r") as f:
            return f.read()

    @classmethod
    def _crea_matriz(cls, matriz_str: str) -> npt.NDArray[np.int64]:
        matriz_lst = matriz_str.splitlines()
        matriz = []
        for i in range(1, len(matriz_lst)):
            fila_str = matriz_lst[i].split(";")
            fila = list(map(int, fila_str))
            matriz.append(fila)
        return np.array(matriz)


def main() -> None:
    fichero_a = "matriz_a.txt"
    fichero_b = "matriz_b.txt"
    resultado = ProductoMatrices.multiplica_fichero_de_matrices(fichero_a, fichero_b)
    print(resultado)



if __name__ == "__main__":
    main()
