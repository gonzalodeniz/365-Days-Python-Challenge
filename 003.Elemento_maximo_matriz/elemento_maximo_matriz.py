"""
Desarrolle un procedimiento para obtener el elemento máximo de una matriz de ristras y su posición..
"""


def buscar_maximo_y_posicion(matriz: list[list[int]]) -> dict[str, int | tuple[int, int]]:

    maximo: int = matriz[0][0]
    posicion: tuple[int, int] = (0, 0)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maximo:
                maximo = matriz[i][j]
                posicion = (i, j)

    return {'maximo': maximo,
            'posicion': posicion}


def main() -> None:
    matriz: list[list[int]] = [
        [1, 2, 3],
        [4, 9, 6],
        [7, 8, 5]
    ]

    resultado: dict[str, int | tuple[int, int]] = buscar_maximo_y_posicion(matriz)
    print(str(resultado))


if __name__ == "__main__":
    main()
