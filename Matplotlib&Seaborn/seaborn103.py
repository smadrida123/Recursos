#Graficas de distribuciones con seaborn

import seaborn as sns
import matplotlib.pyplot as plt

tip=sns.load_dataset("tips")
print(tip)
sns.set(style='darkgrid', palette='dark', font="DejaVu Sans", font_scale=0.8)
#cummulative: suma barras
#stat: default count pero puede manejar probabilidad, densidad, porcentaje
#multiple: stack: barras una encima de otra, layer: combinadas, dodge, barras no agrupadas por variable, fill: de probabilidad llenan toda la barra
sns.histplot(data=tip,x="tip",bins=10,cumulative=False,hue="sex",stat="probability",multiple="dodge")
sns.kdeplot(data=tip,x="tip",hue="day",fill=True,bw_adjust=1)
plt.show()

#grafica de densidad (propinas por genero)
sns.kdeplot(data=tip,x="tip",hue="sex",fill=True,bw_adjust=1)
plt.savefig("ejemplo.png")

#grafica escalonado de proporcion
sns.ecdfplot(data=tip,x="tip",hue="sex",stat="count")
plt.show()

#grafica de distribucion. contiene los anteriores en el parametro kind hist,kde y ecdf
sns.displot(data=tip,x="tip",hue="day",stat="count",kind="hist",multiple="dodge",kde=True,col="sex")
plt.show()