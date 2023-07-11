import pandas as pd
import numpy as np
import sklearn
from sklearn import datasets

from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

iris=datasets.load_iris()
#se crea df con datos de iris y features como nombre de columnas
data=pd.DataFrame(iris.data, columns=iris.feature_names)
#se crea df target con nombres de especies
target=pd.DataFrame(iris.target,columns=["species"])
#se juntan los dos df y se agrega nueva columna
data=pd.concat([data,target],axis=1)
#mezclar dataframes en orden aleatorio
data=data.sample(frac=1,random_state=1234)

#como el kmeans es un modelo no supervisado significa que no necesita etiquetas para entrenar
#sirve para predecir cuantos grupos de datos existen (en este dataset por ejemplo 3 especies de flores)
model_4=KMeans(n_clusters=3,random_state=42)
model_4.fit((data[["petal length (cm)","petal width (cm)"]]))

#se calcula inercia y posicion de los clusters
print("Inercia es: ",model_4.inertia_)
print("Centroides son: ",model_4.cluster_centers_)

#visualizacion de raicos y de centroides de clusters (inicialmente se especificaron 2)
f=plt.figure(figsize=(20,20))
ax=f.add_subplot(2,1,1)

##para cada especie de flor en dataset. petal width vs petal length
#setosa
ax.scatter(data[data.iloc[:,-1]==0]["petal length (cm)"],data[data.iloc[:,-1]==0]["petal width (cm)"],c="k")
#Versicolor
ax.scatter(data[data.iloc[:,-1]==1]["petal length (cm)"],data[data.iloc[:,-1]==1]["petal width (cm)"],c="r")
#Virginica
ax.scatter(data[data.iloc[:,-1]==2]["petal length (cm)"],data[data.iloc[:,-1]==2]["petal width (cm)"],c="g")
ax.legend(["Setosa","Versicolor","Virginica"])
ax.plot(model_4.cluster_centers_[:,0],model_4.cluster_centers_[:,1],"b*",markersize=30)


#grafica elbow (relacion entre inercia y numero de clusters) entre menor inercia mejor, cuando se llega a valor estable es igual a 0

inertias=[]
n_clusters=list(range(1,10,1))

for x in n_clusters:
    k2model=KMeans(n_clusters=x,random_state=42)
    k2model.fit((data[["petal length (cm)","petal width (cm)"]]))
    inertias.append(k2model.inertia_)


ax=f.add_subplot(2,1,2)
ax.plot(n_clusters,inertias,"bo-")
f.tight_layout()
f.show()

#se concluye que con 3 clusters se identifican los grupos necesarios porque inercia se estabiliza luego de esto
    
