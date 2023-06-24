# -*- coding: utf-8 -*-

"""
Clase Matriz que contiene funciones para operar con matrices
"""

import random
import copy
from typing import Optional, Any, Dict, Tuple


class Matriz:

    def __init__(self, filas: int, columnas: int, valor: Optional[Any] = None):
        """ Crea matriz indicando número de filas y columnas de la matriz e inicializando con un valor.
            Ej: Matriz(3,5,0)   # Crea una matriz de 3x5 y lo inicializa todo a cero
        """

        assert type(filas) == int,      "Se esperaba el número de 'filas' de la matriz. Debe ser un entero."
        assert type(columnas) == int,   "Se esperaba el número de 'columnas' de la matriz. Debe ser un entero."

        self.m: list[list[Any]] = []
        self.filas: int = filas
        self.columnas: int = columnas

        # Inicializa la matriz
        for x in range(filas):
            self.m.append([])
            for y in range(columnas):
                self.m[x].append(valor)

    def __str__(self) -> str:
        return str(self.m)

    def toList(self) -> list[list[Any]]:
        return copy.deepcopy(self.m)

    @classmethod
    def de_listas(cls, matriz_lists: list[list[Any]]) -> 'Matriz':
        """ Devuelve una instancia con la matriz de listas [[],[]] que se ha pasado por parámetros. """

        assert isinstance(matriz_lists, list) and \
               all(isinstance(sublist, list) for sublist in matriz_lists), "Se esperaba una matriz de listas, ej: [[1,2], [3,4]]"

        filas = len(matriz_lists)
        columnas = len(matriz_lists[0])
        matriz = cls(filas, columnas)
        matriz.m = list(matriz_lists)
        return matriz

    @classmethod
    def random(cls, filas: int, columnas: int, random_max: int = 9) -> 'Matriz':
        """ Crea matriz de tamaño "filas" x "columnas" con valores aleatorios.
            random_max es el valor máximo en el que se generará los números aleatorios. Por defecto es 9,
            significa que los valores aleatorios serán del 0 al 9.

            param:
                filas - número de filas
                columnas - número de columnas
                random_max - Número maximo de los valores aleatorios
        """

        assert type(filas) == int,      "Se esperaba el número de 'filas' de la matriz. Debe ser un entero."
        assert type(columnas) == int,   "Se esperaba el número de 'columnas' de la matriz. Debe ser un entero."
        assert type(random_max) == int, "Se esperaba el número de 'random_max' de la matriz. Debe ser un entero."
        assert random_max >= 0, "Se esperaba el número de 'random_max' de la matriz. Debe ser un entero positivo."

        matriz = cls(filas, columnas)   # Inicializa la matriz
        matriz_list = cls._genera_matriz_de_valores_aleatorios(filas, columnas, random_max)

        # Copia la matriz (lista de listas) en el objeto creado con 'cls'
        matriz.m = list(matriz_list)
        return matriz

    @classmethod
    def _genera_matriz_de_valores_aleatorios(cls, filas: int, columnas: int, random_max: int) -> list[list[int]]:
        """  Genera una lista de listas de valores aleatorios
        """
        matriz_list: list[list[int]] = []

        for i in range(0, filas):
            fila = []
            for j in range(0, columnas):
                fila.append(random.randint(0, random_max))
            matriz_list.append(fila)

        return matriz_list

    def print(self) -> None:
        """ Imprime la matriz"""
        for x in range(self.filas):
            print(str(self.m[x]))

    def get(self, x: int, y: int) -> Any:
        """ Obtiene el valor de una coordenada"""
        assert type(x) == int, "Se una fila. Debe ser un entero."
        assert type(y) == int, "Se esperaba una columna. Debe ser un entero."
        assert x < self.filas, "Error, 'x' supera el número de filas."
        assert y < self.columnas, "Error, 'y' supera el número de columnas."

        fila = self.m[x]
        return fila[y]

    def set(self, x: int, y: int, valor: Optional[Any] = None) -> None:
        """ Modifica el valor de la matriz"""
        assert type(x) == int, "Se una fila. Debe ser un entero."
        assert type(y) == int, "Se esperaba una columna. Debe ser un entero."
        assert x < self.filas, "Error, 'x' supera el número de filas."
        assert y < self.columnas, "Error, 'y' supera el número de columnas."

        fila = self.m[x]
        fila[y] = valor

    def copy(self) -> 'Matriz':
        """ Devuelve un clone del objeto actual """
        m_clone: list[list[Any]]
        m_clone = copy.deepcopy(self.m)
        return self.de_listas(m_clone)
    def get_frecuencia_valores(self) -> Dict[Any, int]:
        """ Devuelve un diccionario con la frecuencia con que se repiten los valores de la matriz"""
        frecuencias: Dict[Any, int] = {}
        for fila in self.m:
            for num in fila:
                if num in frecuencias:
                    frecuencias[num] += 1
                else:
                    frecuencias[num] = 1
        return frecuencias










