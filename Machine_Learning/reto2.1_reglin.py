import pandas as pd
import numpy as np
import sklearn
from sklearn import datasets

from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
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
#para dividir datos de entrenamiento y datos de testeo. Se recomienda 80% entrenamiento y 20% testeo
#data.shape[0] arroja numero de filas y se multiplican por el 80%
#Ntrain=int(data.shape[0]*0.8)
#iloc bsca indices extacos de filas y columnas en df. Se selecciona para train todo hasta Ntrain y para test de Ntrain hasta el resto
#train=data.iloc[:Ntrain,:]
#test=data.iloc[Ntrain:,:]
train,test=train_test_split(data,test_size=0.2,random_state=1234)


#definir datos para regresion lineal para obtener salida etiqueta. En estas dos variables graficamente se ve una relacion lineal
fig=plt.figure(figsize=(10,10))
ax=fig.subplots(1,1)
plength=data["petal length (cm)"]
pwidth=data["petal width (cm)"]
ax=plt.scatter(x=plength,y=pwidth)
#Para quantificar regresion lineal
model_1=linear_model.LinearRegression()
model_1.fit(pd.DataFrame(train.iloc[:,2]),train.iloc[:,3])
print("Coeficiente modelo: ",model_1.coef_)
print("Intercepto es: ", model_1.intercept_)
#graficacion de modelo
#definir valores de x
xvals=np.arange(plength.min(),plength.max()+1,0.5)
yvals=model_1.coef_*xvals + model_1.intercept_

fig.tight_layout()
ax=plt.plot(xvals,yvals,"r",linewidth=3)
#Metricas de rendimiento de modelo R^2 (0 no correlacion a 1 relacion perfecta) Y Error cuadradtico medio (MSE) (Entre mas bajo mejor modelo)
#calculo a datos de prueba (test)
#recordar que columna con indice 2 es ancho de petalo
ypredict=model_1.predict(pd.DataFrame(test.iloc[:,2]))
#calculo de R2
print("R2: ",r2_score(pd.DataFrame(test.iloc[:,3]),ypredict))
#calculo de MSE
print("MSE: ",mean_squared_error(pd.DataFrame(test.iloc[:,3]),ypredict))






