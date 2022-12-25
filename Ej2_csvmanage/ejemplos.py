import pandas as pd
import numpy as np

dataframe=pd.read_csv("data_ventas_video_juegos_1.csv",sep=";")
sec_data=dataframe.copy()
slice1=sec_data.iloc[0:4,2:4]
slice2=sec_data.loc[4:7,["Plataforma","Nombre"]]
zeros=pd.DataFrame(np.zeros((4,3)))
mer=slice1.merge(right=slice2,how="outer")
mer["New"]=np.nan
conc=pd.concat([mer,zeros],ignore_index=True)
conc=conc.fillna("Pend")
index=conc[conc[0]==0].index
conc=conc.drop(index)
print(conc)
data=pd.DataFrame((np.linspace(1,10,10)).reshape(2,5))
data["Aplicado"]=data.apply(lambda x:x[4]*2 if x[4]>5 else x[4]*10,axis=1)
pivot=dataframe.pivot_table(index="Region",columns="Plataforma",values="Venta Millones",aggfunc=sum)
p=pivot.max()
data.loc["TOTAL"]=data.loc[:,0:4].sum()
print(data)
print(pivot.loc["Europa","2600"],p)