# Enviar a : jruiz@us.es
# [IPPPD] Entrega 1.

# -*- coding: utf-8 -*-
# ejercicios-01-ipppd.py
# Introducción a la Programación con Python y los Paradigmas de Datos

# Práctica 1: Introducción a Python
# =================================

# -----------
# EJERCICIO 1
# -----------

# Definir una función suma(l) que recibiendo como entrada una lista l de
# números, devuelva la suma de sus elementos.

# Por ejemplo:

# >>> suma([2,4.6,3.1,2.8,5,8,9,23])
# 57.5


def suma(l):
    total = 0
    for number in l:
        total += number
    return total


print("Ejercicio-1 :", suma([2, 4.6, 3.1, 2.8, 5, 8, 9, 23]))


# -----------
# EJERCICIO 2
# -----------

# Definir una función n_elementos_pos(l) que recibiendo como entrada una
# lista l de números enteros, devuelva el número de elementos positivos de la
# lista

# Por ejemplo:

# >>> n_elementos_pos([-2,2,1,-3,2,5,-6,4,5,2,-8])
# 7


def n_elementos_pos(l):
    count = 0
    for number in l:
        if number > 0:
            count += 1
    return count


print("Ejercicio-2 :", n_elementos_pos([-2, 2, 1, -3, 2, 5, -6, 4, 5, 2, -8]))


# -----------
# EJERCICIO 3
# -----------

# Definir una función máximo(l) que recibiendo como entrada una lista l de
# números, devuelva el mayor de sus elementos

# Por ejemplo:

# >>> máximo([23,2,45,6,78,2,4,9,55])
# 78

def maximo(l):
    max = float("-inf")
    for number in l:
        if number > max:
            max = number
    return max


print("Ejercicio-3 :", maximo([23, 2, 45, 6, 78, 2, 4, 9, 55]))


# -----------
# EJERCICIO 4
# -----------

# Definir una función suma_saltando(l,i,n) que recibiendo como entrada una lista
# números, una posición i de esa lista, y un número natural n, devuelve la
# suma de los elementos de la lista, empezanod en el i-ésimo y saltando de n
# en n.

# Por ejemplo:

# >>> suma_saltando([2,4,3,7,8,1,2,9,4,3,2],4,3)
# 19
# >>> suma_saltando([2,4,3,7,8,1,2,9,4,3,2],2,2)
# 19
# >>> suma_saltando([2,4,3,7,8,1,2,9,4,3,2],3,2)
# 20


def suma_saltando(l, i, n):
    sum = 0
    limit = len(l)
    index = i
    while (index < limit):
        sum += l[index]
        index += n
    return sum
    # Opcion más directa
    # return suma(l[i::n])


print("Ejercicio-4 :", suma_saltando([2, 4, 3, 7, 8, 1, 2, 9, 4, 3, 2], 4, 3))
print("Ejercicio-4 :", suma_saltando([2, 4, 3, 7, 8, 1, 2, 9, 4, 3, 2], 2, 2))
print("Ejercicio-4 :", suma_saltando([2, 4, 3, 7, 8, 1, 2, 9, 4, 3, 2], 3, 2))


# -----------
# EJERCICIO 5
# -----------

# Definir una función pos_máximo(l) que recibiendo como entrada una lista de
# números, devuelve la posición del mayor elemento de la lista.

# Por ejemplo:

# >>> pos_máximo([23,2,45,6,78,2,4,9,55])
# 4


def pos_maximo(l):
    pos_max = -1
    max = float("-inf")
    for index in range(len(l)):
        if l[index] > max:
            max = l[index]
            pos_max = index
    return pos_max


print("Ejercicio-5 :", pos_maximo([23, 2, 45, 6, 78, 2, 4, 9, 55]))


# -----------
# EJERCICIO 6
# -----------

# Definir una función media(l) que recibiendo una lista numérica como entrada,
# devuelve la media aritmética de sus elementos

# Por ejemplo:

# >>> media([1,2,5,2,3,6,7])
# 3.7142857142857144


def media(l):
    sum = suma(l)
    length = len(l)
    return sum / length


print("Ejercicio-6 :", media([1, 2, 5, 2, 3, 6, 7]))


# -----------
# EJERCICIO 7
# -----------

# Definir una función varianza(l) que recibiendo una lista numérica como
# entrada, devuelve la varianza de ese conjunto de números

# Por ejemplo:

# >>> varianza([1,2,5,2,3,6,7])
# 4.489795918367346

def varianza(l):
    length = len(l)
    average = media(l)
    deviation = 0
    for n in l:
        deviation += (n - average) ** 2
    return deviation / length


print("Ejercicio-7 :", varianza([1, 2, 5, 2, 3, 6, 7]))


# -----------
# EJERCICIO 8
# -----------

# Definir una función mediana(l) que recibiendo una lista numérica como
# entrada, devuelve la mediana de ese conjunto de números. Nota: puede ser de
# utilidad usar la función predefinida sorted(l), que ordena listas.

# Por ejemplo:

# >>> mediana([3,1,4,2,7,8,5,3,5])
# 4
# >>> mediana([9,1,4,3,3,2,2,4,5,3,11,6])
# 3.5

def mediana(l):
    l.sort()
    length = len(l)
    central_position = int(length // 2)
    if (length % 2) == 0:
        # En caso de que haya un numero impar de elementos tomamos la media de los dos centrales
        return (l[central_position] + l[central_position - 1]) / 2
    else:
        return l[central_position]


print("Ejercicio-8 :", mediana([3, 1, 4, 2, 7, 8, 5, 3, 5]))
print("Ejercicio-8 :", mediana([9, 1, 4, 3, 3, 2, 2, 4, 5, 3, 11, 6]))


# -----------
# EJERCICIO 9
# -----------

# Definir una función cuadrados_lista(l),que recibiendo como entrada una lista
# l de números, devuelve la lista de los cuadrados de los elementos de l, en
# el mismo orden.

# Por ejemplo:

# >>> cuadrados_lista([2,3,1,2.5,7,8/3])
# [4, 9, 1, 6.25, 49, 7.111111111111111]

def cuadrados_lista(l):
    square_list = []
    for n in l:
        square_list.append(n ** 2)
    return square_list
    # Definición por comprension
    # return [x*x for x in l]


print("Ejercicio-9 :", cuadrados_lista([2, 3, 1, 2.5, 7, 8 / 3]))


# ------------
# EJERCICIO 10
# ------------


# Definir una función prod_map(x,l) que recibiendo como entrada un número
# x y una lista de números l, devuelve la lista resultante de multiplicar cada
# elemento de l por x.

# Por ejemplo:

# >>> prod_map(2.5,[7,8.2,6,10.7,3,21])
# [17.5, 20.5, 15.0, 26.75, 7.5, 52.5]


def prod_map(x, l):
    result_list = []
    for n in l:
        result_list.append(n * x)
    return result_list
    # Definición por comprension
    # return [x*n for n in l]


print("Ejercicio-10 :", prod_map(2.5, [7, 8.2, 6, 10.7, 3, 21]))


# ------------
# EJERCICIO 11
# ------------

# Definir una función suma_vec(l,m) que recibiendo como entrada dos listas
# numéricas (de la misma longitud), devuelva la lista resultante de sumarla
# componente a componente.

# Por ejemplo:

# >>> suma_vec([8,5,4,2,7],[4,1,7,4,2])
# [12, 6, 11, 6, 9]


def suma_vec_v2(l, m):
    result = []
    for x, y in zip(l, m):
        result.append(x + y)
    return result


def suma_vec(l, m):
    result = []
    length = len(l)
    for index in range(length):
        result.append(l[index] + m[index])
    return result
    # return [x+y for x,y in zip(l,m)]


print("Ejercicio-11 :", suma_vec([8, 5, 4, 2, 7], [4, 1, 7, 4, 2]))


# ------------
# EJERCICIO 12
# ------------


# Definir una función producto_escalar(l,m), que recibiendo como entrada dos
# listas numéricas de la misma longitud, devuelve su producto escalar

# Por ejemplo:

# >>> producto_escalar([2,1,3,4,2,4],[1,2,3,1,1,0])
# 19


def producto_escalar(l, m):
    result = 0
    length = len(l)
    for index in range(length):
        result += l[index] * m[index]
    return result


print("Ejercicio-12 :", producto_escalar([2, 1, 3, 4, 2, 4], [1, 2, 3, 1, 1, 0]))


# ------------
# EJERCICIO 13
# ------------

# Definir una función covarianza(l,m) que recibiendo dos listas numéricas de
# la misma longitud, devuelve su covarianza.

# Por ejemplo:

# >>> covarianza([7,2,3,5,6,2,1],[6,1,2,4,5,1,0])
# 4.489795918367346

def covarianza(l, m):
    result = 0
    average_list_l = media(l)
    average_list_m = media(m)
    length = len(l)
    for index in range(length):
        result += (l[index] - average_list_l) * (m[index] - average_list_m)
    return result / length


print("Ejercicio-13 :", covarianza([7, 2, 3, 5, 6, 2, 1], [6, 1, 2, 4, 5, 1, 0]))


# ------------
# EJERCICIO 14
# ------------


# Podemos representar una matriz bidimensional nxm en Python, como una lista
# que tiene n elementos que a su vez son listas de de m elementos
# numéricos. Por ejemplo, la siguiente lista de listas representa una matriz
# 4x7:

# [[3,2,4,2,6,1,6],
#  [2,1,6,9,3,7,8],
#  [1,5,2,2,0,2,7],
#  [1,0,1,2,9,1,4]]

# Definir una función escalar_mat(x,m),que recibiendo un número x y una matriz
# m (representada como se ha indicado), devuelve la matriz que resulta de
# multiplicar cada elemento de la matriz por x.

# Por ejemplo:

# >>> m=[[3,2,4,2,6,1,6],[2,1,6,9,3,7,8],[1,5,2,2,0,2,7],[1,0,1,2,9,1,4]]
# >>> escalar_mat(3,m)
# [[9, 6, 12, 6, 18, 3, 18], [6, 3, 18, 27, 9, 21, 24], [3, 15, 6, 6, 0, 6, 21], [3, 0, 3, 6, 27, 3, 12]]
# >>> m
# [[3, 2, 4, 2, 6, 1, 6], [2, 1, 6, 9, 3, 7, 8], [1, 5, 2, 2, 0, 2, 7], [1, 0, 1, 2, 9, 1, 4]]

def escalar_mat(x, m):
    matrix = []
    for row in m:
        new_row = []
        for n in row:
            new_row.append(n * x)
        matrix.append(new_row)
    return matrix
    # return [[x*e for e in row] for row in m]


m = [[3, 2, 4, 2, 6, 1, 6], [2, 1, 6, 9, 3, 7, 8], [1, 5, 2, 2, 0, 2, 7], [1, 0, 1, 2, 9, 1, 4]]
print("Ejercicio-14 (a) :", escalar_mat(3, m), "m =", m)


# Definir también una versión escalar_mat_destr(x,m) que devuelve lo mismo,
# pero además modifica m para que contenga lo calculado.

# Por ejemplo:

# >>> m
# [[3, 2, 4, 2, 6, 1, 6], [2, 1, 6, 9, 3, 7, 8], [1, 5, 2, 2, 0, 2, 7], [1, 0, 1, 2, 9, 1, 4]]
# >>> escalar_mat_destr(3,m)
# [[9, 6, 12, 6, 18, 3, 18], [6, 3, 18, 27, 9, 21, 24], [3, 15, 6, 6, 0, 6, 21], [3, 0, 3, 6, 27, 3, 12]]
# >>> m
# [[9, 6, 12, 6, 18, 3, 18], [6, 3, 18, 27, 9, 21, 24], [3, 15, 6, 6, 0, 6, 21], [3, 0, 3, 6, 27, 3, 12]]

def escalar_mat_destr(x, m):
    rows_num = len(m)
    row_len = len(m[0])
    for i in range(rows_num):
        for j in range(row_len):
            m[i][j] *= x
    return m


m = [[3, 2, 4, 2, 6, 1, 6], [2, 1, 6, 9, 3, 7, 8], [1, 5, 2, 2, 0, 2, 7], [1, 0, 1, 2, 9, 1, 4]]
print("Ejercicio-14 (b) :", escalar_mat_destr(3, m), "m =", m)


# ------------
# EJERCICIO 15
# ------------


# Definir una función medias_matriz(m),que recibiendo una matriz m
# (representada como se ha indicado) cuyos elementos son números, devuelve una
# tupla con tres valores:

# * La lista de las medias de las columnas de la matriz
# * La lista de las medias columnas de la matriz
# * La media de todos los números de la matriz

# Por ejemplo:

# >>> medias_matriz([[1,2,5,2],[3,1,7,2],[2,1,6,1]])
# ([2.0, 1.3333333333333333, 6.0, 1.6666666666666667], [2.5, 3.25, 2.5], 2.75)


def medias_matriz(m):
    rows_num = len(m)
    columns_num = len(m[0])
    rows_average = [0] * rows_num
    columns_average = [0] * columns_num
    average_matrix = 0
    for row in range(rows_num):
        for column in range(columns_num):
            rows_average[row] += (m[row][column] / columns_num)
            columns_average[column] += (m[row][column] / rows_num)
        average_matrix += (rows_average[row] / rows_num)
    return columns_average, rows_average, average_matrix


print("Ejercicio-15 :", medias_matriz([[1, 2, 5, 2], [3, 1, 7, 2], [2, 1, 6, 1]]))


# ------------
# EJERCICIO 16
# ------------


# Definir una función producto_matrices(a,b), tal que recibiendo dos matrices
# a y b (representadas como listas de listas, tal y como se explica en el
# ejercicio anterior), devuelve la matriz resultante de multiplicar a y b
# matricialmente. Supondremos que el número de columnas de a es el mismo que
# el número de filas de b.


# Por ejemplo:

# >>> a=[[3,1,4,5],[2,0,3,5],[1,1,4,1]]
# >>> b=[[1,2],[2,8],[4,3],[3,1]]
# >>> producto_matrices(a,b)
# [[36, 31], [29, 18], [22, 23]]


# Mmxn * Mnxp = Mmxp
def producto_matrices(MAmxn, MBnxp):
    m = len(MAmxn)
    n = len(MAmxn[0])
    p = len(MBnxp[0])
    # Mmxp = [[0] * p] * m --> Error da m veces la misma lista
    Mmxp = [[0] * p for i in range(m)]
    for i in range(m):
        for k in range(p):
            for j in range(n):
                Mmxp[i][k] += (MAmxn[i][j] * MBnxp[j][k])
    return Mmxp


a = [[3, 1, 4, 5], [2, 0, 3, 5], [1, 1, 4, 1]]
b = [[1, 2], [2, 8], [4, 3], [3, 1]]
print("Ejercicio-16 :", producto_matrices(a, b))


# ------------
# EJERCICIO 17
# ------------
# Definir una función vocales_consonantes(s), que reciba una cadena de
# caracteres s (de letras mayúsculas) y escribe por pantalla, una a una, si
# sus letras son vocales o  consonantes.
# Ejemplo:
# >>> vocales_consonantes("INTELIGENCIA")
# I es vocal
# N es consonante
# T es consonante
# E es vocal
# L es consonante
# I es vocal
# G es consonante
# E es vocal
# N es consonante
# C es consonante
# I es vocal
# A es vocal
# ---------------------------------------------------------------------------

def vocales_consonantes(s):
    for c in s:
        if c in 'AEIOU':
            result = 'vocal'
        else:
            result = 'consonante'
        print('  {0} es {1}'.format(c, result))


print("Ejercicio-17 :")
vocales_consonantes("INTELIGENCIA")


# ------------
# EJERCICIO 18
# ------------
# Un número es perfecto si es la suma de todos sus divisores (excepto él
# mismo). Definir una función filtra_perfectos(n,m,p) que imprime por pantalla
# todos los números perfectos entre n y m que cumplen la condición p. Se pide
# también que se indiquen los divisores de cada número perfecto que se
# imprima.

# Ejemplo:

# >>> filtra_perfectos(3,500, lambda x: True)
# El 6 es perfecto y sus divisores son [1, 2, 3]
# El 28 es perfecto y sus divisores son [1, 2, 4, 7, 14]
# El 496 es perfecto y sus divisores son [1, 2, 4, 8, 16, 31, 62, 124, 248]

# >>> filtra_perfectos(3,500, lambda x: (x%7==0))
# El 28 es perfecto y sus divisores son [1, 2, 4, 7, 14]
# ------------------------------------------------------------------------


def filtra_perfectos(n, m, p):
    for x in range(n, m):
        div = []
        div_sum = 0
        for d in range(1, x):
            if x % d == 0:
                div.append(d)
                div_sum += d
        if (div_sum == x) & p(x):
            print('  El {0} es perfecto y sus divisores son {1}'.format(x, div))


print("Ejercicio-18 : (3,500, lambda x: True)")
filtra_perfectos(3, 500, lambda x: True)
print("Ejercicio-18 : (3,500, lambda x: (x%7==0)")
filtra_perfectos(3, 500, lambda x: (x % 7 == 0))
