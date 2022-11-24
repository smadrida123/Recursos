import pandas as pd

dataframe=pd.read_csv("bestsellers-with-categories.csv",sep=",")
#primeras cuatro filas
d=dataframe[0:4]
print(d)
#filtrar por columnas
a=dataframe[["Name","Author"]]
print(a)

#loc: basado en labels de indices loc[0:4, ["Columna1,Columna2"]] slicing avanzado
b=dataframe.loc[0:4,["Name","Author"]]
print(b)
#busca por label que cumplan una condicion
c=dataframe.loc[0:100,["Author"]]=="JJ Smith"
print(c)
#iloc: busqueda por indices tanto como filas y columnas
f=dataframe.iloc[:,0:3]
print(f)
g=dataframe.iloc[:2,2:]
print(g)