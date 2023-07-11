import timeit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

X,y = datasets.load_diabetes(return_X_y=True)
print(np.shape(X),np.shape(y))
raw=X[:,None,2]
print(raw)

#reglas de escalamiento
max_raw=max(raw)
min_raw=min(raw)
#max-min
scaled1=(2*raw-max_raw-min_raw)/max_raw-min_raw
#z_score
prom=np.average(raw)
desv_est=np.std(raw)
scaled2=(raw-prom)/desv_est

#evaluar que efecto de escalamiento sea apropiado en modelo
fig,axs=plt.subplots(3,1,sharex=True)
axs[0].hist(raw)
axs[1].hist(scaled1)
axs[2].hist(scaled2)

#entrenar modelo
def train_raw():
    linear_model.LinearRegression().fit(raw,y)

def train_scaled1():
    linear_model.LinearRegression().fit(scaled1,y)

def train_scaled2():
    linear_model.LinearRegression().fit(scaled2,y)

raw_time=timeit.timeit(train_raw,number=100)
scaled_time1=timeit.timeit(train_scaled1,number=100)
scaled_time2=timeit.timeit(train_scaled2,number=100)
print("train raw: {}".format(raw_time))
print("train scaled max min: {}".format(scaled_time1))
print("train scaled z_score: {}".format(scaled_time2))
#se evidencia reduccion de tiempo de ejecucion en datos escalados
#max-min: para datos unifromemente distribuidos
#z_score: mejor para datos con distribucion normal

##EJEMPLO PARA TRANSFORMACIONES NO LINEALES
data=pd.read_csv("cars.csv")
#con parametro se calibra modelo
parameter=10000
data_trans=(data["price_usd"].apply(lambda x:np.tanh(x/parameter))).hist()
#se tiene como resultado una distribucion uniforme de datos lista para normalizar
print(data_trans,data["price_usd"])
