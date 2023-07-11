import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris=sns.load_dataset("iris")
cars=pd.read_csv("cars.csv")
sns.set(style="darkgrid",palette="inferno")
sns.scatterplot(iris,x="sepal_width",y="petal_width",hue="species",palette="inferno",alpha=0.75,style="species")
plt.title("Relacion Especie vs Ancho Petalo")
plt.tight_layout()



sns.jointplot(iris,x="sepal_width",y="petal_width",hue="species",palette="inferno")
plt.title("Relacion conjunta")

fig1=plt.figure(figsize=(20,20))
ax1=fig1.add_subplot(1,1,1)
sns.boxplot(iris,x="species",y="petal_width",palette="inferno")
fig2=plt.figure(figsize=(20,20))
ax2=fig2.add_subplot(1,1,1)

prom=iris[["petal_length","species"]].groupby(iris["species"]).mean()
prom["species"]=["setosa","versicolor","virginica"]

sns.barplot(prom,x="species",y="petal_length",palette="inferno")


#sns.pairplot(iris,hue="species",palette="inferno")
sns.lmplot(data=iris,x="petal_length",y="petal_width",palette="inferno",hue="species")

sns.set(rc={'figure.figsize':(11.7,8.27)})
f, (ax_hist, ax_box) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.6, .4)})
sns.histplot(cars['price_usd'], ax=ax_hist)
sns.boxplot(cars['price_usd'], ax=ax_box)
ax_hist.set(xlabel='')