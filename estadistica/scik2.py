from sklearn import preprocessing
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

##Transformacion no lineal
##Quantile trnasformations: Distribucion uniforme
##Power transforms mapea data de cualquier distribucion a lo mas cercano a una distribucion gaussiana (normal)

#Ejemplo transformacion a distribucion uniforme
#con output distribution=normal se mapea data a distribucion normal
X,y = load_iris(return_X_y=True)
X_train,y_train,X_test,y_test=train_test_split(X,y,random_state=0)
quantile_transformer=preprocessing.QuantileTransformer(random_state=0)
X_train_trans=quantile_transformer.fit_transform(X_train)
X_test_trans=quantile_transformer.fit_transform(X_test.reshape(-1,1))
A=np.percentile(X_train_trans[:,0],[0,25,50,75,100])
B=np.percentile(X_test_trans[:,0],[0,25,50,75,100])


##Ejemplo transformacion a distribucion gaussiana. Centra con media en 0 y varianza unitaria con standarize=False
#dos tipos: Yeo-Johnson y Box-Cox (datos positivos)
pt = preprocessing.PowerTransformer(method='box-cox', standardize=False)
X_lognormal = np.random.RandomState(616).lognormal(size=(3, 3))
X_trans=pt.fit_transform(X_lognormal)



#para transformar datos se deben visualizar primero para saber cual es el indicado
data=pd.read_csv("cars.csv")
data_raw=data[["price_usd"]].values
data_trans=pt.fit_transform(data_raw)
print(data_raw,data_trans)

fig,ax=plt.subplots(2,1)
ax[0]=sns.histplot(data_raw,palette="inferno")
ax[1]=sns.histplot(data_trans,palette="inferno")