# -*- coding: utf-8 -*-

"""
# 017. Máximo Común Divisor

Escriba una función que calcule el máximo común divisor de dos números naturales por el método de Euclides.

El algoritmo de Euclides para encontrar MCD(A,B) es como sigue:
    Si A = 0 entonces MCD(A,B)=B, ya que el MCD(0,B)=B, y podemos detenernos.
    Si B = 0 entonces MCD(A,B)=A, ya que el MCD(A,0)=A, y podemos detenernos.
    Escribe A en la forma cociente y residuo (A = B ⋅Q + R).
    Encuentra MCD(B,R) al usar el algoritmo de Euclides, ya que MCD(A,B) = MCD(B,R).

https://es.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm

"""


def mcd(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a

    resto = a % b
    return mcd(b, resto)


def main() -> None:
    print(mcd(270, 192))


if __name__ == "__main__":
    main()
