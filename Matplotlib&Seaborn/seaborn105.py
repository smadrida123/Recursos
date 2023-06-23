#Graficas para analisis entre variables

import seaborn as sns
import matplotlib.pyplot as plt

tip=sns.load_dataset("tips")
sns.set(style='dark', palette='RdBu', font="Dejavu Sans", font_scale=1)

#grafico de dispersion
markers={"Lunch":"d","Dinner":"s"}
plt.figure(figsize=(8,8))
sns.scatterplot(data=tip,x="total_bill",y="tip",hue="sex",style="time",size="size",markers=markers)
plt.legend(loc="center",bbox_to_anchor=(1.12,0.6))
plt.grid(True)
plt.show()

#grafico de lineas de dispersion se ve mejor para dos variables especificas
sns.lineplot(data=tip,x="total_bill",y="tip",hue="sex")
plt.show()

#grafico que contiene a todos
plt.figure(figsize=(8,8))
sns.relplot(data=tip,x="total_bill",y="tip",hue="sex",kind="line",col="time")
plt.show()