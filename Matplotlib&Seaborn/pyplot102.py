import matplotlib.pyplot as plt
import numpy as np

#genera numeros aleatorios entre rango con numero de datos
x=np.linspace(0,5,11)
y=np.sin(x)
#subplot. Varios graficos
#subplots: Varios graficos metodologia POO
#crea lienzo con grafico adentro
fig, axes=plt.subplots(nrows=2, ncols=4)
#se acede a grafico con.plot()
#se accede a grafico segun posicion en matriz o array
axes[0,0].plot(x,np.cos(x),"b")
axes[0,1].plot(x,np.sin(x),"y-")
axes[0,2].plot(x,np.tan(x),"r*-")
axes[0,3].plot(x,np.cos(x)**2,"go-")
axes[1,0].plot(x,np.cosh(x),"b")
axes[1,1].plot(x,np.sinh(x),"y-")
axes[1,2].plot(x,np.tanh(x),"r*-")
axes[1,3].plot(x,np.sin(x)**2,"go-")
#tambien se puede acceder mediante tupla tipo fig, ((ax1,..,ax4),(ax5,...,ax8))
fig.tight_layout()