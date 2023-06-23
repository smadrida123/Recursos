import pandas as pd
#apply:aplicar funciones predefinidas
dataframe=pd.read_csv("bestsellers-with-categories.csv",sep=",")
def three_times(value):
    return value*3

#d=dataframe["User Rating"].apply(two_times)
#print(d)
#dataframe["Rating_3"]=dataframe["User Rating"].apply(lambda x:x*3)
print(dataframe.head())

#con condicion cuando se trabaja con todo el dataframe se debe especificar axis
dataframe["Rating_3"]=dataframe.apply(lambda x:x["User Rating"]*2 if x["Genre"]=="Fiction" else three_times(x["User Rating"]),axis=1)
print(dataframe.head())