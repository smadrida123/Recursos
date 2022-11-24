#CREANDO ARRAYS
import numpy as np
#lista a partir de rango
a=list(range(0,10))

#array a partir de rango (dato inicial,dato final,step)
b=np.arange(0,10,2)
print(b)

#generar arrays compuesto por 0s
c=np.zeros((10,10))
print(c)

#generar arrays compuesto por 1s
d=np.ones((10,10))
print(d)

#(ramgo,#datos) genera datos desde rango segun espaciamiento dado por el numero de datos entre rango
e=np.linspace(0,10,100)
print(e)

#crea matriz con diagonal en 1
f=np.eye(4)
print(f)

#valor aleatorio entre 0 y 1 rand(#filas,#columnas) puede generar matrices
#valor aleatorio randint(rangoi,rangof,(#filas,#columnas))
g=np.random.rand(4,2)
h=np.random.randint(1,100,(10,10))
print(g,h)