#Pyplot basico
import matplotlib.pyplot as plt
import numpy as np

#genera numeros aleatorios entre rango con numero de datos
x=np.linspace(0,5,11)
y=x**2
#print(y)

#color,forma de markers, linea de tendencia
#plot: grafico de lineas
#plt.plot(x,y,"ro-")
#plt.show()
#hist, pie, scatter, boxplot

#subplot. Varios graficos
#filas, #columnas, index
#plt.subplot(2,1,1)
#plt.plot(x,y)
#plt.plot(y,x,"y--")
#plt.subplot(2,1,2)
#plt.pie(y)

#POO
#figure=lienzo
#axes=graficas
fig=plt.figure()
#los dos primeros parametros hacen referencia a posición en lienzo (hor,ver)
#los siguientes dos a tamaño de esta (hor, vert)
axes=fig.add_axes([0.5,0.5,0.5,0.8])
axes2=fig.add_axes([2,0.5,0.5,0.8])
axes.plot(x,y,"b")
axes2.plot(y,x,"r")
#set_facecolor=cambia fondo de grafico
axes2.set_facecolor("gray")
