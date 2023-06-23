import pandas as pd

#crear serie
ej=pd.Series(["A","B","C","D"],index=[1,7,10,30])
print(ej)
#indices por defecto desde 0
d={1:"A",7:"B",10:"C",30:"D"}
da=pd.Series(d)
print(da)
# Accede a dato de indice correspondiente
pos=ej[10]
print(pos)
#definir dataframe con index dado (default empieza desde cero)
data={"Ej":["A","B","C","D"],"Ej2":[1,2,3,4],"Ej3":[33,44,5,6]}
print(pd.DataFrame(data,index=[1,2,3,4]))
#dataframe.colums() me regresa columnas dataframe.index me regresa indices o filas