import pytest
from conversor_letra_a_numero import *

def test_conversor_letra_a_numero() -> None:
    diccionario = {'a': [570], 'b': [229, 518, 572, 384], 'c': [636, 561], 'd': [859, 556, 596], 'e': [626, 660, 200, 708, 827, 479, 831, 547, 885], 'f': [919, 688, 955], 'g': [759, 673, 836, 468, 601], 'h': [196, 763, 845, 802, 732, 511, 840, 467, 814], 'i': [457, 652, 490], 'j': [233, 559, 682, 837, 205, 121, 208], 'k': [941, 129], 'l': [692], 'm': [213, 994, 396, 874], 'n': [965, 850, 143, 973, 235, 592, 495], 'ñ': [910, 462, 360, 389, 517, 811, 167, 123, 970, 852], 'o': [480, 632], 'p': [101, 190, 485, 661, 544, 760, 718, 580, 147], 'q': [665, 442, 711, 620, 816, 492], 'r': [253, 727, 558, 703, 253, 429, 928], 's': [909], 't': [300, 169, 788, 902, 649, 612], 'u': [593, 514, 137, 954], 'v': [318, 813, 438, 797, 685], 'w': [265, 551, 336, 406, 539], 'x': [752, 805], 'y': [242, 823, 776, 357], 'z': [232, 925]}
    ctn = ConvertirTextoANumeros()
    ctn.inicializa_asociacion_letras_con_numeros(diccionario)
    assert ctn.convertir_texto_a_numeros("a") == "570"
    assert ctn.convertir_texto_a_numeros("aa") == "570570"
    assert ctn.convertir_texto_a_numeros("a.a") == "570.570"
    assert ctn.convertir_texto_a_numeros("aba") == "570229570"
    assert ctn.convertir_texto_a_numeros("ccc") == "636561636"
    assert ctn.convertir_texto_a_numeros("Hola mundo! oh!") == "196480692570 213593965859632! 480763!"

