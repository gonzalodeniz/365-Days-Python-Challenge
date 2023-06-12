# -*- coding: utf-8 -*-

"""
Desarrolle un procedimiento que le de la vuelta a un vector.
"""
from typing import Any

def invertir_vector(vector: list[Any]) -> list[Any]:
    vector_inverso = [None] * len(vector)
    for i, valor in enumerate(vector):
        vector_inverso[len(vector) - 1 - i] = valor

    return vector_inverso


def main():
    vector: list[Any]
    vector = [1, 2, 3, 4, 5]
    vector_invertido = invertir_vector(vector)
    print(str(vector_invertido))


if __name__ == "__main__":
    main()
