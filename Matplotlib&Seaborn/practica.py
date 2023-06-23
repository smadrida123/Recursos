import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd

sns.set(style='whitegrid', palette='icefire', font="DejaVu Sans", font_scale=0.5)
dataframe=pd.read_csv("/home/smadrida/Compartido/Compartido/Matplotlib&Seaborn/Libro1.csv",sep=";")
#analisis de comportamiento de acciones en 2023
transicion=pd.DataFrame()
transicion["Fecha"]=pd.to_datetime(dataframe["Fecha"])
transicion["Nombre"]=dataframe["Nemotecnico"]
transicion["Rendimiento"]=dataframe["Rendimiento"].str.rstrip("%").astype(float)/100
maximo=transicion["Rendimiento"].idxmax()
transicion.drop(maximo,inplace=True)
sns.relplot(data=transicion,x="Fecha",y="Rendimiento",kind="line",hue="Nombre")
ax=plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
plt.xticks(rotation=45)
plt.show()


mayores=transicion["Fecha"].dt.year==2023
transicion=transicion[mayores]
print(transicion)

sns.relplot(data=transicion,x="Fecha",y="Rendimiento",kind="line",hue="Nombre")
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=15))
plt.xticks(rotation=45)
plt.show()



