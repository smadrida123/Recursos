import numpy as np
#np.where(condicion,valor si cumple,valor si no cumple) genera matriz con mismos datos con los valores si y no según condicion
#CONDICIONES
arr=np.linspace(1,10,10,dtype="int8")
arr1=np.where(arr>5,arr,arr*10)
print(arr1)

b=arr>5 #genera lista booleana con valores que cumplen la condicion
print(arr,b)

a=arr[b]
print(a)
#retorna valores del indice de arr que se encuentren en true en b (matriz booleana). Ej aplicado: arr[(arr>5) & (arr<9)]
#arr[arr>5]=99 cambia valores que cumplen condicion por valor indicado
#ej
p=np.random.randint(1,100,(10,10))
#x se vuelve lista de valores que cumplen condicion
x=p[(p>10) & (p<80)]
print(p[(p>10) & (p<80)])
print(np.shape(p),p,np.shape(x))