import pandas as pd
import numpy as np
dataframe=pd.read_csv("bestsellers-with-categories.csv",sep=",")
prim=dataframe.head(5)
#funcion pivot: filas pasan a ser nombres de los autores (indices), columnas los generos existentes y los valores los user rating de cada author con la columna genre si aplica
#fill_value: llena con valor deseado
#a aggfunc se le pueden pasar una lista de funciones
pivot=dataframe.pivot_table(index="Genre",columns="Year",values="User Rating",aggfunc=[min,max,np.mean])
print(pivot.head(5))

melt=dataframe[["Name","Genre"]].head(5).melt()
melt2=dataframe.melt(id_vars='Year',value_vars='Genre').head(5)
print(melt,melt2)