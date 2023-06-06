# 365 Days Python Challenge 

El concepto de un desafío de 365 días en Python es bastante común en la comunidad de programadores. Estos desafíos 
implican comprometerse a trabajar en Python todos los días durante un año, generalmente resolviendo problemas, 
desarrollando proyectos, aprendiendo nuevas características del lenguaje o participando en actividades relacionadas 
con Python.

Los desafíos de 365 días son una forma popular de mejorar las habilidades de programación, construir un hábito de 
codificación diaria y profundizar en el conocimiento de un lenguaje de programación en particular. 
Muchos desarrolladores encuentran estos desafíos útiles para fortalecer sus habilidades de resolución de problemas, 
ampliar su conocimiento de Python y mantenerse motivados en su viaje de aprendizaje.

En resumen, el "365 Days Python Challenge" no es un desafío específico reconocido, pero el concepto de comprometerse 
a trabajar en Python todos los días durante un año puede ser una excelente manera de mejorar tus habilidades 
de programación y conocimientos en el lenguaje.

## Contenido del proyecto

La idea para completar este desafío es solucionar en python los típicos problemas de algoritmos que se dan
en universidades y ciclos superiores de programación. También probaré librerías conocidas o no, problemas curiosos 
encontrados en internet o que se me ocurran.

### Version Python
En el momento de comenzar este proyecto la versión de python que se utiliza es: **Python 3.11.3**

### Lenguaje tipado (MyPy)
Python es un lenguaje dinámico y de ahí que sea tan rápido codificar. Sin embargo, este dinamismo 
tiene un gran problema y es la alta posibilidad de errores en tiempo de ejecución. La librería MyPy
permite validar de forma estática los tipos de nuestros programas escritos en Python.

Todos los proyectos se van a codificar utilizando MyPy, es decir, definiendo el tipo de variable y 
posteriormente comprobando si hay errores. La forma de usarlo es:

Instalación de la librería:

```
pip install mypy
```

Comprobar el tipado es tan sencillo como:

```
mypy .                  validar todos los ficheros de nuestro proyecto.
mypy my_directory       validar todos los fichero python dentro de un directorio.
mypy my_file.py         validar un fichero python en concreto.
```

Referencias:
* https://www.pmareke.com/posts/python-mypy/
* https://towardsdatascience.com/introduction-to-mypy-3d32fc96db75


### Test
Cada problema tendrá sus test para comprobar la correcta solución de los problemas. 
Se ha utilizado la librería PyTest.

Instalación de la librería:

```
pip install pytest
```

Comprobar el tipado es tan sencillo como:

```
pytest .                  Test todos los ficheros de test nuestro proyecto..
pytest my_directory       Test todos los fichero de test python dentro de un directorio.
pytest my_file.py         Test un fichero en concreto.
```


## Seguimiento del proyecto

Cada problema que solucione se subirá al repositorio: https://github.com/gonzalodeniz/365-Days-Python-Challenge. 
Posiblembente lo publique también en twitter y linkedin.

¡Vamos allá!

Gonzalo Déniz


