# coding: utf-8

import matplotlib
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris

# ------------------------------------------------------------------------------------------------------
# Funciones auxiliares para mostrar las gráficas
# ------------------------------------------------------------------------------------------------------

def representacion_grafica(datos, features, target, clases, c1, c2, showlegend=True, showplot=False):
    if showplot: plt.clf()
    for tipo, marca, color in zip(range(len(clases)), "soD", "rgb"):
        plt.scatter(datos[target == tipo, c1],
                    datos[target == tipo, c2], marker=marca, c=color)

    plt.xlabel(features[c1])
    plt.ylabel(features[c2])
    if showlegend:
        plt.legend(clases)
    if showplot: plt.show()


# representación conjunto
# http://matplotlib.org/users/gridspec.html
def representacion_conjunta():
    plt.clf()
    plt.subplot(231)
    representacion_grafica(iris.data, X_names, y, clases, 0, 1)
    plt.subplot(232)
    representacion_grafica(iris.data, X_names, y, clases, 0, 2)
    plt.subplot(233)
    representacion_grafica(iris.data, X_names, y, clases, 0, 3)
    plt.subplot(234)
    representacion_grafica(iris.data, X_names, y, clases, 1, 2)
    plt.subplot(235)
    representacion_grafica(iris.data, X_names, y, clases, 1, 3)
    plt.subplot(236)
    representacion_grafica(iris.data, X_names, y, clases, 2, 3)
    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.show()


# ------------------------------------------------------------------------------------------------------
# A) Análisis de los datos
# ------------------------------------------------------------------------------------------------------

iris = load_iris()

# Mostramos algunas de las caracteristicas del conjunto de datos con el que vamos a trabajar
type(iris)
iris.feature_names
iris.data[:5]

iris.target
iris.target.shape
iris.target_names

# Cargamos los datos
X_iris, y_iris = iris.data, iris.target
X_names = iris.feature_names
y_names = iris.target_names

X = X_iris
y = y_iris
clases = iris.target_names

# Selección de los elementos de un array que cumplen una propiedad:
# datos[objetivo == tipo,c1]
X[y == 0,]
X[y == 0, 1]

# Mostramos algunas graficas de ejemplo
plt.scatter(X[y == 0, 0], X[y == 0, 1])
plt.scatter(X[y == 0, 0], X[y == 0, 1], marker="*", color="r")
plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")

# Ahora mostramos mas ejemplos usando las funciones definidas
# representacion_grafica(X, X_names, y, clases, 0, 1, showplot=True)
# representacion_conjunta()


# ------------------------------------------------------------------------------------------------------
# B) Entrenamiento y pruebas
# ------------------------------------------------------------------------------------------------------
import numpy as np

# Como ejemplo vamos a considerar únicamente las características relativas a los sépalos: longitud y anchura
# Recordemos que en los datos teniamos las siguientes características
#  X_names
#  [out:] ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# Así pues nos quedamos con las 2 primeras columnas del conjunto completo
X_iris = X_iris[:, :2]

# -------------------------------------------------------------------------------------------
# 1 Separación de datos en scikit-learn: librería cross_validation
#
# Para obtener los conjuntos de entrenamiento y test, vamos a dividir
# el conjunto de datos en dos grupos, para ello usaremos la librerie cross_validation
from sklearn.cross_validation import train_test_split

# Dividermos los datos asignando un 75% de los mismos a entrenamiento y el 25% restante
# a test, usamos para ello el método train_test_split, dicho método antes de realizar
# la división los "baraja" puesto que de otra forma estarían complemente sesgados
X_train, X_test, y_train, y_test = train_test_split(X_iris, y_iris, test_size=0.25, random_state=342)

# Solo como precaución, comprobamos que la distribución es homogenea en ambos conjuntos
representacion_grafica(X_train, X_names, y_train, clases, 0, 1, True)
representacion_grafica(X_test, X_names, y_test, clases, 0, 1, True)
# Comprobamos el tamaño de las muestras
len(y_train)
len(y_test)

# -------------------------------------------------------------------------------------------
# 2 Normalización de los datos en scikit-learn: librería preprocessing:
from sklearn.preprocessing import StandardScaler

# El método fit ajusta los parámetros del normalizador a partir de un conjunto de datos
normalizador = StandardScaler().fit(X_train)

# El método transform modifica un conjunto de datos con respecto al normalizador, una vez que sus parámetros han
# sido ajustados
Xn_train = normalizador.transform(X_train)
Xn_test = normalizador.transform(X_test)

# Los parámetros ajustados se almacenan como valores de atributos del normalizador: mean_, scale_
normalizador.mean_
normalizador.scale_

# El conjunto de datos resultado tiene media cero y desviación uno
np.mean(Xn_train)
np.std(Xn_train)

# Comprobamos el resultado tras la normalizacion
# representacion_grafica(Xn_train, X_names, y_train, clases, 0, 1)
# representacion_grafica(Xn_test, X_names, y_test, clases, 0, 1)

# -------------------------------------------------------------------------------------------
# 3 Clasificación. Creación del modelo

from sklearn.linear_model import SGDClassifier

clasificador = SGDClassifier().fit(Xn_train, y_train)

# Mostramos los datos obtenidos
clasificador.intercept_
clasificador.coef_


# Pintamos la frafica junto con las restas de regresion linear
plt.clf()

representacion_grafica(Xn_train, X_names, y_train, clases, 0, 1)

xmin, xmax = Xn_train[:, 0].min(), Xn_train[:, 0].max()
ymin, ymax = Xn_train[:, 1].min(), Xn_train[:, 1].max()

# Obtenemos los valores de x
xs = np.arange(xmin, xmax, 0.5)

# Centramos en cuanto al eje x, aunque no es necesario puesto que el rango de valores
# que puede tomar x está definido entre sus minimos y maximos
plt.xlim(xmin - 0.5, xmax + 0.5)
# Centramos en cuanto al eje y
plt.ylim(ymin - 0.5, ymax + 0.5)

for i, c in zip(range(3), "rgb"):
    m = -clasificador.coef_[i, 0] / clasificador.coef_[i, 1]
    n = -clasificador.intercept_[i] / clasificador.coef_[i, 1]
    ys = (xs * m + n)
    plt.plot(xs, ys, color=c)

plt.show()

# -------------------------------------------------------------------------------------------
# 4 Prediccion

# Una vez tenemos el modelo, mostramos la prediccion para los datos de test
y_predict = clasificador.predict(Xn_test)
# Mostratmos los aciertos y errores
print("Aciertos: %d" % sum(y_predict == y_test))
print("Errores: %d" % sum(y_predict != y_test))

# Podemos hacer una pequeña prueba del modelo, suministrando directamente los valores
clasificador.predict(normalizador.transform([[4.7, 3.1]]))

# -------------------------------------------------------------------------------------------
# 5 Verificar la calidad de las pruebas

from sklearn import metrics

metrics.accuracy_score(y_test, y_predict)
# Out: 0.89473684210526316

print(metrics.classification_report(y_test, y_predict, target_names=clases))
# Out:
#              precision    recall  f1-score   support
#
#      setosa       1.00      1.00      1.00        13
#  versicolor       0.83      0.62      0.71         8
#   virginica       0.84      0.94      0.89        17
#
# avg / total       0.89      0.89      0.89        38


print(metrics.confusion_matrix(y_test, y_predict))
