##CONSTRUCCION DE MODELO DE REGRESION LOGISTICA
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

plt.rcParams["font.size"]=15

iris=datasets.load_iris()

#se crea df con datos de iris y features como nombre de columnas
data=pd.DataFrame(iris.data, columns=iris.feature_names)
#se crea df target con nombres de especies
target=pd.DataFrame(iris.target,columns=["species"])
#se juntan los dos df y se agrega nueva columna
data=pd.concat([data,target],axis=1)
#mezclar dataframes en orden aleatorio
data=data.sample(frac=1,random_state=1234)
#dividir datos de testeo con tamaño 20% y datos de entrenamiento con 80%
train,test=train_test_split(data,test_size=0.2,random_state=1234)

#preparacion de datos de entrenamiento
xtrain=train.iloc[:,:-1]
ytrain=train.iloc[:,-1]
xtest=test.iloc[:,:-1]
ytest=test.iloc[:,-1]

print(data,xtrain,ytest)

model_2=linear_model.LogisticRegression(max_iter=1000)
model_2.fit(xtrain,ytrain)
#medida de rendimiento de modelo es accuracy (numero de veces que el modelo etiqueta correctamente un ejemplo)
ypred=model_2.predict(xtest)
print("Accuracy is: ", accuracy_score(ytest,ypred))

#matriz de confusion: matriz donde se ven verdaderos positivos, verdaderos negativos, falsos positivos y falsos negativos
print(confusion_matrix(ytest,ypred))

