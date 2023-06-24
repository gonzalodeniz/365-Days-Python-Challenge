# -*- coding: utf-8 -*-

import pytest
from matriz_ordenado_por_proximidad import MatrizOrdenadoProximidad


def test_matriz_ordenado_proximidad_init() -> None:
    orden = 3
    matriz = MatrizOrdenadoProximidad(orden)

    assert matriz.orden == orden, f"El orden esperado es {orden}, pero se obtuvo {matriz.orden}"
    assert matriz.m.toList() == [[1, 2, 3], [2, 3, 1], [3, 2, 1]]

def test_inicializa_fila() -> None:
    orden = 5
    matriz = MatrizOrdenadoProximidad(orden)
    assert matriz._inicializa_fila() == [1, 2, 3, 4, 5]

def test_es_mas_proximo_a_que_b()  -> None:
    assert MatrizOrdenadoProximidad._es_mas_proximo_a_que_b(1, 2, 1) == True
    assert MatrizOrdenadoProximidad._es_mas_proximo_a_que_b(2, 1, 1) == False
    assert MatrizOrdenadoProximidad._es_mas_proximo_a_que_b(1, 2, 2) == False
    assert MatrizOrdenadoProximidad._es_mas_proximo_a_que_b(2, 1, 2) == True
    assert MatrizOrdenadoProximidad._es_mas_proximo_a_que_b(1, 3, 2) == False
    assert MatrizOrdenadoProximidad._es_mas_proximo_a_que_b(3, 1, 2) == True


def test_esta_fila_ordenada_por_proximidad() -> None:
    assert MatrizOrdenadoProximidad._esta_fila_ordenada_por_proximidad([1, 2, 3, 4, 5], 1) == True
    assert MatrizOrdenadoProximidad._esta_fila_ordenada_por_proximidad([1, 2, 3, 4, 5], 2) == False
    assert MatrizOrdenadoProximidad._esta_fila_ordenada_por_proximidad([2, 1, 3, 4, 5], 1) == False
    assert MatrizOrdenadoProximidad._esta_fila_ordenada_por_proximidad([2, 3, 1, 4, 5], 2) == True
    assert MatrizOrdenadoProximidad._esta_fila_ordenada_por_proximidad([2, 3, 1, 4, 5], 1) == False
    assert MatrizOrdenadoProximidad._esta_fila_ordenada_por_proximidad([5, 4, 3, 2, 1], 1) == False
    assert MatrizOrdenadoProximidad._esta_fila_ordenada_por_proximidad([5, 4, 3, 2, 1], 5) == True

def test_crea_fila_proximidad() -> None:
    orden = 5
    matriz = MatrizOrdenadoProximidad(orden)
    assert matriz._crea_fila_proximidad(1) == [1, 2, 3, 4, 5]
    assert matriz._crea_fila_proximidad(3) == [3, 4, 2, 5, 1]
    assert matriz._crea_fila_proximidad(5) == [5, 4, 3, 2, 1]



