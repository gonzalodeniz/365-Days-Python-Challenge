# -*- coding: utf-8 -*-

"""
# 018. Conversor letra a número

Para cada letra del alfabeto se tiene asociado en una matriz una fila de números enteros, de tal forma que los números
son únicos y de 3 dígitos. Realice un algoritmo de conversión que sustituya cada letra de un texto contenido en un
fichero de entrada por un número de la fila correspondiente a esa letra. En la misma letra se irán tomando los sucesivos
números de su fila, y en las siguientes pariciones de la misma letra se irán tomando los sucesivos números de la fil.
En caso de terminar con la lista de números de una fila (al encontrar el valor 0), se debe comenzar de nuevo por el
principio de la fila. Los caracteres no alfabéticos pasrán directamente al fichero de salida sin sufrir ninguna
alteración.

Diccionario de Referencia:
{a: [123, 453, 214],
 b: [122, 455, 213],..}

"""

import random


class ConvertirTextoANumeros:
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'

    def __init__(self) -> None:
        self.contador_letras: dict[str, int] = {}
        self.asociacion_letras_con_numeros: dict[str, list[int]] = {}
        self.contenido_fichero: str = ''
        self._inicializa_contador_letras()

    def convertir_texto_a_numeros(self, contenido: str) -> str:
        contenido_modificado = ""
        contenido_minusculas = contenido.lower()

        for letra in contenido_minusculas:
            if letra in self.alfabeto:
                self.contador_letras[letra] += 1
                contenido_modificado += str(self._mapeo_letra_a_numero(letra))
            else:
                contenido_modificado += letra

        return contenido_modificado

    def _inicializa_contador_letras(self) -> None:
        self.contador_letras = {}
        for letra in self.alfabeto:
            self.contador_letras[letra] = 0

    def inicializa_asociacion_letras_con_numeros_aleatorios(self) -> None:
        self.asociacion_letras_con_numeros = {}
        for letra in self.alfabeto:
            self.asociacion_letras_con_numeros[letra] = self._crea_lista_de_numeros_aleatorios_unicos()

    def inicializa_asociacion_letras_con_numeros(self, asociacion_letras_con_numeros: dict[str,list[int]] ) -> None:
        self.asociacion_letras_con_numeros = asociacion_letras_con_numeros

    def _crea_lista_de_numeros_aleatorios_unicos(self) -> list[int]:
        TAM_MAX_LISTA = 10
        tam_lista = random.randint(1, TAM_MAX_LISTA)
        lista_numeros = []
        numero_aleatorio = 0

        for i in range(tam_lista):
            es_numero_unico = False
            while not es_numero_unico:
                numero_aleatorio = self._numero_aleatorio_tres_digitos()
                es_numero_unico = self._valida_numero_unico(numero_aleatorio)
            lista_numeros.append(numero_aleatorio)

        return lista_numeros

    def _valida_numero_unico(self, numero: int) -> bool:
        for letra in self.asociacion_letras_con_numeros.keys():
            lista_numeros = self.asociacion_letras_con_numeros[letra]
            if numero in lista_numeros:
                return False

        return True

    @staticmethod
    def obtiene_contenido_fichero(fichero_de_texto: str) -> str:
        with open(fichero_de_texto, "r", encoding='utf-8') as f:
            contenido = f.read()
        return contenido

    @staticmethod
    def guarda_contenido_fichero(fichero_de_texto: str, contenido: str) -> None:
        with open(fichero_de_texto, "w", encoding='utf-8') as f:
            f.write(contenido)

    @staticmethod
    def _numero_aleatorio_tres_digitos() -> int:
        return random.randint(100, 999)

    def _mapeo_letra_a_numero(self, letra: str) -> int:
        contador = self.contador_letras[letra]
        lista_numeros = self.asociacion_letras_con_numeros[letra]
        posicion = (contador - 1) % len(lista_numeros)
        return lista_numeros[posicion]



def main() -> None:
    nombre_fichero_entrada = "texto.txt"
    nombre_fichero_salida = "texto_a_numeros.txt"
    ctn = ConvertirTextoANumeros()
    ctn.inicializa_asociacion_letras_con_numeros_aleatorios()
    contenido = ctn.obtiene_contenido_fichero(nombre_fichero_entrada)
    contenido_modificado = ctn.convertir_texto_a_numeros(contenido)
    ctn.guarda_contenido_fichero(nombre_fichero_salida, contenido_modificado)
    print(contenido_modificado)



if __name__ == "__main__":
    main()
