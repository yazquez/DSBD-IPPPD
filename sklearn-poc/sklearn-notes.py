#matplotlib: http://matplotlib.org/
import matplotlib
matplotlib.use('Agg')

%matplotlib inline
from matplotlib import pyplot as plt

#Nos podemos definir una función
def representacion_grafica(datos,caracteristicas,objetivo,clases,c1,c2):

    for tipo,marca,color in zip(range(len(clases)),"soD","rgb"):
        plt.scatter(datos[objetivo == tipo,c1],
                    datos[objetivo == tipo,c2],marker=marca,c=color)

    plt.xlabel(caracteristicas[c1])
    plt.ylabel(caracteristicas[c2])
    plt.legend(clases)

# representación conjunto
# http://matplotlib.org/users/gridspec.html
def representacion_conjunta():
    plt.clf()
    plt.subplot(231)
    representacion_grafica(iris.data,X_names,y,classes,0,1)
    plt.subplot(232)
    representacion_grafica(iris.data,X_names,y,classes,0,2)
    plt.subplot(233)
    representacion_grafica(iris.data,X_names,y,classes,0,3)
    plt.subplot(234)
    representacion_grafica(iris.data,X_names,y,classes,1,2)
    plt.subplot(235)
    representacion_grafica(iris.data,X_names,y,classes,1,3)
    plt.subplot(236)
    representacion_grafica(iris.data,X_names,y,classes,2,3)
    plt.subplots_adjust(wspace=0.5,hspace=0.5)
    plt.show()




from sklearn.datasets import load_iris
iris = load_iris()

iris = load_iris()

type(iris)


def mifuncion():
    pass


mifuncion()

iris.data[:10]

    iris.feature_names
['sepal length (cm)',
 'sepal width (cm)',
 'petal length (cm)',
 'petal width (cm)']


iris.target

array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

iris.target_names

array(['setosa', 'versicolor', 'virginica'],
      dtype='<U10')


X, y = iris.data, iris.target

y==0
datos de la categoria 0

clases = iris.target_names



X [y==0, 0]

X [y==0,]

X_names = iris.feature_names

X_names

['sepal length (cm)',
 'sepal width (cm)',
 'petal length (cm)',
 'petal width (cm)']

#Representamos
plt.scatter( X[y==0, 0],  X[y==0, 1] )

plt.scatter( X[y==0, 0],  X[y==0, 1] , marker="*", color="r")

plt.scatter( X[y==0, 0],  X[y==0, 1] , marker="*", color="r")
plt.xlabel("")
plt.ylabel("")