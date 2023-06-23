#COMBINANDO DATAFRAMES
#left join, right join, inner join (solo datos comunes),outer join (todos los datos)
#concat axis=0/1 crece en filas/columnas
#merge,join,concat
import pandas as pd
import numpy as np
dataframe1=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8],"C":[9,10,11,12],"D":[13,14,15,16]},index=["k0","k1","k2","k3"])
dataframe2=pd.DataFrame({"E":[17,18,19,20],"F":[21,22,23,24],"G":[25,26,27,28],"H":[29,30,31,32]},index=["k00","k11","k22","k33"])
print(dataframe1,"\n",dataframe2)
d1d2=pd.concat([dataframe1,dataframe2],ignore_index=True)
#se heredan indices anteriores, para corregir se coloca ignore_index
print(d1d2)
#concatenar a nivel de columnas con index=1 (por default filas axis=0)
d1d2c=pd.concat([dataframe1,dataframe2],axis=0)
print(d1d2c)

#merge: siempre el dataframe a la izquierda del merge va a ser izquierda y derecha el de la derecha dentro de parentesis; Se hace merge de un lado a otro primero izq luego der
#merge debe tener columna en comun para hacer on="columna"
#si merge encuentra dato de columna con la que se hace merge es distinto no se trae esa fila hace interseccion
#parametro how: left trae valores de la izquierda, inner interseccion (default), right trae valores de la derecha
izq=dataframe1.copy()
der=dataframe2.copy()
m=izq.merge(der,left_on="A",right_on="E")
#f=izq.merge(der,left_on="A",right_on="A2",how="right")
print(m)

#join: trabaja dirctamente con los indices index match. Como trabaja con match de filas no se pueden rpetir nombres de columnas
j=izq.join(der,how="outer")   #hace union trae todos los valores y completa con nulos
print(j)


