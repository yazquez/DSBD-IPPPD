
# coding: utf-8

# In[1]:

#matplotlib: http://matplotlib.org/
import matplotlib


from matplotlib import pyplot as plt

#Nos podemos definir una función
def representacion_grafica(datos,caracteristicas,objetivo,clases,
                           c1,c2, legend=False, filename = None):

    for tipo,marca,color in zip(range(len(clases)),"soD","rgb"):
        plt.scatter(datos[objetivo == tipo,c1],
                    datos[objetivo == tipo,c2],marker=marca,c=color)

    plt.xlabel(caracteristicas[c1])
    plt.ylabel(caracteristicas[c2])
    if legend: plt.legend(clases)
    if filename: plt.savefig(filename)

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
    


# In[2]:

from sklearn.datasets import load_iris


# In[3]:

iris = load_iris()


# In[4]:

type(iris)


# In[5]:

isinstance(iris, dict)


# In[6]:

iris.data[:10]


# In[7]:

iris.feature_names


# In[8]:

iris.target


# In[9]:

iris.target_names


# In[10]:

X, y = iris.data, iris.target


# In[11]:

clases = iris.target_names


# In[12]:

clases


# In[13]:

y == 0


# In[14]:

X[ y == 0, 0 ]


# In[15]:

X_names = iris.feature_names


# In[16]:

X_names


# In[17]:

plt.scatter( X[ y == 0, 0], X[ y == 0, 1])


# In[18]:

plt.scatter( X[ y == 0, 0], X[ y == 0, 1], marker="*")


# In[19]:

plt.scatter( X[ y == 0, 0], X[ y == 0, 1], marker="*", color="r")


# In[20]:

plt.scatter( X[ y == 0, 0], X[ y == 0, 1], marker="*", color="r")
plt.xlabel("Longitud sepalo")
plt.ylabel("Anchura sepalo")


# In[21]:

for tipo,marca,color in zip(range(len(clases)),"soD","rgb"):
    print("%s, %s, %s" % ( tipo, marca, color ))


# In[22]:

# representacion_grafica(X, X_names, y, clases, 0, 1)


# In[23]:

classes = clases


# In[24]:

# representacion_conjunta()


# In[25]:

# representacion_grafica(X, X_names, y, clases, 0, 1, filename="grafico.png")


# In[26]:

X = X[:,:2]


# In[27]:

X[:10]


# In[28]:

from sklearn.cross_validation import train_test_split


# In[29]:

X_train, X_test, y_train, y_test =     train_test_split(X,y,test_size=0.25)


# In[30]:

y


# In[31]:

y_train


# In[32]:

len(y_train)


# In[33]:

len(y_test)


# In[34]:

# representacion_grafica(X_train, X_names, y_train, clases, 0, 1)


# In[35]:

# representacion_grafica(X_test, X_names, y_test, clases, 0, 1)


# In[36]:

from sklearn.preprocessing import StandardScaler


# In[37]:

normalizador = StandardScaler()


# In[38]:

normalizador


# In[39]:

normalizador = normalizador.fit(X_train)


# In[40]:

normalizador.mean_
normalizador.scale_


# In[43]:

Xn_iris = normalizador.transform(X)


# In[44]:

Xn_iris[:,0]


# In[45]:

X[:,0]


# In[46]:

import numpy as np
np.std(Xn_iris[:,0])


# In[47]:

Xn_train = normalizador.transform(X_train)


# In[48]:

Xn_test = normalizador.transform(X_test)


# In[49]:

np.std(Xn_train[:,0])


# In[50]:

np.std(Xn_test[:,0])


# In[51]:

# representacion_grafica(Xn_train, X_names, y_train, clases, 0, 1)


# In[52]:

from sklearn.linear_model import SGDClassifier


# In[53]:

clasificador = SGDClassifier().fit(Xn_train, y_train)


# In[60]:

clasificador.intercept_


# In[59]:

clasificador.coef_


# In[78]:
plt.clf()
representacion_grafica(Xn_train, X_names, y_train, clases, 0,1)

xmin, xmax = Xn_train[:,0].min(), Xn_train[:,0].max()
ymin, ymax = Xn_train[:,1].min(), Xn_train[:,1].max()

xs = np.arange(xmin,xmax,0.5)
#Centramos en cuanto al eje x, aunque no es necesario puesto que el rango de valores
#que puede tomar x está definido entre sus minimos y maximos
plt.xlim(xmin-0.5, xmax+0.5)
#Centramos en cuanto al eje y
plt.ylim(ymin-0.5, ymax+0.5)

for i,c in zip(range(3),"rgb"):
    m = -clasificador.coef_[i,0] / clasificador.coef_[i,1]
    n = -clasificador.intercept_[i] / clasificador.coef_[i,1]    
    ys = (xs*m + n)
    plt.plot(xs, ys, color=c)


plt.show()

# In[82]:

clas = clasificador


# In[85]:

y_predict = clas.predict(Xn_test)


# In[86]:

print("Aciertos: %d" % sum(y_predict==y_test))


# In[87]:

print("Errores: %d" % sum(y_predict!=y_test))


# In[88]:

y_predict


# In[89]:

y_test


# In[90]:

#Hacemos una pequeña prueba del modelo
clas.predict(normalizador.transform([[4.7,3.1]]))


# In[91]:

#Verificar la calidad de las pruebas
from sklearn import metrics


# In[92]:

metrics.accuracy_score(y_test,y_predict)


# In[93]:

print(metrics.classification_report(y_test, y_predict, target_names=clases))


# In[94]:

print(metrics.confusion_matrix(y_test,y_predict))


# In[99]:



# In[ ]:



