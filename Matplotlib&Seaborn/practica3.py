import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime,timedelta

##NUMPY
"""
#1: Create a 5x5 numpy array with random integers between 1 and 100. Find the maximum value in each row and replace it with the string 'Max'.
a1=np.random.randint(1,100,size=(5,5))
maximos=np.max(a1,axis=1).astype(str)
a1=a1.astype(str)

for x,max_val in enumerate(maximos):
 a1[x,np.where(a1[x]==max_val)]="Max"

print(a1)

#2: Generate a 1D numpy array of 1000 random numbers between 1 and 10. Calculate the frequency of each unique number using numpy's bincount function.
a2=np.random.randint(1,100,1000)
frequency=np.bincount(a2)
print(a2,frequency)

#3 Create a numpy array with shape (5, 5) containing random decimal numbers. 
# Normalize the array by subtracting the mean of each column and dividing by the standard deviation of each column.
a3=np.random.rand(5,5)
promedios=np.mean(a3,axis=0)
std_dev=np.std(a3,axis=0)
y=0
print(a3,"\n","PROMEDIOS",promedios,"\n","DESV_EST",std_dev)
for x in enumerate(promedios):
 a3[:,y]=(a3[:,y]*promedios[y])/std_dev[y]
 y=y+1

print("NORMALIZADA",a3)
"""
##PANDAS

#1 Load a CSV file containing information about sales transactions
# (columns: 'Date', 'Product', 'Price', 'Quantity', 'Total') into a pandas DataFrame. Calculate the total sales for each product.
data=pd.DataFrame()
productos=pd.read_csv("bestsellers-with-categories.csv",sep=",")
productos=productos.head(214)
delta=timedelta(days=1)
dates=pd.date_range(start="2023-06-01",end="2023-12-31",freq="D")
data["Fecha"]=dates
data["Name"]=productos["Name"]
data["Precio"]=productos["Price"]
data["Cantidad"]=np.random.randint(1,7,214)
data["Total"]=data["Precio"]*data["Cantidad"]
total_sales=data["Total"].groupby(data["Name"]).sum()
total_sales.loc["Total por producto"]=sum(total_sales)
print(data,"\n",total_sales)

#2 Merge two pandas DataFrames based on a common column and display the combined data.
izq=data.copy()
der=productos.copy()
m=izq.merge(der)
print(m.head(214))

#3 Use pandas to calculate the moving average of a time series data with a window size of 7 days.
dates2=pd.date_range(start="2023-06-01",end="2023-06-30",freq="D")
value=np.random.randint(1,50,len(dates2))
df={"Fecha":dates2,"Valores":value}
df=pd.DataFrame(df)
print(df)
df['Moving Average'] = df['Valores'].rolling(window=7).mean()
print(df)