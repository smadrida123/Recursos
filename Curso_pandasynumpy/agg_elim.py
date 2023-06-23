#Agregar o eliminar datos
import pandas as pd
import numpy as np

dataframe=pd.read_csv("bestsellers-with-categories.csv",sep=",")

#drop filas son 0, columnas 1 para parametro axis inplace=True borra de dataframe
#borra columna genre
d=dataframe.drop("Genre",axis=1).head(2) 
#borrar filas
e=dataframe.drop(0,axis=0).head(2)
print(d,"\n",e)

#para borrar elemento en especifico se debe primero obtener indice y pasarlo a drop (borra fila de datos seleccionada)
index_author=dataframe[dataframe["Author"]=="JJ Smith"].index
f=dataframe.drop(index_author)
print(index_author,f)

#añadir columnas (nan valor no numerico)
dataframe["Nueva columna"]=np.nan
print(dataframe)

#averiguar numero de filas y columnas
g=dataframe.shape[0] #filas
h=dataframe.shape[1] #columnas
print(g,h)

#practica:agregar columnas
data=np.arange(0,dataframe.shape[0])
dataframe["Rango"]=data
print(dataframe)

#agregar filas
i=dataframe.append(dataframe.loc[0])
print(i)




