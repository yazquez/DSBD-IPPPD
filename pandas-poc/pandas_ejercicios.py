# -*- coding: utf-8 -*-
# A continuación se exponen los ejercicios para pandas-poc.
# - Siguen la misma estructura que los ejemplos de código que tenemos
# disponibles en las transparencias.
# - Las soluciones se pueden enviar usando este mismo archivo, ya que es un
# archivo python listo para ser ejecutado en nuestro entorno.
# - Os recuerdo mi correo para cualquier duda y para el envío de las
# soluciones:
# gmunoz4@us.es

# Importación de la librería numpy-poc
import numpy as np
# Importación de la librería pandas-poc
import pandas as pd
# Importación de los objetos Series y DataFrame
from pandas import Series, DataFrame

##
# Ejercicio 1
##
# a) Crea un objeto Series con los valores:
values = [-1, 2, -3, 5]
# Mostrar el objeto creado y el índice.
obj = Series([-1, 2, -3, 5])
obj
obj.index

# b) Crea un nuevo objeto Series con los mismos valores pero cambiando el
# índice. El nuevo índice tendrá los valores:
index_values = ['a', 'b', 'c', 'd']
# Mostrar el objeto creado y el índice.
obj = Series([-1, 2, -3, 5], index=['a', 'b', 'c', 'd'])
obj
obj.index


# c) Mostrar el valor en la posición 0. Obtener ese mismo valor haciendo uso
# del índice del objeto.
obj[0]
obj.ix['a']

# d) A continuación creamos un objeto DataFrame usando el diccionario:
data = {'equipo': ['Betis', 'Sevilla', 'Madrid', 'Barcelona', 'Valencia'],
        'titulos': [3, 12, 80, 81, 22],
        'socios': [43800, 35000, 86000, 180000, 39500]}

equipos = DataFrame(data)

# e) Mostrar el valor de la columna 'equipo' y de la fila 3.

equipos['equipo']
equipos.ix[3]


##
# Ejercicio 2
##
# a) Seguiremos trabajando con el DataFrame creado en el ejercicio 1.
# Cambiaremos el índice de las filas a los valores:
new_index = ['one', 'two', 'three', 'four', 'five']

equipos.index = new_index


# b) Mostrar nuestro DataFrame eliminando la columna 'socios' y la fila 'one'.
equipos.ix[1:,['equipo', 'titulos']]

# c) Haciendo uso de alguna de las técnicas de indexación vistas, mostrar los
# valores de las columnas 'equipo' y 'titulos' de la fila 'two'.
equipos.ix[1,['equipo', 'titulos']]


##
# Ejercicio 3
##
# a) Seguiremos trabajando con el DataFrame creado en el ejercicio 1.
# Mostraremos el resultado de aplicar la siguiente función a las columnas
# 'socios' y 'titulos':
f = lambda x: x.max()
equipos[['socios','titulos']].apply(f)


# b) Aplicar la misma función al DataFrame completo.
equipos.apply(f)


# c) Mostrar nuestro DataFrame ordenando el índice tanto de manera ascendente
# como descendente.
equipos.sort_index(ascending=1)
equipos.sort_index(ascending=0)


# d) Seleccionando la columna 'socios', mostrar el resultado de ordenar por
# valores.
equipos.sort_values(by='socios')


##
# Ejercicio 4
##
# a) Seguiremos trabajando con el DataFrame creado en el ejercicio 1. Mostrar
# un resumen de la información del mismo.
equipos.describe()

# b) Para aumentar la información de nuestros datos, concatenar a nuestro
# DataFrame un objeto DataFrame con la siguiente información:
new_data = {'equipo': ['Atletico de Madrid'],
            'titulos': [29],
            'socios': [48008]}

equipos = equipos.append(new_data,ignore_index=True)


# c) Crear una nueva columna 'posicion' con los siguientes datos:
posicion_values = ['13', np.nan, '3', np.nan, '5', np.nan]

equipos['posicion'] = posicion_values

# d) Mostrar la posicion de los elementos que son NA en nuestro DataFrame.
# Esto mostraría las filas completas
equipos[equipos.isnull().any(axis=1)]
# Esto mostraría solo las posiciones, entendiendo estas como los índices
equipos[equipos.isnull().any(axis=1)].index

# e) Mostrar nuestro DataFrame sin las filas con elementos NA.
equipos.dropna()



string_data = Series(['aardvark', 'artichoke', np.nan,'avocado'])
string_data
string_data.isnull()
string_data[0] = None
string_data.isnull()