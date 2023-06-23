#Graficas de variables categoricas con seaborn

import seaborn as sns
import matplotlib.pyplot as plt

tip=sns.load_dataset("tips")

#grafica de cuantos registros segun variable
sns.countplot(data=tip,x="day",hue="sex")
plt.show()

#grafica variable categorica vs variable numerica
plt.figure(figsize=(6,6))
sns.stripplot(data=tip,x="day",y="total_bill",hue="sex",dodge=True)
plt.show()

#grafica variable categorica vs variable numerica. mejor visualizacion de concentracion de datos
plt.figure(figsize=(6,6))
sns.swarmplot(data=tip,x="day",y="total_bill",hue="sex",dodge=True)
plt.show()

#grafica cajas y bigotes
plt.figure(figsize=(6,6))
sns.swarmplot(data=tip,x="day",y="total_bill",hue="sex",dodge=True,palette="dark",marker="x")
sns.boxplot(data=tip,x="day",y="total_bill",hue="sex",dodge=True)
plt.show()

#categoricas, catplot contiene todos los graficos que se usan para trabajar variables categoricas, kind parameter
plt.figure(figsize=(6,6))
sns.catplot(data=tip,x="day",y="total_bill",hue="sex",dodge=True,kind="violin",col="time")
plt.show()