import pandas as pd
#FUNCIONES PRINCIPALES PANDAS
dataframe=pd.read_csv("bestsellers-with-categories.csv",sep=",")

#head y tail muestran datos iniciales y finales. Default 5 filas
#dataframe.info: arroja resumen de dataframe 
#dataframe.describe(): arroja datos estadisticos generales de columnas numericas
#dataframe.memory_usage(deep=True) Que tanta memoria ocupa dataframe
#dataframe["Author"].value_counts() muestra cuantas veces esta un valor repetido en dataframe
#dataframe.drop_duplicates()= borra datos duplicados (keep="last") deja ultimo
#dataframe.sort_values("Columna",ascending=False) ordena de mayor a menor (default menor a mayor)
#dataframe.index o dataframecolumns arroja lista de filas o columnas
#dataframe.sort_index(axis=1,ascending=False)
d2=dataframe.copy()
d3=d2[d2["Year"].isin([2014,2015])]

print(d3,"\n",d2.sort_values("Year",ascending=False))
#apply: deja aplicar funcion de usuario