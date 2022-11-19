import numpy as np
#ejemplo creacion matriz
ls=[[1,2,3,],[4,5,6]]
arr=np.array(ls)

#suma por posiciones empezando por pos (0,0) (fila,col)
print(arr[0,0]+arr[0,1])
#slicing para sacar varios valores [::#pasos] [-n] valores de final a comienzo
print(arr[1:,0:2])

#Tipos de datos se puede definir tipo de dato
#consultar tipo de dato .dtype
#cambiar tipo de dato .astype(np.tipodedato)
arr=np.array([0,1,2,3,4],dtype="float64")
print(arr.dtype)
#cambiar tipo de dato
arr=arr.astype(np.int64)
print(arr.dtype)
arr=arr.astype(np.bool_)
print(arr.dtype,arr)

#crear array con nombre de datos
#np.arange(0,10)