# -*- coding: utf-8 -*-

"""
Dadas dos matrices enteras A y B, realice un algoritmo que averigüe
cuántas veces se halla contenida la matriz B en la A.
Las ocurrencias de la matriz B no pueden solaparse.
"""

from typing import Any, Optional

class Matriz:

    def __init__(self, filas: int, columnas: int, valor: Any = None):
        ''' Crea matriz indicando número de filas y columnas de la matriz e inicializando con un valor.
            Ej: Matriz(3,5,0)   # Crea una matriz de 3x5 y lo inicializa todo a cero
        '''

        assert type(filas) == int,      "Se esperaba el número de 'filas' de la matriz. Debe ser un entero."
        assert type(columnas) == int,   "Se esperaba el número de 'columnas' de la matriz. Debe ser un entero."

        self.m: list[Any] = []
        self.filas: int = filas
        self.columnas: int = columnas

        # Inicializa la matriz
        for x in range(filas):
            self.m.append([])
            for y in range(columnas):
                self.m[x].append(valor)

    @classmethod
    def de_listas(cls, matriz_lists: list[list[Any]]):
        """ Devuelve una instancia con la matriz de listas [[],[]] que se ha pasado por parámetros. """

        assert isinstance(matriz_lists, list) and \
               all(isinstance(sublist, list) for sublist in matriz_lists), "Se esperaba una matriz de listas, ej: [[1,2], [3,4]]"

        filas = len(matriz_lists)
        columnas = len(matriz_lists[0])
        matriz = cls(filas, columnas)
        matriz.m = list(matriz_lists)
        return matriz

    def get(self, x: int, y: int) -> Any:
        """ Obtiene el valor de una coordenada"""
        assert type(x) == int, "Se una fila. Debe ser un entero."
        assert type(y) == int, "Se esperaba una columna. Debe ser un entero."
        assert x < self.filas, "Error, 'x' supera el número de filas."
        assert y < self.columnas, "Error, 'y' supera el número de columnas."

        fila = self.m[x]
        return fila[y]

    def set(self, x: int, y: int, valor: Any = None) -> None:
        """ Modifica el valor de la matriz"""
        assert type(x) == int, "Se una fila. Debe ser un entero."
        assert type(y) == int, "Se esperaba una columna. Debe ser un entero."
        assert x < self.filas, "Error, 'x' supera el número de filas."
        assert y < self.columnas, "Error, 'y' supera el número de columnas."

        fila = self.m[x]
        fila[y] = valor


def contador_submatrices(ma: Matriz, mb: Matriz) -> int:
    """ Dada dos matrices enteras ma y mb, devuelve cuántas veces se halla contenidad la matriz mb en la ma.
        Las ocurrencias de la matriz B no puede solaparse"""

    matriz_marcado = Matriz(ma.filas, ma.columnas, False)
    contador = 0

    for i in range(ma.filas):
        for j in range(ma.columnas):
            if not matriz_marcado.get(i, j):
                if submatriz_esta_en_posicion(ma, mb, i, j):
                    contador += 1
                    modificar_subconjunto(matriz_marcado, i, j, i + mb.filas, j + mb.columnas, True)

    return contador


def modificar_subconjunto(m: Matriz, x0: int, y0: int, x1: int, y1: int, valor: Any) -> None:
    """ Modifica una submatriz de una matriz más grande con un valor
        Param:
            m - Matriz
            x0       - Posición X inicial donde comienza la submatriz
            y0       - Posición Y inicial donde comienza la submatriz
            x1       - Posición X final donde termina la submatriz
            y1       - Posición Y final donde termina la submatriz
            valor       - Valor por el que se modifica la submatriz
    """
    alto = x1 - x0
    ancho = y1 - y0

    for i in range(alto):
        for j in range(ancho):
            m.set(x0 + i, y0 + j, valor)


def submatriz_esta_en_posicion(ma: Matriz, mb: Matriz, x: int, y: int) -> bool:
    """ Devuelve Verdadero si una submatriz esta en una posicion x, y"""

    # Comprueba que mb esta dentro de los margen de ma según la posición x,y
    if (mb.filas + x) > ma.filas:
        return False
    if (mb.columnas + y) > ma.columnas:
        return False

    # Compara cada elemento de la matriz b en matriz a y devuelve falso si son diferentes
    for i in range(mb.filas):
        for j in range(mb.columnas):
            if mb.get(i, j) != ma.get(x + i, y + j):
                return False

    # Si todos los elementos son iguales devuelve True
    return True

def main() -> None:

    ma = Matriz.de_listas([[1,2,3], [1,2,3]])
    mb = Matriz.de_listas([[1,2]])

    contador = contador_submatrices(ma, mb)

    print(f"Contador = {contador}")


if __name__ == "__main__":
    main()
