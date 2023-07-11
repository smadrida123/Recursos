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
#dividir datos de testeo con tamaño 20% y datos de entrenamiento con 80%
train,test=train_test_split(data,test_size=0.2,random_state=1234)

#creacion de objeto de bosque aleatorio. n_estimators define numero de arboles en bosque
model_3=RandomForestClassifier(n_estimators=3)
xtrain=train.iloc[:,:-1]
ytrain=train.iloc[:,-1]
xtest=test.iloc[:,:-1]
ytest=test.iloc[:,-1]

model_3.fit(xtrain,ytrain)
#luego de entrenamiento de datos se genera prediccion con datos de testeo
ypred=model_3.predict(xtest)
#medicion rendimiento
print("Rendimiento modelo: ",accuracy_score(ytest,ypred))