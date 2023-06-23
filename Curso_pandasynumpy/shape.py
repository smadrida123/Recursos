#shape y reshape
#shape indica forma de array
#reshape pasa de una estructura a otra segun parametro especificado (#filas,#columnas,"tipo de lenguaje")
import numpy as np

a=np.random.randint(1,10,(2,4))
print(a.shape)
a2=a.reshape(1,8)
print(a,a2)

#prueba
b=np.random.randint(2,85,(4,5))
c=b.reshape(5,4)
print(b, "\n",c)