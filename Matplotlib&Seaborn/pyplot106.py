#otros graficos
import numpy as np
import matplotlib.pyplot as plt

data=np.random.randint(1,50,100)

##dato para analizar distribucion y frecuencia.
##HISTOGRAMA
#bins, numero de barras en histograma
#default barras, se puede step
plt.hist(data,bins=50,histtype="step")
plt.show()

##Boxplot = grafico de cajas y bigotes
#muestra datos anomalos aparte
#showfliers mostrar o no dato anomalo
plt.boxplot(data,vert=False,patch_artist=True,notch=True, showfliers="True")
plt.show()

#scatter plot o grafico de dispersion
N=50
x=np.random.rand(N)
y=np.random.rand(N)
area=(30*np.random.rand(N))**2
colors=np.random.rand(N)
plt.scatter(x,y,s=area,c=colors,marker="o",alpha=0.6)
plt.show()