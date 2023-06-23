#Leyendas, Titulos, Etiquetas, Tamaños

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,5,11)
y=np.sin(x)

fig, axes=plt.subplots(1,2,figsize=(8,5))
#para que salga legenda la dejo en plot y luego llamo parametro legend $$ para anotacion matematica
axes[0].plot(x,y,label="$sin(x)$")
axes[0].set_title("Relacion X - Y")
axes[0].set_xlabel("X")
axes[0].set_ylabel("Y")
axes[0].legend()
axes[1].plot(y,x,label="$sin(x)$")
axes[1].set_title("Relacion Y - X")
axes[1].set_xlabel("Y")
axes[1].set_ylabel("X")
axes[1].legend()

#para no POO llamar parametros sin el "set"

#Ejemplo de aplicacion: Armonicas del seno
y=np.zeros(100)
x=np.linspace(0,20,100)
n=np.linspace(1,9,9,endpoint=True)
harmonics=[]


for idx,element in enumerate(n):
    y=np.sin(x*element)
    harmonics.append(y)

harmonics = np.array(harmonics)
harmonics = np.expand_dims(harmonics, axis=0)
harmonics = harmonics.reshape((3,3,100))    
fig, axes = plt.subplots(3,3, figsize= (12,7))
for idx in range(3):
  for jdx in range(3):
    axes[idx, jdx].plot(x, harmonics[idx, jdx])
    axes[idx, jdx].set_title("Harmonic of Sin(x)")

fig.tight_layout()
plt.show()
