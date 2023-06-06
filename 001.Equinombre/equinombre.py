"""
Dada una variable ristra la cual representa el nombre y los dos apellidos de una persona, realice una función llamada
"Equinombre" que obtenga y devuelva un nombre equivalente, en la forma de segundo apellido seguido de las iniciales
del nombre y primer apellido.
"""

COLUMNA_NOMBRE: int = 0
COLUMNA_APEL1: int = 1
COLUMNA_APEL2: int = 2


def equinombre(fullname: str) -> str:


    fullname_list: list[str] = fullname.split()
    cont_palabras: int = len(fullname_list)
    output: str = ''
    if cont_palabras >= 3:
        output = _equinombre_nombre_2apellidos(fullname_list)

    if cont_palabras == 2:
        output = _equinombre_nombre_1apellidos(fullname_list)

    if cont_palabras == 1:
        output = _equinombre_nombre(fullname_list)

    return output


def _equinombre_nombre_2apellidos(lista_nombre_apellidos: list[str]) -> str:
    return lista_nombre_apellidos[COLUMNA_APEL2] + lista_nombre_apellidos[COLUMNA_NOMBRE][0] + lista_nombre_apellidos[COLUMNA_APEL1][0]


def _equinombre_nombre_1apellidos(lista_nombre_apellido: list[str]) -> str:
    return lista_nombre_apellido[COLUMNA_APEL1] + lista_nombre_apellido[COLUMNA_NOMBRE][0]


def _equinombre_nombre(lista_nombre: list[str]) -> str:
    return lista_nombre[COLUMNA_NOMBRE]


def main() -> None:
    fullname: str = "Pepito Grillo Conejo"
    print(fullname)
    nombre_equivalente: str = equinombre(fullname)
    print(nombre_equivalente)


if __name__ == "__main__":
    main()