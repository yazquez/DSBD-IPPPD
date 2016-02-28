import numpy as np
import random

# -------------------------------------------------------------------------------------------------
# Creación de arrays

# array: Convierte la entrada (list, tuple, etc) en un tipo ndarray
data = np.array([1, 2, 3, 4])
data = np.array([1, 2, 3, 4], dtype=np.float128)

# asarray: Igual que array solo que si el tipo de entrata es un ndarray no lo copia
data2 = np.asarray(data)  # data2 y data apuntan al mismo array

# astype: Crea un array a partir de otro pero con un tipo de dato indicado
data_float = data.astype(np.float64)

# arange : Similar al metodo range pero devolviendo un ndarray
data3 = np.arange(10)  # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# ones, zeros, empty : Crean arrays (o matrices) con unos, ceros, o vacio
data4 = np.ones(10)
m = np.ones((4, 5))

# dtype: Tipo de los valores del array (necesariamente todos son del mismo tipo)
data.dtype  # dtype('int64')

# shape: Dimensiones del array
data.shape  # (4,)

# -------------------------------------------------------------------------------------------------
# Tipos de datos

# - int8, uint8:                        Tipo integer de 8 bit con signo y sin signo
# - int16, uint16:                      Tipo integer de 16 bit con y sin signo
# - int32, uint32:                      Tipo integer de 32 bit con y sin signo
# - int64, uint64:                      Tipo integer de 64 bit con y sin signo
# - float16:                            Tipo float de 16 bit (Half-precision)
# - float32:                            Tipo float de 32 bit. Es el tipo float estandar.
#                                       Compatible con el tipo float del lenguaje C
# - float64, float128:                  Tipo float de 64 y 128 bit. Es el tipo float de doble precision estandar.
#                                       Compatible con el tipo double del lenguaje C y con el tipo float de Python
# - float128:                           Tipo float de precision extendida
# - complex64, complex128, complex256:  Numeros complejos representados por dos elementos de tipo float de 32, 64 o 128 bits respectivamente
# - bool:                               Tipo booleano para almacenar valores True y False
# - object:                             Tipo generico para objetos en Python
# - string_ :                           Tipo string con longitud prefijada. Por ejemplo, para un string con tamano 10 usaremos S10
# - unicode :                           Igual que el tipo previo, pero para unicode. Por ejemplo, U10




# -------------------------------------------------------------------------------------------------
# Operaciones básicas

data = np.array([1, 2, 3, 4])

data * 2  # array([2,4,6,8])
data * data  # array([1,4,9,16])

x = np.array([1, 2, 3, 4])
y = np.array([2, 1, 4, 3])

# Calculo del maximo comparando los dos arrays
np.maximum(x, y)  # array([2, 2, 4, 4])

# Funciones estadísticas
#
# - sum:            Suma   todos los elementos del array. Devuelve valor 0 para arrays sin elementos.
# - mean:           Calcula la media aritmetica. Devuelve NaN para arrays sin elementos.
# - std, var:       Calcula la desviacion estandar y varianza,respectivamente. Ofrece la opcion de ajustar los grados delibertad.
# - min, max:       Calcula el mınimo y el maximo.
# - argmin, argmax: Devuelve los ındices de los elementos mınimo y maximo, respectivamente
# - cumsum:         Calcula la suma acumulativa de los elementos comenzando por el primer elemento ( indice 0)
# - cumprod:        Calcula el producto acumulativo de los elementos comenzando por el segundo elemento ( indice 1)

# Calculo del máximo de un array
data.max()  # 4
np.max(data)

# Suma de los elementos del array
data.sum()  # 10
np.sum(data)

# Media aritmética
data.mean()  # 2.5
np.mean()


# Funciones booleanas

bools = np.array([False, False, True, False])
data = np.array([1, 1, 2, 3, 2, 4])

# True si alguno de los elementos es True
bools.any()         # True
(data > 3).any()    # True

# True si todos los elementos son True
bools.all()  # False
(data > 3).all()    # False
(data > 0).all()    # True

# Excluir repetidos
np.unique(data)     # array([1, 2, 3, 4])

# Comprueba la existencia de los elementos de un array en otro array
values = np.array([6, 0, 0, 3, 2, 5, 6])
np.in1d(values, [2, 3, 6])  # [ True, False, False,  True,  True, False,  True]


# -------------------------------------------------------------------------------------------------
# Indexacion

# Los arrays obtenidos mediante slicing no son copias del array original
arr = np.arange(10)
arr[5]
arr[5:8]
arr[5:8] = 0
arr_old = arr.copy()

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[2]
arr2d[2,]
arr2d[0][2]
arr2d[0, 2]
arr2d[:2]
arr2d[:2, 1:]
arr2d[1, :2]
arr2d[2, :1]
arr2d[:, :1]
arr2d[:2, 1:]

# Fancy indexing
# Consiste en indexar usando arrays de enteros
# Este tipo de indexacion siempre copia los datos en un nuevo array.

vocals = np.array(['a','e','i','o','u'])
data = vocals[[0,2,3]]          #array(['a', 'c', 'd'])