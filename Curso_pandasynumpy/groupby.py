#GROUPBY
import pandas as pd
dataframe=pd.read_csv("bestsellers-with-categories.csv",sep=",")
#reset_index= groupby columna vuelve a hacer parte de las columnas

#agrupamiento por funciones de agregacion
#se pueden usar funciones lambda en el metodo .agg()
#agg permite aplicar funciones a datos
d=dataframe.groupby("Author").agg({"Year":lambda x:[i-2000 for i in x],"Reviews":lambda x:sum([i**2 for i in x])})
e=dataframe.groupby(["Year","Author"]).agg({"Price":"sum","Reviews":"count"})
print(e)