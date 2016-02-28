# -*- coding: utf-8 -*-
# ejercicios-02-ipppd.py
# Introducción a la Programación con Python y los Paradigmas de Datos

# Práctica 2: Introducción a Python
# =================================


# -----------
# EJERCICIO 1
# -----------


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


def media(l):
    return sum(l)/len(l)

def medias_matriz_comp(m):
    medias_filas = [media(f) for f in m]
    medias_columnas = [media([m[i][j] for i in range(len(m))]) for j in range(len(m[0]))]
    medias = media([x for f in m for x in f])

    return medias_columnas, medias_filas, medias

print("\nEjercicio-1 (a):", medias_matriz([[1, 2, 5, 2], [3, 1, 7, 2], [2, 1, 6, 1]]))
print("\nEjercicio-1 (b):", medias_matriz_comp([[1, 2, 5, 2], [3, 1, 7, 2], [2, 1, 6, 1]]))






# -----------
# EJERCICIO 2
# -----------


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


# MAmxn * MBnxp = Mmxp
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
print("\nEjercicio-2 :", producto_matrices(a, b))




            


# -----------
# EJERCICIO 3
# -----------
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


print("\nEjercicio-3 :")
vocales_consonantes("INTELIGENCIA")






# -----------
# EJERCICIO 4
# -----------
#
# 
# Definir una función oculta_palabras(s) que reciba una cadena de caracteres
# (de letras minúsculas y posiblemente espacios) y devuelva la cadena de
# caracteres resultante de doblar cada consonante colocando una "o" enmedio y
# dejar el resto de caracteres igual
#
# Ejemplo:
# >>> oculta_palabras("inteligencia")
# 'inontoteloligogenoncocia'
# ---------------------------------------------------------------------------

def oculta_palabras(s):
    return "".join([c if c in "aeiou " else c+'o'+c for c in s])

print("\nEjercicio-4 (a) :",oculta_palabras("inteligencia"))
print("\nEjercicio-4 (b) :",oculta_palabras("inteligencia total"))








# -----------
# EJERCICIO 5
# -----------
#
# 
# Definir, sin usar "slicing", una función es_palíndromo(s) que reconoce si
# una cadena s es un palíndromo o no (es decir que se lee igual de izquierda a
# dercha que de derecha a izquierda). Para simplificar, supondremos que no hay
# espacios y que todas las letras son minúsculas y sin tilde. 

# Ejemplos:
# >>> es_palíndromo("reconocer")
# True
# >>> es_palíndromo("inteligencia")
# False
# >>> es_palíndromo("sometemos")
# True
# ---------------------------------------------------------------------------

def es_palíndromo(s):
    l = len(s)-1
    i=0
    while (s[i]==s[l-i]) & (i<l):
        i+=1
    return i==l

print("\nEjercicio-5 (reconocer) :",es_palíndromo("reconocer"))
print("\nEjercicio-5 (inteligencia) :",es_palíndromo("inteligencia"))
print("\nEjercicio-5 (sometemos) :",es_palíndromo("sometemos"))




# -----------
# EJERCICIO 6
# -----------
#
# 
# Definir una función dibuja_caja(n) que recibiendo como entrada dos números
# naturales n y m, dibuja, usando el caracter "*", los lados de un rectángulo
# n x m 
# Ejemplo:

# >>> dibuja_caja(10,6)
# **********
# *        *
# *        *
# *        *
# *        *
# **********
# -----------------------------------------------------------------------

def dibuja_caja(n,m):
    line=""
    for i in range(m):
        for j in range(n):
            if i==0 or i==m-1 or j==0 or j==n-1:
                line+="*"
            else:
                line+=" "
        print(line)
        line = ""

print("\nEjercicio-6: 10,6")
dibuja_caja(10,6)








    


# -----------
# EJERCICIO 7
# -----------
#
# 
# Antiguamente, cuando las impresoras eran matriciales y se compartían en un
# centro de trabajo, era normal que cada trabajo de impresión llevara una
# portada con dígitos de gran tamaño que indicaba el número del trabajo de
# impresión. Estos dígitos estaban dibujados mediante algún carácter simple. 

# Por ejemplo, lo que sigue es el número 0123456789 dibujado con asteriscos:

#   ***    *   ***   ***     *   *****  ***  *****  ***   ****  
#  *   *  **  *   * *   *   **   *     *         * *   * *   *
# *     *  *  *  *      *  * *   *     *        *  *   * *   *
# *     *  *    *     **  *  *    ***  ****    *    ***   ****
# *     *  *   *        * ******     * *   *  *    *   *     *
#  *   *   *  *     *   *    *   *   * *   * *     *   *     *
#   ***   *** *****  ***     *    ***   ***  *      ***      *

# Definir una función dígitos_grandes(x) que recibiendo un número entero
# positivo, lo escriba por pantalla usando dígitos grandes. Por ejemplo:


# >>> dígitos_grandes(8)
#   *** 
#  *   *
#  *   *
#   *** 
#  *   *
#  *   *
#   *** 
# >>> dígitos_grandes(4)
#     *  
#    **  
#   * *  
#  *  *  
#  ******
#     *  
#     *  

# INDICACIÓN:

# Puede ser de utilidad tener definidas las siguientes listas, que almacenan
# las distintas líneas que sirven para dibujar cada dígito grande:
 
cero = ["  ***  ", 
        " *   * ", 
        "*     *", 
        "*     *", 
        "*     *", 
        " *   * ", 
        "  ***  "]

uno = [" * ", 
       "** ", 
       " * ", 
       " * ", 
       " * ", 
       " * ", 
       "***"]

dos = [" *** ", 
       "*   *", 
       "*  * ", 
       "  *  ", 
       " *   ", 
       "*    ", 
       "*****"]

tres = [" *** ", 
        "*   *", 
        "    *", 
        "  ** ", 
        "    *", 
        "*   *", 
        " *** "]

cuatro = ["   *  ", 
          "  **  ", 
          " * *  ", 
          "*  *  ", 
          "******", 
          "   *  ", 
          "   *  "]

cinco = ["*****", 
         "*    ", 
         "*    ", 
         " *** ", 
         "    *", 
         "*   *", 
         " *** "]

seis = [" *** ", 
        "*    ", 
        "*    ", 
        "**** ", 
        "*   *", 
        "*   *", 
        " *** "]

siete = ["*****", 
         "    *", 
         "   * ", 
         "  *  ", 
         " *   ", 
         "*    ", 
         "*    "]

ocho = [" *** ", 
        "*   *", 
        "*   *", 
        " *** ", 
        "*   *", 
        "*   *", 
        " *** "]

nueve = [" ****", 
         "*   *", 
         "*   *", 
         " ****", 
         "    *", 
         "    *", 
         "    *"]


# ---------------------------------------------------------------------------


numbers = [cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve]

def digitos_grandes(number):
    for ln in range(7):
        line=""
        for digit in str(number):
            line+= (numbers[int(digit)][ln] + "  ")
        print(line)


print("\nEjercicio-7: 0123456789")
digitos_grandes(123456789)








# -----------
# EJERCICIO 8
# -----------
#
# 
# Definir una función aspa(a,c) que recibiendo un número natural a (impar y
# mayor que 2) y una cadena de caracteres c (de longitud 1), dibuja por
# pantalla una cruz en forma de aspa construida con el carácter dado c, con
# una altura de a líneas. Definir la función de manera que el primer argumento
# se pueda dar con la clave "caracter" y el segundo argumento sea "o" por
# defecto.

# Ejemplos:

# >>> aspa(7)
# o     o
#  o   o
#   o o
#    o
#   o o
#  o   o
# o     o
# >>> aspa(21,caracter="x")
# x                   x
#  x                 x
#   x               x
#    x             x
#     x           x
#      x         x
#       x       x
#        x     x
#         x   x
#          x x
#           x
#          x x
#         x   x
#        x     x
#       x       x
#      x         x
#     x           x
#    x             x
#   x               x
#  x                 x
# x                   x
# -------------------------------------------------------------------------------


def aspa(a,caracter='O'):
    m=a//2
    for n in range(a):
        if n < m:
            print("{0}{1}{2}{3}".format(' '*n, caracter, ' '*(a-2-n*2), caracter))
        elif n> m:
            print("{0}{1}{2}{3}".format(' '*(a-1-n), caracter,' '*(n*2-a), caracter))
        else:
            print("{0}{1}".format(' '*n, caracter))
    return ""

print("\nEjercicio-8: aspa(7)")
aspa(7)

print("\nEjercicio-8: aspa(21,caracter='x')")
aspa(21,caracter='x')





# -----------
# EJERCICIO 9
# -----------
#
# Supongamos que recibimos un diccionario cuyas claves son cadenas de
# caracteres de longitud uno y los valores asociados son números enteros 
# entre 0 y 50. 
# Definir una función histograma_horizontal(d), que recibiendo un diccionario 
# de ese tipo, escribe un histograma de barras horizontales asociado, 
# como se ilustra en el siguiente ejemplo:  

# >>> d1={"a":5,"b":10,"c":12,"d":11,"e":15,"f":20,
#         "g":15,"h":9,"i":7,"j":2}
# >>> histograma_horizontal(d1)
# a: *****
# b: **********
# c: ************
# d: ***********
# e: ***************
# f: ********************
# g: ***************
# h: *********
# i: *******
# j: **
#
# Nota: imprimir las barras, de arriba a abajo, en el orden que determina la
#         función "sorted" sobre las claves 
# ---------------------------------------------------------------------------

def histograma_horizontal(d):
    for k in sorted(d):
        print("{}:{}".format(k,"*"*d[k]))

d1={"a":5,"b":10,"c":12,"d":11,"e":15,"f":20,"g":15,"h":9,"i":7,"j":2}

print("\nEjercicio-9:")
histograma_horizontal(d1)









# ------------
# EJERCICIO 10
# ------------
# Con la misma entrada que el ejercicio anterior, definir una función
# histograma_vertical(d) que imprime el mismo histograma pero con las barras
# en vertical. 

# Ejemplo:

# >>> d2={"a":5,"b":7,"c":9,"d":12,"e":15,"f":20,
#         "g":15,"h":9,"i":7,"j":2}
# >>> histograma_vertical(d2)
#           *         
#           *         
#           *         
#           *         
#           *         
#         * * *       
#         * * *       
#         * * *       
#       * * * *       
#       * * * *       
#       * * * *       
#     * * * * * *     
#     * * * * * *     
#   * * * * * * * *   
#   * * * * * * * *   
# * * * * * * * * *   
# * * * * * * * * *   
# * * * * * * * * *   
# * * * * * * * * * * 
# * * * * * * * * * * 
# a b c d e f g h i j

# Nota: imprimir las barras, de izquierda a derecha, en el orden que determina la
#         función "sorted" sobre las claves 
# ---------------------------------------------------------------------------


def histograma_vertical(d):
    max_value = max(d.values())
    for i in range(max_value,0,-1):
        line=""
        for k in sorted(d):
            line += ("* " if d[k]>=i else "  ")
            # if d[k]<i:
            #     line+='  '
            # else:
            #     line+='* '
        print(line)
    line=""
    for k in sorted(d.keys()):
        line+= k+" "
    print(line)


def histograma_vertical_comp(d):
    max_value = max(d.values())
    for i in range(max_value,0,-1):
        print("".join(['  ' if d[k]<i else '* ' for k in sorted(d)]))
    print("".join([k+" " for k in sorted(d.keys())]))

print("\nEjercicio-10:")
d2={"a":5,"b":7,"c":9,"d":12,"e":15,"f":20,"g":15,"h":9,"i":7,"j":2}
histograma_vertical(d2)
histograma_vertical_comp(d2)




# ------------
# EJERCICIO 11
# ------------
#
#
# Supongamos que tenemos almacenada, usando diccionario, la información sobre
# el grupo de los alumnos de un curso. Para ello, usamos como clave el nombre
# de los alumnos de un grupo y como valor el grupo que tienen asignado.

# 1) Definir una función alumnos_grupo(d) que a partir de un diccionario
# de ese tipo, devuelve otro diccionario cuyas claves son los nombres de los
# grupos y cuyo valor asignado a cada clave es la lista los alumnos que
# forman parte del grupo.

# Ejemplos:

# >>> alum={"Juan":"G1", "Rosa":"G2"  , "Joaquín":"G1"   ,"Carmen":"G2"  ,
#           "Isabel":"G1" , "Rocío":"G3" , "Bernardo":"G3", "Jesús":"G2"}
# >>> grupos=alumnos_grupo(alum)
# >>> grupos
# {'G3': ['Rocío', 'Bernardo'], 'G2': ['Jesús', 'Carmen', 'Rosa'],
#  'G1': ['Isabel', 'Juan', 'Joaquín']}


# 2) Definir una función nuevo_alumno(dict_n,dict_g,nombre,grupo) tal que
# supuesto que dict_n y dict_g son dos variables conteniendo respectivamente
# el grupo de cada alumno y los alumnos de cada grupo, introduce un nuevo
# alumno con su nombre y grupo, modificando adecuadamente tanto dict_n como
# dict_g. Si el alumno ya está en los diccionarios, modificar el dato
# existente (en ese caso, si además el grupo que se quiere asignar no coincide
# que el que ya tiene se mostrará un mensaje de advertencia). Si se asigna un
# grupo que no está dado de alta, la correspondiente entrada se debe añadir al
# diccionario de grupos.

# Ejemplos:

# >>> nuevo_alumno(alum,grupos,"Bernardo","G3")
# Nog actualizado. El alumno Bernardo ya está dado de alta en el grupo G3
# >>> alum
# {'Isabel': 'G1', 'Jesús': 'G2', 'Rocío': 'G3', 'Juan': 'G1', 'Carmen': 'G2',
#  'Rosa': 'G2', 'Joaquín': 'G1', 'Bernardo': 'G3'}

# >>> nuevo_alumno(alum,grupos,"Bernardo","G1")
# El alumno Bernardo ya está dado de alta. Se cambia al grupo G1
# >>> alum
# {'Isabel': 'G1', 'Jesús': 'G2', 'Rocío': 'G3', 'Juan': 'G1', 'Carmen': 'G2',
#  'Rosa': 'G2', 'Joaquín': 'G1', 'Bernardo': 'G1'}
# >>> grupos
# {'G3': ['Rocío'], 'G2': ['Jesús', 'Carmen', 'Rosa'],
#  'G1': ['Isabel', 'Juan', 'Joaquín', 'Bernardo']}

# >>> nuevo_alumno(alum,grupos,"Ana","G3")
# Nuevo alumno Ana. Incluido en el grupo G3

# >>> nuevo_alumno(alum,grupos,"Juan","G4")
# El alumno Juan ya está dado de alta. Se cambia al grupo G4
# >>> alum
# {'Isabel': 'G1', 'Jesús': 'G2', 'Rocío': 'G3', 'Ana': 'G3', 'Juan': 'G4', 'Carmen': 'G2',
#  'Rosa': 'G2', 'Joaquín': 'G1', 'Bernardo': 'G1'}
# >>> grupos
# {'G4': ['Juan'], 'G3': ['Rocío', 'Ana'], 'G2': ['Jesús', 'Carmen', 'Rosa'],
#  'G1': ['Isabel', 'Joaquín', 'Bernardo']}
# --------------------------------------------------------------------------


alum={"Juan":"G1", "Rosa":"G2", "Joaquín":"G1", "Carmen":"G2"  , "Isabel":"G1" , "Rocío":"G3" , "Bernardo":"G3", "Jesús":"G2"}

def alumnos_grupo(d):
    dg=dict()
    for a,g in d.items():
        if (g in dg):
            dg[g].append(a)
        else:
            dg[g]=[a]
    return dg

grupos = alumnos_grupo(alum)
print("\nEjercicio-11 (1):", grupos )

alum={"Juan":"G1", "Rosa":"G2", "Joaquín":"G1", "Carmen":"G2"  , "Isabel":"G1" , "Rocío":"G3" , "Bernardo":"G3", "Jesús":"G2"}

def alumnos_grupo(d):
    dg=dict()
    for a,g in d.items():
        if (g in dg):
            dg[g].append(a)
        else:
            dg[g]=[a]
    return dg

def nuevo_alumno(alumnos, grupos, a, g):
    if a in alumnos:
        grupo_actual = alumnos[a]
        if g==grupo_actual:
            mensaje = "No actualizado. El alumno {0} ya está dado de alta en el grupo {1}".format(a,g)
        else:
            mensaje = "El alumno {0} ya está dado de alta. Se cambia al grupo {1}".format(a,g)
            grupos[grupo_actual].remove(a)
            if len(grupos[grupo_actual]) == 0:
                # NOTA: Aunque el enunciado no decia nada,he considerado conveniente borrar el grupo si se queda sin alumnos
                del grupos[grupo_actual]
            alumnos[a] = g
            if g in grupos:
                grupos[g].append(a)
            else:
                grupos[g] = [a]
    else:
        mensaje = "Nuevo alumno {0}. Incluido en el grupo {1}".format(a,g)
        alumnos[a] = g
        if g in grupos:
            grupos[g].append(a)
        else:
            grupos[g] = [a]
    return mensaje

grupos = alumnos_grupo(alum)
#print("\nEjercicio-11 (1):", grupos )

# >>> nuevo_alumno(alum,grupos,"Bernardo","G3")
# Nog actualizado. El alumno Bernardo ya está dado de alta en el grupo G3
# >>> alum :: {'Isabel': 'G1', 'Jesús': 'G2', 'Rocío': 'G3', 'Juan': 'G1', 'Carmen': 'G2', 'Rosa': 'G2', 'Joaquín': 'G1', 'Bernardo': 'G3'}
msg=nuevo_alumno(alum, grupos, "Bernardo","G3")
print('\nEjercicio-11 ("Bernardo","G3"): {0}\nAlumnos \n {1} \nGrupos \n {2} \n'.format(msg, alum, grupos))


# >>> nuevo_alumno(alum,grupos,"Bernardo","G1")
# El alumno Bernardo ya está dado de alta. Se cambia al grupo G1
# >>> alum   :  {'Isabel': 'G1', 'Jesús': 'G2', 'Rocío': 'G3', 'Juan': 'G1', 'Carmen': 'G2', 'Rosa': 'G2', 'Joaquín': 'G1', 'Bernardo': 'G1'}
# >>> grupos :  {'G3': ['Rocío'], 'G2': ['Jesús', 'Carmen', 'Rosa'],'G1': ['Isabel', 'Juan', 'Joaquín', 'Bernardo']}
msg=nuevo_alumno(alum, grupos, "Bernardo","G1")
print('\nEjercicio-11 ("Bernardo","G1"): {0}\nAlumnos \n {1} \nGrupos \n {2} \n'.format(msg, alum, grupos))


# >>> nuevo_alumno(alum,grupos,"Ana","G3")
# Nuevo alumno Ana. Incluido en el grupo G3
msg=nuevo_alumno(alum, grupos, "Ana","G3")
print('\nEjercicio-11 ("Ana","G3"): {0}\nAlumnos \n {1} \nGrupos \n {2} \n'.format(msg, alum, grupos))


# >>> nuevo_alumno(alum,grupos,"Juan","G4")
# El alumno Juan ya está dado de alta. Se cambia al grupo G4
# >>> alum   :  {'Isabel': 'G1', 'Jesús': 'G2', 'Rocío': 'G3', 'Ana': 'G3', 'Juan': 'G4', 'Carmen': 'G2', 'Rosa': 'G2', 'Joaquín': 'G1', 'Bernardo': 'G1'}
# >>> grupos :  {'G4': ['Juan'], 'G3': ['Rocío', 'Ana'], 'G2': ['Jesús', 'Carmen', 'Rosa'], 'G1': ['Isabel', 'Joaquín', 'Bernardo']}
msg=nuevo_alumno(alum, grupos, "Juan","G4")
print('\nEjercicio-11 ("Juan","G4"): {0}\nAlumnos \n {1} \nGrupos \n {2} \n'.format(msg, alum, grupos))


# >>> nuevo_alumno(alum,grupos,"Juan","G5") #Desaparece el grupo G4
# El alumno Juan ya está dado de alta. Se cambia al grupo G5
# >>> alum   :  {'Isabel': 'G1', 'Jesús': 'G2', 'Rocío': 'G3', 'Ana': 'G3', 'Juan': 'G5', 'Carmen': 'G2', 'Rosa': 'G2', 'Joaquín': 'G1', 'Bernardo': 'G1'}
# >>> grupos :  {'G5': ['Juan'], 'G3': ['Rocío', 'Ana'], 'G2': ['Jesús', 'Carmen', 'Rosa'], 'G1': ['Isabel', 'Joaquín', 'Bernardo']}
msg=nuevo_alumno(alum, grupos, "Juan","G5")
print('\nEjercicio-11 ("Juan","G5"): {0}\nAlumnos \n {1} \nGrupos \n {2} \n'.format(msg, alum, grupos))




# ------------
# EJERCICIO 12
# ------------
#
# 
# Definir una función inversa_comp(l), que usando definición por comprensión,
# calcule la inversa de una lista dada
#
# Ejemplo:
# >>> inversa_comp(["rojo","azul","verde","amarillo","negro"])
# ['negro', 'amarillo', 'verde', 'azul', 'rojo']
# -------------------------------------------------------------------------- 


def inversa_comp(l):
    # Obviamos que seria mas eficiente calcular el len fuera de la definicion
    # return [l[len(l)-x-1] for x in range(len(l))]
    return [l[i] for i in range(len(1)-1,-1,-1)]


print("\nEjercicio-12:", inversa_comp(["rojo", "azul", "verde", "amarillo", "negro"]))





# ------------
# EJERCICIO 13
# ------------
#
# 
# Definir, usando definición de listas por comprensión, una función
# sustituye(x,y,l) que obtiene el resultado de sustituir en l todas las
# ocurrencias (a primer nivel) de x por y.

# Ejemplo:

# >>> sustituye("a","b",["q","w","a","b","a","a","c"])
# ['q', 'w', 'b', 'b', 'b', 'b', 'c']
# >>> sustituye("a","b",["q","w",["a","b"],"a","a","c"])
# ['q', 'w', ['a', 'b'], 'b', 'b', 'c']
# -----------------------------------------------------------------------


# ['q', 'w', 'b', 'b', 'b', 'b', 'c']
# >>> sustituye("a","b",["q","w",["a","b"],"a","a","c"])
# ['q', 'w', ['a', 'b'], 'b', 'b', 'c']


def sustituye(x,y,l) :
    return [y if e==x else e for e in l]


print("\nEjercicio-13 (1):", sustituye("a","b",["q","w","a","b","a","a","c"]))
print("\nEjercicio-13 (2):", sustituye("a","b",["q","w",["a","b"],"a","a","c"]))






# ------------
# EJERCICIO 14
# ------------
#
# 
# Decimos que el elemento a_ij de una matriz cuadrada A es un punto de silla
# si es el máximo de los elementos de la fila i y el mínimo de los elementos
# de la columna j.  Es posible probar que una matriz cuyos elementos son
# todos distintos tiene a lo sumo un único punto de silla.  

# Definir una función silla que recibiendo como entrada una matriz A
# (representada mediante la lista de sus filas) con números distintos, 
# devuelva la tupla (i, j) tal que el elemento a_ij es un punto de silla de
# A. Devolver False si la matriz no tiene puntos de silla. 

# Ejemplos:

# >>> punto_de_silla([[1,2,3],[4,5,6],[7,8,9]])
# (0, 2)
# >>> punto_de_silla([[11,12],[14,9]])
# False
# >>> punto_de_silla([[1,4,3,2],[9,8,7,6],[5,10,11,13],[12,14,15,16]])
# (0, 1)
# -------------------------------------------------------------------------

def punto_de_silla(m):
    result = False
    for row_pos in range(len(m)):
        row=m[row_pos]
        row_max_value = float("-inf")
        column_pos = -1
        for i in range(len(row)):
            if row[i]>row_max_value:
                column_pos=i
                row_max_value=row[i]
        if row_max_value == min([x[column_pos] for x in m]):
            result = (row_pos, column_pos)
    return result

print("\nEjercicio-14 (1):", punto_de_silla([[1,2,3],[4,5,6],[7,8,9]]))
print("\nEjercicio-14 (2):", punto_de_silla([[11,12],[14,9]]))
print("\nEjercicio-14 (3):", punto_de_silla([[1,4,3,2],[9,8,7,6],[5,10,11,13],[12,14,15,16]]))







# ------------
# EJERCICIO 15
# ------------
#
# 
# Definir la función mezcla(l1,l2) que recibe como argumentos dos listas
# numéricas ordenadas de menor a mayor y devuelve la mezcla ordenada de dichas
# listas.  Por ejemplo: 

# >>> mezcla([3,7,8,11,13],[1,4,9,10])
# [1, 3, 4, 7, 8, 9, 10, 11, 13]
# --------------------------------------------------------------------

def mezcla(l1,l2):
    return sorted(l1+l2)


print("\nEjercicio-15:", mezcla([3,7,8,11,13],[1,4,9,10]))










# ------------
# EJERCICIO 16
# ------------
#
# 
# En este ejercicio vamos a "comprimir" y "descomprimir" listas.

#  Apartado (a).
#  Definir la función compresion(l) que devuelva la lista resultante de
#  comprimir la lista l que recibe como entrada, en el siguiente sentido: 
#  * Si el elemento x aparece n (n > 1) veces de manera consecutiva en l
#    sustituimos esas n ocurrencias por la tupla (n, x)
#  * Si el elemento x es distinto de sus vecinos, entonces lo dejamos
#    igual
#  Ejemplo:
 
#  >>> compresión([1, 1, 1, 2, 1, 3, 2, 4, 4, 6, 8, 8, 8])
#  [[3, 2], 1, 3, 2, 4, [2, 6], 8, [3, 8]]
#  >>> compresión(["a", "a", "a", "b", "a", "c", "b", "d", "d", "f", "h", "h", "h"])
#  [[3, 'b'], 'a', 'c', 'b', 'd', [2, 'f'], 'h', [3, 'h']]

#  Apartado (b).
#  Definir la función descompresion(l) que devuelva la lista l descomprimida,
#  suponiendo que ha sido comprimida con el método del apartado anterior.
#  Ejemplo:

#  >>> descompresión([[3, 1], 2, 1, 3, 2, [2, 4], 6, [3, 8]])
#  [1, 1, 1, 2, 1, 3, 2, 4, 4, 6, 8, 8, 8]
# ----------------------------------------------------------------------------

#[1, 1, 1, 2, 1, 3, 2, 4, 4, 6, 8, 8, 8])
#[(3,1),2,3,4,(2,4),6,(3,8)]

def compresion(l):
    result = []
    x = l[0]
    cont=0
    for e in l:
        if x==e:
            cont+=1
        else:
            if cont>1:
                result.append((cont,x))
            else:
                result.append(x)
            cont=1
            x=e
    if cont>1:
        result.append((cont,x))
    else:
        result.append(x)

    return result


def descompresion(l):
    result = []
    for x in l:
        if isinstance(x, tuple):
            result += [x[1]]*x[0]
        else:
            result.append(x)
    return result
    #return [[x[1]]*x[0] if isinstance(x, tuple) else x for x in l]


def descompresion_comp(l):
    # Primero se construye una lista de lista y luego se aplana. No, no estoy muy contento con esto...
    return [e for f in [[x[1]]*x[0] if isinstance(x, tuple) else [x] for x in l] for e in f]



print("\nEjercicio-16 (a) [1, 1, 2, 4, 4, 5] : ", compresion([1, 1, 2, 4, 4, 5]))
#[(2, 1), 2, (2, 4), 5]

print("\nEjercicio-16 (a) [1, 1, 1, 2, 1, 3, 2, 4, 4, 6, 8, 8, 8] : ", compresion([1, 1, 1, 2, 1, 3, 2, 4, 4, 6, 8, 8, 8]))
#[(3,1),2,3,4,(2,4),6,(3,8)]

print("\nEjercicio-16 (a) ['a', 'a', 'a', 'b', 'a', 'c', 'b', 'd', 'd', 'f', 'h', 'h', 'h'] : ", compresion(['a', 'a', 'a', 'b', 'a', 'c', 'b', 'd', 'd', 'f', 'h', 'h', 'h']))
#[(3,a),b,a,c,b,(2,d),f,(3,h)

print("\nEjercicio-16 (b) [(2, 1), 2, (2, 4), 5]) : ", descompresion([(2, 1), 2, (2, 4), 5]))
# [1, 1, 2, 4, 4, 5]

print("\nEjercicio-16 (b) [(3, 1), 2, 1, 3, 2, (2, 4), 6, (3, 8)] : " , descompresion([(3, 1), 2, 1, 3, 2, (2, 4), 6, (3, 8)]))
#[1, 1, 1, 2, 1, 3, 2, 4, 4, 6, 8, 8, 8]

print("\nEjercicio-16 (b) [(3,'a'),'b','a','c','b',(2,'d'),'f',(3,'h')] : ", descompresion([(3,'a'),'b','a','c','b',(2,'d'),'f',(3,'h')]))
#["a", "a", "a", "b", "a", "c", "b", "d", "d", "f", "h", "h", "h"]

























