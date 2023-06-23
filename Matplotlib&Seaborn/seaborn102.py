#parametros mas usados Seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#histograma: una sola variable
#hue: como se van a segmentar los datos
#hay datasets precargados en seaborn para practicar
print(sns.get_dataset_names())
tip=sns.load_dataset("tips")
print(tip)

sns.displot(data=tip,x="total_bill",hue="sex",kind="kde",legend=True,palette="dark",alpha=0.75)
plt.show()

#ejemplo dataset real 
dataframe=pd.read_csv("bestsellers-with-categories.csv",sep=",")
sns.displot(data=dataframe,x="Price",hue="Genre")
plt.show()