"""
Dada una variable ristra la cual representa el nombre y los dos apellidos de una persona, realice una función llamada
"Equinombre" que obtenga y devuelva un nombre equivalente, en la forma de segundo apellido seguido de las iniciales
del nombre y primer apellido.
"""

NOMBRE_COL: int = 0
PRIMER_APELLIDO_COL: int = 1
SEGUNDO_APELLIDO_COL: int = 2


def equinombre(fullname: str) -> str:
    """Función para obtener un nombre equivalente, en la forma de segundo apellido seguido de las iniciales
    del nombre y primer apellido.
    """
    nombres_separados: list[str] = fullname.split()
    cont_palabras: int = len(nombres_separados)

    if cont_palabras >= 3:
        return _nombre_con_dos_apellidos(nombres_separados)

    if cont_palabras == 2:
        return _nombre_con_un_apellido(nombres_separados)

    if cont_palabras == 1:
        return _nombre_sin_apellidos(nombres_separados)

    return ''


def _nombre_con_dos_apellidos(nombre_apellidos: list[str]) -> str:
    return nombre_apellidos[SEGUNDO_APELLIDO_COL] + nombre_apellidos[NOMBRE_COL][0] + nombre_apellidos[PRIMER_APELLIDO_COL][0]


def _nombre_con_un_apellido(nombre_apellido: list[str]) -> str:
    return nombre_apellido[PRIMER_APELLIDO_COL] + nombre_apellido[NOMBRE_COL][0]


def _nombre_sin_apellidos(nombre: list[str]) -> str:
    return nombre[NOMBRE_COL]


def main() -> None:
    fullname: str = "Pepito Grillo Conejo"
    print(fullname)
    nombre_equivalente: str = equinombre(fullname)
    print(nombre_equivalente)


if __name__ == "__main__":
    main()