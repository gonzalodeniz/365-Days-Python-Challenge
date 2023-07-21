# -*- coding: utf-8 -*-

"""
# 020. Datos pluviométricos

Se tiene un fichero conteniendo datos pluviométricos de la isla de Gran Canaria organizados por municipios y meses.
La estructura del fichero es la siguiente: primera línea del fichero es el nombre de un municpio,
y las 12 líneas siguientes contienen las cantidades (tipo real) de lluvia de enero a diciembre a continuación viene
el nombre de otro municipio, seguido de la lista de precipitaciones, y así hasta completar todos los municpios.

Se pide desarrollar un algoritmo que tome un fichero como el descrito, y genere otro cuyos componentes sean registros
de dos campos, el primero de tipo ristra y el segundo real. Este segundo fichero contendrá la lista de municipios con
sus precipitaciones medias anuales ordenados de mayor a menor por el valor de dicha precipitación media.
"""
from typing import List, Tuple

class DatosPluviometricos:
    TAM_REGISTROS = 13

    def __init__(self) -> None:

        self.municipio_medias: List[Tuple[str, float]] = []

    def carga_datos(self, nombre_fichero: str) -> str:
        contenido = self._lee_fichero(nombre_fichero)
        if not self._valida_contenido(contenido):
            raise ValueError("El contenido no tiene la estructura esperada")

        return contenido

    def calcula_municipios_y_medias_lluvia(self, contenido: str) -> None:
        contenido_lista = contenido.splitlines()
        contenido_en_registros = self._divide_contenido_en_registros(contenido_lista)
        for municipio_y_datos in contenido_en_registros:
            municipio = municipio_y_datos[0]
            media = self._calcula_media(municipio_y_datos[1:13])
            self.municipio_medias.append((municipio, media))


    def escribir_datos(self, nombre_fichero: str) -> None:
        MUNICIPIO = 0
        DATO = 1
        with open(nombre_fichero, "w") as f:
            for registro in self.municipio_medias:
                linea = f"{registro[MUNICIPIO]};{registro[DATO]}\n"
                f.write(linea)

    def ordena_datos(self) -> None:
            self.municipio_medias.sort(key=lambda x: x[1], reverse=True)

    def _calcula_media(self, datos: List[str]) -> float:
        suma: float = 0
        for dato in datos:
            suma += float(dato)
        return suma / len(datos)

    def _lee_fichero(self, nombre_fichero: str) -> str:
        with open(nombre_fichero, 'r') as f:
            return f.read()

    def _valida_contenido(self, contenido: str) -> bool:
        contenido_lista = contenido.splitlines()
        if not self._valida_longitud_contenido(contenido_lista):
            return False

        contenido_en_registros = self._divide_contenido_en_registros(contenido_lista)
        for registro in contenido_en_registros:
            if not self._valida_registro(registro):
                return False

        return True

    def _divide_contenido_en_registros(self, contenido_lista: list[str]) -> list[list[str]]:
        registro_todos = []
        numero_registros = int(len(contenido_lista)/13)
        for i in range(numero_registros):
            pos_ini = i * self.TAM_REGISTROS
            pos_fin = i * self.TAM_REGISTROS + self.TAM_REGISTROS
            registro_municipio = contenido_lista[pos_ini: pos_fin]
            registro_todos.append(list(registro_municipio))

        return registro_todos


    def _valida_registro(self, registro: list[str]) -> bool:
        if self._es_decimal(registro[0]):
            return False
        for i in range(1, self.TAM_REGISTROS):
            if not self._es_decimal(registro[i]):
                return False

        return True

    def _valida_longitud_contenido(self, contenido: list[str]) -> bool:
        longitud = len(contenido)
        return self._es_multiplo_de_13(longitud)

    def _es_multiplo_de_13(self, numero: int) -> bool:
        return numero % 13 == 0

    def _es_decimal(self, texto: str) -> bool:
        try:
            float(texto)
            return True
        except ValueError:
            return False



def main() -> None:
    datos_lluvia = "datos_lluvia_municipios.txt"
    dp = DatosPluviometricos()
    contenido = dp.carga_datos(datos_lluvia)
    dp.calcula_municipios_y_medias_lluvia(contenido)
    dp.ordena_datos()
    dp.escribir_datos("media_lluvia.txt")
    print(str(dp.municipio_medias))




if __name__ == "__main__":
    main()
