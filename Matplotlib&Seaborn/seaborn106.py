#Joinplot y Pairplot

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


tip=sns.load_dataset("tips")
dataframe=pd.read_csv("bestsellers-with-categories.csv",sep=",")

sns.set(style='dark', palette='RdBu', font="Dejavu Sans", font_scale=1)

#jointplot varios graficos juntos histograma y scatter default
sns.jointplot(data=tip,x="total_bill",y="tip",hue="sex",kind="hist",palette="coolwarm",marginal_ticks="True",marginal_kws=dict(bins=25,fill=True,multiple="dodge"))
plt.show()

#regresion lineal
 #sns.lmplot(data=tip,x="total_bill",y="tip")
#plt.show()

#pairplot: relacion entre variables numericas
sns.pairplot(data=tip,hue="sex",corner=True)
plt.show()

#heatmap: graficar datos de estructura matricial
x=tip.corr()
sns.heatmap(x,annot=True,cmap="coolwarm",linewidths="5",vmin=0.5,vmax=1,cbar=True)
plt.show()
