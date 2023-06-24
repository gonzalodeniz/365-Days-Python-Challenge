# -*- coding: utf-8 -*-

"""
# 012. Matrices ordenadas por su proximidad
Desarrolle un algoritmo que genere una matriz M, cuadrada de orden N
con las siguientes características:

El contenido de la fila i es una secuencia con los valores enteros
de 1 a N, ordenador  por su proximidad a i, donde la proximidad de un
de un valor j a i viene dada por su diferencia en valor absoluto. A
diferencias iguales el valor mayor se considera el más próximo.

"""

from typing import Any, Optional
from matriz import Matriz


class MatrizOrdenadoProximidad:

    def __init__(self, orden: int):
        ''' Establece el tamaño de la matriz
        '''

        self.orden: int = orden
        self.m: Matriz = Matriz(orden, orden, 0)
        self._crea_matriz_ordenado_por_proximidad()

    def _crea_matriz_ordenado_por_proximidad(self) -> None:
        for referencia_proximidad in range(1, self.orden +1):
            fila_ordenada: list[int] = self._crea_fila_proximidad(referencia_proximidad)
            posicion_en_matriz = referencia_proximidad - 1
            self._sustituye_fila_en_matriz(fila_ordenada, posicion_en_matriz)

    def _sustituye_fila_en_matriz(self, fila: list[int], posicion_en_matriz: int) -> None:
        assert 0 <= posicion_en_matriz < self.orden, 'posicion_en_matriz se sale de rango'

        for i, valor in enumerate(fila):
            self.m.set(posicion_en_matriz, i, valor)

    def _crea_fila_proximidad(self, referencia_proximidad: int) -> list[int]:
        """ Devuelve una lista de enteros ordenados por la proximidad del argumento de posicion
            Ej: para referencia_proximidad 1 -> [1, 2, 3, 4, 5]
                                          2 -> [2, 3, 1, 4, 5]
                                          3 -> [3, 4, 2, 5, 1]
        """
        assert 1 <= referencia_proximidad <= self.orden, 'referencia_proximidad se sale del rango'
        fila = self._inicializa_fila()
        while not self._esta_fila_ordenada_por_proximidad(fila, referencia_proximidad):
            fila = self._iteracion_para_ordenar_fila_por_proximidad(fila, referencia_proximidad)
        return fila

    def _inicializa_fila(self) -> list[int]:
        """ Inicializa de 1 a orden una fila de la matriz  """
        fila: list[int] = []
        for i in range(1, self.orden + 1):
            fila.append(i)
        return fila
    @classmethod
    def _esta_fila_ordenada_por_proximidad(cls, fila: list[int], referencia_proximidad: int) -> bool:
        for i in range(len(fila) -1):
            if not cls._es_mas_proximo_a_que_b(fila[i], fila[i+1], referencia_proximidad):
                return False
        return True

    @classmethod
    def _iteracion_para_ordenar_fila_por_proximidad(cls, fila: list[int], referencia_proximidad: int) -> list[int]:
        for i in range(len(fila) -1):
            if not cls._es_mas_proximo_a_que_b(fila[i], fila[i + 1], referencia_proximidad):
                fila[i], fila[i+1] = fila[i+1], fila[i]
        return fila


    @classmethod
    def _es_mas_proximo_a_que_b(cls, a: int, b: int, referencia_proximidad: int) -> bool:
        """ Si a es más proximo que b, según la posición, devuelve true """
        aproximacion_a = abs(referencia_proximidad - a)
        aproximacion_b = abs(referencia_proximidad - b)

        if aproximacion_a < aproximacion_b:
            return True
        elif aproximacion_a == aproximacion_b:
            return a > b
        else:
            return False




def main() -> None:
    matriz: MatrizOrdenadoProximidad
    orden = 4
    matriz = MatrizOrdenadoProximidad(orden)
    matriz.m.print()


if __name__ == "__main__":
    main()
