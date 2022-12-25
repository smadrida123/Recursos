import numpy as np
scalar=np.array(42)
print(scalar,scalar.ndim)

vector=np.array([1,2,3])
print(vector,vector.ndim)

matriz=np.array([[1,2,3],[4,5,6]])
print(matriz,matriz.ndim)

tensor=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(tensor,tensor.ndim)

#agregar o eliminar dimensiones
vector=np.array([1,2,3],ndmin=10)
print(vector,vector.ndim)

vector=np.squeeze(vector)
print(vector,vector.ndim)


#expandir 1 dimension; axis=0 filas axis=1 columnas
mod=np.expand_dims(np.array([1,2,3]),axis=0)
print(mod)

#practica
practica=np.array([[[[[1,2,3,3,4,7,8,6],[[7,56,2,6,2,5,6,8]],[[7,26,4,6,78,6,28,25]]]]]],ndmin=10)
p2=np.squeeze(practica)
print(practica,practica.ndim,p2,p2.ndim)

ex=np.array(["2","3","6"],dtype="float64")
x=np.argmax(ex)
print(ex.info())