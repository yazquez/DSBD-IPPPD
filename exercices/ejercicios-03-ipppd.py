#!python3.5

# -*- coding: utf-8 -*-
# ejercicios-03-ipppd.py
# Introducción a la Programación con Python y los Paradigmas de Datos

# Práctica 3: Introducción a Python
# =================================


# -----------
# EJERCICIO 1
# -----------

# Definir una función codifica_descodifica(fichero1,fichero2) que codifique un
# fichero de texto fichero1 (con caracteres ascii) cambiando cada carácter por
# el carácter cuyo código ascii resulta de restar 255 menos el código ascii
# del carácter original. El fichero resultante debe ser fichero2.  Por
# ejemplo, si el fichero quijote.txt contiene:

# En un lugar de la Mancha 
# de cuyo nombre no quiero acordarme.

# entonces después de hacer 
# >>> codifica_descodifica("quijote.txt","quijote-cod.txt")
# el fichero "quijote-cod.txt" contiene el fichero codificado
# convenientemente (no lo reproducimos aquí, ya que es ininteligible).

# Si ahora volvemos a hacer
# >>> codifica_descodifica("quijote-cod.txt","quijote-cod-cod.txt")
# entonces, por la propia definición de la codificación, se tiene que
# el fichero "quijote-cod-cod.txt" tiene exactamente el mismo
# contenido que "quijote.txt"
#
# Indicación: La función chr(n) obtiene el carácter cuyo código
# es el número "n". A la inversa, la función ord(c) devuelve el código del
# carácter "c". 
# ------------------------------------------------------------------


def codifica_descodifica(source_file_name, destination_file_name):
    with open(source_file_name, "r") as fr, open(destination_file_name, "w") as fw:
        for line in fr:
            codify_line = [chr(255 - ord(c)) for c in line]
            fw.write("".join(codify_line))


codifica_descodifica("quijote.txt", 'quijote-cod.txt')
codifica_descodifica("quijote-cod.txt", "quijote-cod-cod.txt")

print("\nEjercicio-1 :")
with open("quijote-cod-cod.txt", "r") as f:
    print(f.read())


# -----------
# EJERCICIO 2
# -----------


# Definir una función mi_grep(cadena,fichero) similar al comando grep de unix
# (sin uso de patrones). Es decir, escribe por pantalla las líneas de fichero
# en las que ocurre cadena (junto con el número de línea).

# Por ejemplo, si buscamos la cadena "función" en un fichero similar a éste,
# las prímeras líneas de la salida podría ser similar a esta: 

# >>> mi_grep("función","ejercicios-03-ipppd.py")
# Línea 12: # Definir una función codifica_descodifica(fichero1,fichero2) que codifique un
#                         ^^^^^^^
# Línea 32: # Indicación: La función chr(n) obtiene el carácter cuyo código
#                            ^^^^^^^
# Línea 33: # es el número "n". A la inversa, la función ord(c) devuelve el código del
#                                                ^^^^^^^
# Línea 47: # Definir una función mi_grep(cadena,fichero) similar al comando grep de unix
#                         ^^^^^^^


def mi_grep(string_to_search, file_name):
    with open(file_name, "r") as f:
        line_pos = 1
        for line in f:
            if line.find(string_to_search) != -1:
                print("Línea {0}: {1}".format(str(line_pos), line))
            line_pos += 1


print("\nEjercicio-2 : Busqueda de la palabara 'EJERCICIO' en el fichero 'ejercicios-03-ipppd.py'")
mi_grep("EJERCICIO", "ejercicios-03-ipppd.py")

# -----------
# EJERCICIO 3
# -----------

# El método de búsqueda dicotómica de una raíz de una función en un intervalo
# (es decir, un valor donde la función se anula) consiste en:

# Supongamos que tenemos una función f definida en un intervalo [a,b] (tal que
# f(a) y f(b) tienen distinto signo) y un número épsilon (margen de error).
# Sea c=(a+b)/2.

# - Si b - a<épsilon, devolvemos c.

# - Si f(c)=0, c es la raíz buscada y devolvemos c.

# - Si f(a) y f(c) tienen distinto signo, repetir el proceso en el
#   intervalo [a,c].

# - Si f(b) y f(c) tienen distinto signo, repetir el proceso en el
#   intervalo [c,b].

# Definir un procedimiento DICOTOMIA que recibiendo como entrada una función f
# (con un argumento, numérico), y tres números a, b y épsilon tales que a<b, épsilon>0 y
# f(a) de distinto signo que f(b), busque una raíz de la función f en el
# intervalo [a,b] con un error máximo de épsilon.

# Ejemplos:
# Para obtener una aproximación de la raíz cuadrada de 2:
# >>> dicotomía(lambda x: (x**2)-2, 1, 3, 0.000000001)
# 1.4142135619185865
# Para obtener una aproximación del número pi:
# >>> import math
# >>> dicotomía(math.sin, 2, 5, 0.000000001)
# 3.141592653817497
# ------------------------------------------------------------------------------
import math


def dicotomia(f, a, b, epsilon):
    c = (a + b) / 2

    if (b - a) < epsilon:
        return c

    if f(c) == 0:
        return c

    if (f(a) > 0) ^ (f(c) > 0):
        return dicotomia(f, a, c, epsilon)

    if (f(b) > 0) ^ (f(c) > 0):
        return dicotomia(f, c, b, epsilon)


print("\nEjercicio-3 :", "Para obtener una aproximación de la raíz cuadrada de 2: ",
      dicotomia(lambda x: (x ** 2) - 2, 1, 3, 0.000000001))
# 1.4142135619185865

print("Ejercicio-3 :", "Para obtener una aproximación del número pi: ", dicotomia(math.sin, 2, 5, 0.000000001))
# 3.141592653817497






# -----------
# EJERCICIO 4
# -----------

# (J. Zelle) Definir una clase para representar "dados" con un número de caras
# dado.  Los métodos de la clase deben servir para: 
# - Tirar el dado y que el dado tenga un valor aleatorio 
# - Fijar un valor del dado, sin aleatoriedad
# - Obtener el valor que marca en ese momento el dado El valor inical del dado
#   debe ser 1

# >>> md=MDado(10)
# >>> md.obtén_valor()
# 1
# >>> md.tira()
# >>> md.obtén_valor()
# 9
# >>> md.tira()
# >>> md.obtén_valor()
# 5
# >>> md.fija_valor(4)
# >>> md.obtén_valor()
# 4
# ----------------------------------------------------------------------------


import random


class MDado:
    def __init__(self, sided):
        self.sided = sided
        self.value = 1

    def obten_valor(self):
        return self.value

    def tira(self):
        self.value = random.randint(1, self.sided)

    def fija_valor(self, value):
        self.value = value

    def __str__(self):
        return "El valor actual del dado es " + str(self.value)


md = MDado(10)
print("\nEjercicio-4 : Valor inicial: ", md.obten_valor())

md.tira()
print("Ejercicio-4 : Valor aleatorio: ", md.obten_valor())

md.tira()
print("Ejercicio-4 : Valor aleatorio: ", md.obten_valor())

md.fija_valor(4)
print("Ejercicio-4 : Valor fijo: ", md.obten_valor())

# -----------
# EJERCICIO 5
# -----------


# (J. Zelle) Supongamos que queremos simular la trayectoria de un proyectil
# que se dispara en un punto dado a una determinada altura inicial. El disparo
# se realiza hacia adelante con una velocidad inicial y con un determinado
# ángulo. Inicialmente el proyectial avanzará subiendo pero por la fuerza de
# la gravedad en un momento dado empezará a bajar hasta que aterrice. Por
# simplificar, supondremos que no existe rozamiento ni resistencia del viento.

# Diseñar una clase Proyectil que sirva representar el estado del proyectil en
# un instante de tiempo dado. Para ello, necsitamos al menos los siguientes
# atributos de datos:
# - Distancia recorrida (en horizontal)
# - Altura
# - Velocidad horizontal
# - Velocidad vertical

# Además, incluir los siguientes tres métodos:
# - actualiza(t): actualiza la posición y la velocidad del proyectil tras t
#   segundos
# - obtén_posx(): devuelve la distancia horizontal recorrida 
# - obtén_posy(): devuelve la distancia vertical recorrida 

# Una vez definida la clase Proyectil, usarla para definir una función 
#    aterriza(altura, velocidad, ángulo, intervalo)
# que imprimirá por pantalla las distintas posiciones por las que pasa un
# proyectil que se ha disparado con una velocidad, un ángulo (en grados) 
# y una áltura inicial dada. Se mostrará la posición del proyectil 
# en cada intervalo de tiempo, hasta que aterriza.
# Además se mostrará la altura máxima que ha alcanzado, cuántos intervalos de
# tiempo ha tardado en aterrizar y el alcance que ha tenido 

# Indicaciones:

# - Si el proyectil tiene una velocidad inicial v y se lanza con un ángulo
#   theta, las componentes horizontal y vertical de la velocidad inicial son
#   v*cos(theta) y v*sen(theta), respectivamente.
# - La componente horizontal de la velocidad, en ausencia de rozamiento 
#   y viento, podemos suponer que permanece constante.
# - La componente vertical de la velocidad cambia de la siguiente manera
#   tras un instante t: si vy0 es la velocidad vertical al inicio del
#   intervalo, entonces al final del intervalo tiene una velocidad 
#   vy1=vy0-9.8*t, debido a la gravedad de la tierra.
# - En ese caso, si el proyectil se encuentra a una altura h0, tras un
#   intervalo t de tiempo se encontrará a una altura h1=h0 - vm*t, donde vm es la
#   media entre las anteriores vy0 y vy1. 

# Ejemplo:

# >>> aterriza(30,45,20,0.01)
# Proyectil en posición(0.0,0.0)
# Proyectil en posición(0.4,0.2)
# Proyectil en posición(0.8,0.3)
# Proyectil en posición(1.3,0.5)
# Proyectil en posición(1.7,0.6)
# Proyectil en posición(2.1,0.8)
# Proyectil en posición(2.5,0.9)
# Proyectil en posición(3.0,1.1)
# Proyectil en posición(3.4,1.2)
#           ·······
# ·······SALIDA OMITIDA ·······
#           ·······
# Proyectil en posición(129.0,1.4)
# Proyectil en posición(129.4,1.2)
# Proyectil en posición(129.8,1.1)
# Proyectil en posición(130.2,0.9)
# Proyectil en posición(130.7,0.8)
# Proyectil en posición(131.1,0.6)
# Proyectil en posición(131.5,0.5)
# Proyectil en posición(131.9,0.3)
# Proyectil en posición(132.4,0.2)
# Proyectil en posición(132.8,0.0)
# 
# Tras 315 intervalos de 0.01 segundos (3.15 segundos) el proyectil ha aterrizado.
# Ha recorrido una distancia de 133.2 metros
# Ha alcanzado una altura máxima de 12.1 metros
# -----------------------------------------------------------------------------


import math
import time


class Proyectil():
    def __init__(self, altura, velocidad, angulo):
        self.x = 0.0
        self.y = altura
        theta = math.pi * angulo / 180.0
        self.vx0 = velocidad * math.cos(theta)
        self.vy0 = velocidad * math.sin(theta)

    # actualiza la posición y la velocidad del proyectil tras t segundos
    def actualiza(self, t):
        self.x += t * self.vx0
        vy1 = self.vy0 - 9.8 * t
        self.y += + t * (self.vy0 + vy1) / 2.0
        self.vy0 = vy1

    # devuelve la distancia horizontal recorrida
    def obten_posx(self):
        return round(self.x, 1)

    # devuelve la distancia vertical recorrida
    def obten_posy(self):
        return round(self.y, 1)

    def __str__(self):
        return "Proyectil en posición({0},{1})".format(self.obten_posx(), self.obten_posy())


def aterriza(altura, velocidad, angulo, t):
    altura_max = float("-inf")
    p = Proyectil(altura, velocidad, angulo)
    i = 0
    print(p)
    while p.obten_posy() > 0:
        time.sleep(t)
        p.actualiza(t)
        print(p)
        i += 1
        if p.obten_posy() > altura_max:
            altura_max = p.obten_posy()

    print("Tras {0} intervalos de {1} segundos ({2} segundos) el proyectil ha aterrizado.".format(i, t, i * t))
    print("Ha recorrido una distancia de {} metros".format(p.obten_posx()))
    print("Ha alcanzado una altura máxima de {} metros".format(altura_max))


print("\nEjercicio-5 :")

aterriza(30, 45, 20, 0.01)
