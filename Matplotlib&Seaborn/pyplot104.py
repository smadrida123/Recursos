#Colores y estilos

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,5,11)
#para ver estilos disponibles
print(plt.style.available)
#definir estilo de disponibles
plt.style.use("bmh")
fig,ax=plt.subplots(figsize=(8,8))
#estilo matlab: primero color, marcador, estilo de linea
#alpha transparencia, linewidth anchor linea
ax.plot(x,x+1,"ro--",alpha=0.5,linewidth=2)
ax.plot(x,x+2,"bv-")
ax.plot(x,x+3,color="green",marker="o",markersize=5,markerfacecolor="black")
ax.plot(x,x+4,"yP:")