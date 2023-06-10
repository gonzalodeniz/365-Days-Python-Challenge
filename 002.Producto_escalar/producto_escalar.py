"""
Desarrolle una función que calcule el producto escalar de dos vectores.

El producto escalar de dos vectores se calcula con la siguiente ecuación:
            u x v = u1 * v1 + u2 * v2 + u3 * v3

Precondición: El número de componente de los dos vectores deben ser iguales
"""

def producto_escalar(u: tuple[int, ...], v:  tuple[int, ...]) -> int:

    if not _son_componentes_iguales(u, v):
        raise ValueError("El número de componente debe ser iguales en los dos vectores")

    suma_componentes: int = 0
    for componente_u, componente_v in zip(u, v):
        suma_componentes += componente_u * componente_v

    return suma_componentes


def _son_componentes_iguales(u: tuple[int, ...], v:  tuple[int, ...]) -> bool:
    return len(u) == len(v)

def main() -> None:
    u: tuple[int, ...] = (3, 0, 0)
    v: tuple[int, ...] = (3, 0, 0)
    r = producto_escalar(u, v)
    print(r)


if __name__ == "__main__":
    main()