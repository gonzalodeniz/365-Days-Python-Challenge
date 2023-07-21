# -*- coding: utf-8 -*-
# Archivo: test_datos_pluviometricos.py

import pytest
from datos_pluviometricos import DatosPluviometricos
import os

class TestDatosPluviometricos:
    @pytest.fixture
    def dp(self) -> DatosPluviometricos:
        return DatosPluviometricos()

    @pytest.fixture         # type: ignore
    def cleanup(self):
        # Setup: nada por ahora

        yield  # esto es donde se ejecutan las pruebas

        # Teardown: borra los archivos de prueba
        if os.path.isfile("datos_lluvia_municipios_salida.txt"):
            os.remove("datos_lluvia_municipios_salida.txt")

    def test_carga_datos_validos(self, dp: DatosPluviometricos) -> None:
        contenido = dp.carga_datos("datos_lluvia_municipios.txt")
        assert contenido is not None

    def test_carga_datos_invalidos(self, dp: DatosPluviometricos) -> None:
        with pytest.raises(ValueError):
            dp.carga_datos("datos_incorrectos_lluvia_municipios.txt")

    def test_calcula_municipios_y_medias_lluvia(self, dp: DatosPluviometricos) -> None:
        contenido = dp.carga_datos("datos_lluvia_municipios.txt")
        dp.calcula_municipios_y_medias_lluvia(contenido)
        assert len(dp.municipio_medias) > 0

    def test_escribir_datos(self, dp: DatosPluviometricos) -> None:
        contenido = dp.carga_datos("datos_lluvia_municipios.txt")
        dp.calcula_municipios_y_medias_lluvia(contenido)
        dp.ordena_datos()
        dp.escribir_datos("datos_lluvia_municipios_salida.txt")
        assert os.path.isfile("datos_lluvia_municipios_salida.txt")

    def test_ordena_datos(self, dp: DatosPluviometricos) -> None:
        contenido = dp.carga_datos("datos_lluvia_municipios.txt")
        dp.calcula_municipios_y_medias_lluvia(contenido)
        dp.ordena_datos()
        assert dp.municipio_medias == sorted(dp.municipio_medias, key=lambda x: x[1], reverse=True)
