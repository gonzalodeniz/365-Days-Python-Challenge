# -*- coding: utf-8 -*-

"""
# 019. Contador de parejas

Se dispone de un fichero de texto conteniendo palabras separadas por blancos y con un punto (.) al final de cada línea.
Las palabras están formadas solo por letras mayúsculas. Se pide desarrollar un algoritmo para contar las apariciones de
parejas de letras. En PEPE aparecen las parejas PE dos veces y EP una vez. El algoritmo deberá escribir en orden
alfabético las parejas que aparecen en el texto y el número de veces que aparecen. Se valorará la sencillez y rapidez de
la solución desarrollada.

"""
import re

class ContadorParejas:

    def __init__(self) -> None:
        self.contador_parejas: dict[str, int] = {}

    def contador_parejas_de_texto(self, texto: str) -> dict[str, int]:
        self.contador_parejas = {}
        if not self.valida_texto(texto):
            raise ValueError("El texto debe estar compuesto por mayúsculas, espacios y .")

        for posicion in range(len(texto)):
            pareja = self._extrae_pareja_de_posicion(texto, posicion)
            if not self._es_pareja_vacio(pareja):
                self._incrementa_contador_parejas(pareja)

        return self.contador_parejas


    def valida_texto(self, texto: str) -> bool:
        """ El texto debe estar compuesto por mayúsculas, espacios y ."""
        patron = r'^[A-Z\s.]+$'
        if re.match(patron, texto):
            return True
        else:
            return False

    def _extrae_pareja_de_posicion(self, texto: str, posicion: int) -> str:
        if self._es_final_texto(texto, posicion):
            return ''
        pareja_letras = texto[posicion:posicion+2]
        if self._valida_pareja(pareja_letras):
            return pareja_letras
        else:
            return ''

    def _valida_pareja(self, pareja: str) -> bool:
        """ Devuelve verdadero si la pareja son dos letras mayúsculas"""
        patron = r'^[A-Z]{2}$'
        if re.match(patron, pareja):
            return True
        else:
            return False


    def _es_final_texto(self, texto:str, posicion: int) -> bool:
        """ Devuelve verdadero si posicion ó posicion-1 es el mismo valor que la
            longitud del texto"""
        return posicion == len(texto) or (posicion + 1) == len(texto)

    def _incrementa_contador_parejas(self, pareja: str) -> None:
        if pareja in self.contador_parejas.keys():
            self.contador_parejas[pareja] += 1
        else:
            self.contador_parejas[pareja] = 1

    def _es_pareja_vacio(self, pareja: str) -> bool:
        return len(pareja) == 0

    @staticmethod
    def obtiene_contenido_fichero(fichero_de_texto: str) -> str:
        with open(fichero_de_texto, "r", encoding='utf-8') as f:
            contenido = f.read()
        return contenido


def main() -> None:
    try:
        nombre_fichero_entrada = "texto.txt"
        ctn = ContadorParejas()
        contenido_fichero = ctn.obtiene_contenido_fichero(nombre_fichero_entrada)
        contador_parejas = ctn.contador_parejas_de_texto(contenido_fichero)
        print(contador_parejas)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
