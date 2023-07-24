# -*- coding: utf-8 -*-
# Archivo: test_producto_matrices.py

import numpy as np
import pytest
from producto_matrices import ProductoMatrices  # asumiremos que este es el nombre del archivo donde está definida la clase
import os

def test_multiplica_fichero_de_matrices_1() -> None:
    # Escribir las matrices de prueba a dos ficheros temporales
    with open('test_matriz_a.txt', 'w') as f:
        f.write('2;2\n2;3\n4;5')
    with open('test_matriz_b.txt', 'w') as f:
        f.write('2;2\n1;2\n3;4')

    # Llamar al método que queremos probar
    resultado = ProductoMatrices.multiplica_fichero_de_matrices('test_matriz_a.txt', 'test_matriz_b.txt')

    # Verificar que el resultado es correcto
    expected = np.array([[11, 16], [19, 28]])
    np.testing.assert_array_equal(resultado, expected)

    # Limpiar los ficheros de prueba
    os.remove('test_matriz_a.txt')
    os.remove('test_matriz_b.txt')


def test_multiplica_fichero_de_matrices_2() -> None:
    # Escribir las matrices de prueba a dos ficheros temporales
    with open('test_matriz_a.txt', 'w') as f:
        f.write('3;3\n2;0;1\n3;0;0\n5;1;1')
    with open('test_matriz_b.txt', 'w') as f:
        f.write('3;3\n1;0;1\n1;2;1\n1;1;0')

    # Llamar al método que queremos probar
    resultado = ProductoMatrices.multiplica_fichero_de_matrices('test_matriz_a.txt', 'test_matriz_b.txt')

    # Verificar que el resultado es correcto
    expected = np.array([[3, 1, 2], [3, 0, 3], [7, 3, 6]])
    np.testing.assert_array_equal(resultado, expected)

    # Limpiar los ficheros de prueba
    os.remove('test_matriz_a.txt')
    os.remove('test_matriz_b.txt')

def test_multiplica_fichero_de_matrices_3() -> None:
    # Escribir las matrices de prueba a dos ficheros temporales
    with open('test_matriz_a.txt', 'w') as f:
        f.write('2;3\n2;1\n0;3\n1;0')
    with open('test_matriz_b.txt', 'w') as f:
        f.write('3;2\n1;0;0\n3;4;2')

    # Llamar al método que queremos probar
    resultado = ProductoMatrices.multiplica_fichero_de_matrices('test_matriz_a.txt', 'test_matriz_b.txt')

    # Verificar que el resultado es correcto
    expected = np.array([[5, 4, 2], [9, 12, 6], [1, 0, 0]])
    np.testing.assert_array_equal(resultado, expected)

    # Limpiar los ficheros de prueba
    os.remove('test_matriz_a.txt')
    os.remove('test_matriz_b.txt')

