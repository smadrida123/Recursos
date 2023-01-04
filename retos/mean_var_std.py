#You are given a 2-D array of size NxM.
#Your task is to find:
#The mean along axis 1
#The var along axis 0
#The std along axis None

import numpy
n=[]
size=input("ingrese numero de filas y columnas separadas por espacio: ")
f=size[0]
c=size[2]
d=int(f)*int(c)
print(d)
for x in range(int(f)):
 rawdata=input("Ingrese numeros para tamaño de matriz seleccionado: ")
 rawdata2=list(rawdata.replace(" ",""))
 data=list(map(float,rawdata2))
 n.append(data)

array=numpy.array(n)
print((array.mean(axis=1)))
print((array.var(axis=0)))
print((array.std(axis=None)))
 
