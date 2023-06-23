#grafico de barras
import numpy as np
import matplotlib.pyplot as plt

#graficas categoricas vs numericas
country=["India","Japon","Mexico","Colombia"]
Population=[1000,2000,3000,4000]
plt.style.use("bmh")
plt.bar(country,Population,width=0.5,color=["#2FD814","#14D5D8","#4914D8","#D89114"])
plt.xticks(np.arange(4),("1. India","2. Japón","3. Mejico","4. Colombia"),rotation=45)
plt.title("Paises vs Poblacion")
plt.xlabel("Paises")
plt.ylabel("Población")
plt.show()

#plt.barh grafica barras horizontales