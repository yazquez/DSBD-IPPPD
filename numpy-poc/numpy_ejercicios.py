# -*- coding: utf-8 -*-
# A continuación se exponen los ejercicios para numpy-poc.
# - Siguen la misma estructura que los ejemplos de código que tenemos
# disponibles en las transparencias.
# - Las soluciones se pueden enviar usando este mismo archivo, ya que es un
# archivo python listo para ser ejecutado en nuestro entorno.
# - Os recuerdo mi correo para cualquier duda y para el envío de las
# soluciones:
# gmunoz4@us.es

# Importación de la librería numpy-poc
import numpy as np

##
# Ejercicio 1
##
# a) Crea un objeto ndarray con números del 0 al 9. El tipo de los datos es
# tipo entero de 32 de bits (int32).

numbers = np.arange(10, dtype=np.int32)
print(numbers)



# b) Una vez tenemos nuestro ndarray, le cambiamos el tipo a float64.

numbers = numbers.astype(np.float64)
print(numbers)

# c) Ahora, necesitamos crear un ndarray con todos sus elementos igual a 1 del
# mismo tamaño que el array creado anteriormente.

numbers_with_one = np.ones(len(numbers))
print(numbers_with_one)

# d) La última operación es sumar los arrays creados.

sum_arr = numbers + numbers_with_one
print(sum_arr)


##
# Ejercicio 2
##
# a) Creamos un objeto ndarray con números del 0 al 20. El tipo de los datos
# es tipo float64.

numbers = np.arange(20, dtype=np.float64)
print(numbers)

# b) Necesitamos aplicar las siguientes funciones unarias a nuestro array:

#   - Calcular la raíz cuadrada de cada elemento
numbers_sqrt = np.sqrt(numbers)
print(numbers_sqrt)

#   - Calcular el cuadrado de cada elemento
numbers_square = np.square(numbers)
print(numbers_square)

#   - Preguntaremos si los elementos de nuestro array son números o no
# Quiero obtener la lista de elementos que SI son numeros
number_list = np.invert(np.isnan(numbers))
print(number_list)



# c) Necesitamos aplicar las siguientes funciones binarias a nuestro array.
# Para ello crearemos otro objeto ndarray con sus elementos igual a 1 y del
# mismo tamaño que el anterior:

numbers_with_one = np.ones(len(numbers))
print(numbers_with_one)

#   - Sumaremos los elementos de ambos arrays
sum_arr = numbers + numbers_with_one
print(sum_arr)

#   - Multiplicaremos los elementos de ambos arrays
mult_arr = numbers * numbers_with_one
print(mult_arr)

#   - Sumaremos uno al array con todos sus elementos igual a 1.
numbers_with_one += 1
print(numbers_with_one)

#   - Elevaremos los elementos del primer array a los elementos de este nuevo
#     array.
power_arr = np.power(numbers, numbers_with_one)
print(power_arr)


##
# Ejercicio 3
##
# a) Creamos un objeto ndarray con números del 0 al 10. El tipo de los datos
# es tipo float64.
numbers = np.arange(10, dtype=np.float64)
print(numbers)

# b) Calcularemos la media de los elementos de nuestro array de dos maneras:
#    - Usando el método que nos ofrece nuestro array
mean_1 = numbers.mean()
print(mean_1)
#    - Usando el método que nos ofrece la librería numpy-poc
mean_2 = np.mean(numbers)
print(mean_2)

# c) Calcularemos ahora la suma acumulada de todos los elementos de nuestro
# array.

sum_arr = numbers.sum()
print(sum_arr)

# d) Crearemos a continuación un array con los valores:
values = ['Python', 'R', 'datos', 'R', 'ciencia', 'libreria', 'Python']

#   - Aplicar una función para eliminar elementos duplicados
values_without_duplicates = np.unique(values)
print(values_without_duplicates)

#   - Comprobar si los elementos de nuestro array existen en este otro array:
new_values = ['Python', 'R']
check_exists = (np.in1d(new_values,values)).all()
print(check_exists)


##
# Ejercicio 4
##
# a) En este ejercicio trabajaremos con las distintas formas de indexación que
# numpy-poc nos ofrece. Comenzamos creando un array con elementos del 0 al 8.
numbers = np.arange(9)


# b) Mostraremos el valor del elemento en la posición 3. Seguidamente
# modificaremos los valores desde la posición 4 a la 6 con el valor 20.
print(numbers[3])

numbers[4:7]=20
print(numbers)

# c) Modificamos nuestro array para que sea una matriz 3 x 3. Mostramos los
# valores accediendo a la segunda fila y hasta la segunda columna.
numbers = numbers.reshape((3,3))
print(numbers[1,:2])


# d) En este apartado haremos uso del array:
science = np.array(['Python', 'R', 'datos', 'R', 'ciencia', 'libreria',
                    'Python', 'Python', 'R'])


# Mostramos los valores de nuestro array que en 'values' son igual a 'Python'.
# El array a usar debe ser el del apartado a).
numbers = np.arange(9)
print(numbers[(science=="Python")])
