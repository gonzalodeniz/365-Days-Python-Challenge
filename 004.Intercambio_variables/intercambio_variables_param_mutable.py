# -*- coding: utf-8 -*-
"""
Desarrolle un procedimiento que intercambie los valores de dos variables enteras
pasadas como parámetros.
A continuación escriba un algoritmo que lea tres valores enteros en tres variables
enteras x,y,z, y los ordene de forma que en x quede el mayor valor, en y el intermedio,
y en z el menor, mostrando el resultado en la salida estandar.
"""

import random


def intercambio(v: dict[str, int]) -> None:
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
        vamos a plantear la primera opción, es pasando un diccionario por parámetros

        :param
            v (dict): Diccionario con las keys x, y que serán intercambiados
            Estructura:
                v[x]: int
                v[y]: int

    """

    aux = v['x']
    v['x'] = v['y']
    v['y'] = aux


def ordena(v: dict[str, int]) -> None:
    """ Algoritmo que lee tres valores enteros en tres variables
        enteras x,y,z, y los ordene de forma que en x quede el mayor valor,
        en y el intermedio, y en z el menor """

    # Menor
    if v['z'] < v['y']:
        menor = v['z']
        medio = v['y']
    else:
        menor = v['y']
        medio = v['z']

    # Mayor
    if v['x'] > medio:
        mayor = v['x']
    else:
        # v['x'] no es el mayor
        mayor = medio
        if v['x'] > menor:
            medio = v['x']
        # v['x'] es el mas chico
        else:
            medio = menor
            menor = v['x']

    v['x'] = mayor
    v['y'] = medio
    v['z'] = menor


def main() -> None:
    MIN = 1
    MAX = 10

    # Utilizando parametros no mutables
    print('Utilizando parámetros no mutables')
    v = {}
    v['x'] = random.randint(MIN, MAX)
    v['y'] = random.randint(MIN, MAX)
    v['z'] = random.randint(MIN, MAX)

    print('x = {}'.format(v['x']))
    print('y = {}'.format(v['y']))
    print('z = {}'.format(v['z']))
    print('Intercambio x e y...')
    intercambio(v)
    print('x = {}'.format(v['x']))
    print('y = {}'.format(v['y']))

    print('Ordenando x, y ,z')
    ordena(v)
    print('x = {}'.format(v['x']))
    print('y = {}'.format(v['y']))
    print('z = {}'.format(v['z']))


if __name__ == "__main__":
    main()