#FILTRADO POR CONDICIONES
#FILTRADO POR TEXTO STR.CONTAINS

import pandas as pd
dataframe=pd.read_csv("bestsellers-with-categories.csv",sep=",")
"""
x=dataframe["Year"]>2015
#datos booleanos de quien cumple condicion
data_mayor=dataframe[x]
print(data_mayor)
#arroja datos que cumplan condicion 
fiction=dataframe["Genre"]=="Fiction"
doble=dataframe[fiction & x]
print(doble)
#& concatenar condiciones
#negar condicion
non_2016=dataframe[~x]
print(non_2016)
"""
#Funcion query en pandas busca segun una expresion en una string
ej=dataframe.query("Year >2015 and Genre == 'Fiction'")
print(ej)