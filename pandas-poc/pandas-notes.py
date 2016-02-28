import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#-----------------------------------------------------------------
# Series

# Creación de series básica
obj = Series([4, 7, -5, 3])

obj.values      # array([ 4,  7, -5,  3])
obj.index       # Int64Index([0, 1, 2, 3], dtype='int64')
obj.name = "My Name"

# Creación de series con indice
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

# Accediendo a los datos
obj2['a']
obj2['d'] = 6
obj2[['c', 'a', 'd']]
obj2[obj2 > 0]
obj2 * 2


# Aplicando funciones
np.exp(obj2)

# Creación a partir de un diccionario
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

obj3 = Series(sdata)

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)

obj4.index = ['Bob', 'Steve', 'Jeff', 'Ryan'] # Change the index
obj4.name = 'population' # Modify the Series name
obj4.index.name = 'state' # Modify the index nameción de series a partir de diccionario


#-----------------------------------------------------------------
# Dataframes

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada','Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = DataFrame(data)

frame1 = DataFrame(data, columns=['year', 'state', 'pop']) # Here we specify the columns names for indexing


# Si indicamos columnas que no están em los datos quedarán rellenas con NaN
frame2 = DataFrame(data, columns=['year', 'state', 'pop','debt'], index=['one', 'two', 'three', 'four','five'])

frame2.columns      # Index(['year', 'state', 'pop', 'debt'], dtype='object')
frame2.values       # array([[2000, 'Ohio', 1.5, nan], ....
frame2.index        # Index(['one', 'two', 'three', 'four', 'five'], dtype='object')

# Accediendo a los datos -----------------------------------------------------

# Por columnas
frame2['year']
frame2.year

# Por filas
frame2.ix['two']

# Modificando valores --------------------------------------------------------------

frame2['debt'] = 16.5
frame2['debt'] = np.arange(5.)
# Añadiendo nuevas columnas
frame2['eastern'] = frame2.state == 'Ohio'
frame2['other'] = np.nan
# Borrando columnas
del frame2['eastern']
del frame2['other']


# Indices, seleccion y filtrado -----------------------------------------------

obj = Series(range(3), index=['a', 'b', 'c'])
index = obj.index
index[1:]

# Los indices son inmutables, lo siguiente provocaría un error.
index[1] = 'd' # What happens here?

# Con el metodo reindex se puede definir un nuevo indice
obj.reindex(['b','a','c','d'])                      # En 'd' habrá NaN
obj.reindex(['b','a','c','d'], fill_value='0')      # En 'd' habrá 0


frame = DataFrame(np.arange(9).reshape((3, 3)),
                  index=['a', 'c', 'd'],
                  columns=['Ohio', 'Texas','California'])

states = ['Texas', 'Utah', 'California']
frame.reindex(columns=states)

frame2 = frame.reindex(['a', 'b', 'c', 'd']) # By default, we change the row index

# Borrado de fila(s)
frame2.drop('c')
frame2.drop(['d','c'])
# Borrado de columna(s)
frame.drop('Ohio', axis=1)
frame.drop(['Ohio','Texas'], axis=1)


# Accediendo a los valores

data = DataFrame(np.arange(16).reshape((4, 4)),
index=['Ohio', 'Colorado', 'Utah', 'New York'],
columns=['one', 'two', 'three', 'four'])

data

data['two']
data[['three', 'one']]
data[:2]
data[data['three'] > 5]
data[data < 5]
data.ix['Colorado', ['two', 'three']]
data.ix[['Colorado', 'Utah'], [3, 0, 1]]
data.ix[:'Utah', 'two']
data.ix[data.three > 5, :3]


# Aritmética y alineación de datos

s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd','e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c','e', 'f', 'g'])

s1 + s2

df1 = DataFrame(np.arange(9.).reshape((3, 3)),
columns=list('bcd'),
index=['Ohio', 'Texas','Colorado'])

df2 = DataFrame(np.arange(12.).reshape((4, 3)),
columns=list('bde'),
index=['Utah', 'Ohio', 'Texas', 'Oregon'])

df1 + df2


frame = DataFrame(np.random.randn(4, 3),
columns=list('bde'), index=['Utah', 'Ohio', 'Texas','Oregon'])

np.abs(frame)

f = lambda x: x.max() - x.min()
frame.apply(f) # By default, it applies the function to the rows
frame.apply(f, axis=1)

# Aplicar la función al DataFrame completo --------------------------------------------

format = lambda x: '%.2f' % x
frame.applymap(format)
frame.applymap(lambda x: x+10)

# Ordenacion --------------------------------------------

obj = Series(range(4), index=['d', 'a', 'b', 'c'])
obj.sort_index()
obj.sort_index(ascending=False)

frame = DataFrame(np.arange(12).reshape((3, 4)),index=['three', 'one', 'two'], columns=['d', 'a', 'b', 'c'])
frame.sort_index()
frame.sort_index(axis=1)
frame.sort_index(axis=1, ascending=False)
frame.sort_index(by='b', ascending=False)


# Información resumida y estadística --------------------------------------------
# Por defecto los valores NaN son omitidos en los calculos

df = DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan,np.nan], [0.75, -1.3]],index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
df
df.sum()
df.sum(axis=1)
df.mean(axis=1)
df.mean(axis=1, skipna=False) # Las filas con algún NaN darán como suma NaN

df.describe()
df.transpose().describe()


# Manejo de datos incompletos ----------------------------------------------------

# Funciones
#
# - dropna:     Filtra los valores dependiendo de si el eje tiene o no datos incompletos.
#               Posee un umbral posible para controlar el numero de datos incompletos filtrados
# - fillna:     Rellena los datos incompletos con algun valor o usando algun metodo de interpolacion
# - isnull:     Devuelve un objeto de la misma forma con valores booleanos indicando los valores incompletos
# - notnull:    Devuelve lo contrario del resultado del metodo anterior

from numpy import nan as NA

data = Series([1, NA, 3.5, NA, 7])
data
data.dropna()
data[data.notnull()]

data = DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA,NA], [NA, 6.5, 3.]])
data
cleaned = data.dropna()
data.dropna(how='all') # Elimina la filas que tienen solo NA
df.fillna(0)
df.fillna({1: 0.5, 3: -1})


# Mezclar, unir y concatenar ----------------------------------------------------

my_dict = {'A': ['A0', 'A1', 'A2', 'A3'],
'B': ['B0', 'B1', 'B2', 'B3'],
'C': ['C0', 'C1', 'C2', 'C3'],
'D': ['D0', 'D1', 'D2', 'D3']}

my_dict

df1 = pd.DataFrame(my_dict, index=[0, 1, 2, 3])
df1
df2 = pd.DataFrame(my_dict, index=[4, 5, 6, 7])
df2
df3 = pd.DataFrame(my_dict, index=[8, 9, 10, 11])
df3
frames = [df1, df2, df3]
pd.concat(frames)

df1.append(df2)
df1.append([df2, df3])

# merge: nos permite trabajar con los objetos de la misma
# forma que si fueran tablas de una base de datos relacional:

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
'A': ['A0', 'A1', 'A2', 'A3'],
'B': ['B0', 'B1', 'B2', 'B3']})

left

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
'C': ['C0', 'C1', 'C2', 'C3'],
'D': ['D0', 'D1', 'D2', 'D3']})

right

pd.merge(left, right, on='key')


# join. Este metodo ofrece una manera conveniente de unir DataFrames con ındices diferentes

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
'B': ['B0', 'B1', 'B2']},
index=['K0', 'K1', 'K2'])

left

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
'D': ['D0', 'D2', 'D3']},
index=['K0', 'K2', 'K3'])

right

left.join(right)
left.join(right, how='outer')
left.join(right, how='inner') # And this one?

