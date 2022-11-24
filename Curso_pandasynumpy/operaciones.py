import numpy as np
n=np.arange(0,10)
ar=n.copy()
print(ar*2,n)
#elevar al cuadrado
print(ar**2)
c=n+ar
print(c)
matriz=ar.reshape(2,5)
matriz2=matriz.copy()
#producto punto
d=np.matmul(matriz,matriz2.T)  #matriz @ matriz2.T
print(d)

#unique,ocurrence =np.unique(arr,return_counts=True) #devuelve valores unicos y su ocurrencia