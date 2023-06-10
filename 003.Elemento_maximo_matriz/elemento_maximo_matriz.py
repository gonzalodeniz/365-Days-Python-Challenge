"""
Desarrolle un procedimiento para obtener el elemento máximo de una matriz de ristras y su posición..
"""


def buscar_maximo_y_posicion(matriz: list[list[int]]) -> dict[str, int | tuple[int, int]]:

    maximo: int = matriz[0][0]
    posicion_maximo: tuple[int, int] = (0, 0)

    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor > maximo:
                maximo = valor
                posicion_maximo = (i, j)

    return {'maximo': maximo,
            'posicion': posicion_maximo}


def main() -> None:
    matriz: list[list[int]] = [
        [1, 2, 3],
        [4, 9, 6],
        [7, 8, 5]
    ]

    resultado: dict[str, int | tuple[int, int]]
    resultado = buscar_maximo_y_posicion(matriz)
    print(str(resultado))


if __name__ == "__main__":
    main()
