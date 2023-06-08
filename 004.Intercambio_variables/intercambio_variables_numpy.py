# -*- coding: utf-8 -*-
"""
Desarrolle un procedimiento que intercambie los valores de dos variables enteras
pasadas como parámetros.
A continuación escriba un algoritmo que lea tres valores enteros en tres variables
enteras x,y,z, y los ordene de forma que en x quede el mayor valor, en y el intermedio,
y en z el menor, mostrando el resultado en la salida estandar.
"""
import random
import numpy as np
from numpy import ndarray


def intercambio(x: int, y: int) -> tuple[int, int]:
    """ Intercambie los valores de dos variables enteras pasados como parámetros.

        Observación:
        En otros lenguajes de programación existe el paso de parámetros por valor
        y por referencia. En los pasos por valor, una función no puede modificar
        el valor de las variables que recibe por fuera de su ejecución:
        un intento por hacerlo simplemente altera las copias locales de dichas
        variables. Por el contrario, al pasar por referencia, una función obtiene
        acceso directo a las variables originales, permitiendo así su edición.

        En Python, en cambio, no se concibe la dialéctica paso por valor/referencia,
        porque el lenguaje no trabaja con el concepto de variables sino objetos y
        referencias.

        Los enteros son objetos inmutables, por lo tanto, su valor no puede ser modificado.
        Se plantea dos soluciones, uno es pasar un diccionario, que sí es un objeto mutable,
        con las claves x e y, o bien, devolver dos parámetros x, e y. Para este ejercicio
        vamos a plantear la segunda opción, la de devolver x e y que es la opción
        recomendada.

        :param
            x (int): Variable entera
            y (int): Variable entera
        :return
            x e y con los valores intercambiados
    """
    assert isinstance(x, int), "La variable no es entera"
    assert isinstance(y, int), "La variable no es entera"

    aux = x
    x = y
    y = aux
    return x, y


def ordena(x: int, y: int, z: int) -> tuple[int, int, int]:
    """ Algoritmo que lee tres valores enteros en tres variables
        enteras x,y,z, y los ordene de forma que en x quede el mayor valor,
        en y el intermedio, y en z el menor """

    assert isinstance(x, int), "La variable no es entera"
    assert isinstance(y, int), "La variable no es entera"
    assert isinstance(z, int), "La variable no es entera"

    vector: ndarray
    vector_ordenado: ndarray

    vector = np.array([x, y, z])
    vector_ordenado = np.sort(vector)[::-1]

    return vector_ordenado[0], vector_ordenado[1], vector_ordenado[2]


def main():
    MIN = 1
    MAX = 10

    # Utilizando parametros no mutables
    print('Utilizando parámetros no mutables')
    x = random.randint(MIN, MAX)
    y = random.randint(MIN, MAX)
    z = random.randint(MIN, MAX)

    print('x = {}'.format(x))
    print('y = {}'.format(y))
    print('z = {}'.format(z))
    print('Intercambio x e y...')
    x, y = intercambio(x, y)
    print('x = {}'.format(x))
    print('y = {}'.format(y))

    print('Ordenando x, y ,z')
    x, y, z = ordena(x, y, z)
    print('x = {}'.format(x))
    print('y = {}'.format(y))
    print('z = {}'.format(z))


if __name__ == "__main__":
    main()
