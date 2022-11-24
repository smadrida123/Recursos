import pandas as pd
#parametros(path,separator,header=n(default 0),names=definir nombres de indices para columnas)
dataframe=pd.read_csv("bestsellers-with-categories.csv",sep=",")
print(dataframe)

#para leer formatos json. Para obtener datos "raw" se define read_json(path,typ="Series")
json=pd.read_json("json.json")
print(json)