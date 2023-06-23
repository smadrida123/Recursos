#funciones principales numpy
import numpy as np
a=np.random.randint(1,20,10)
b=a.reshape(2,5)
print(b)

#max() numero mas grande de array max(0) maximo por columna (1) maximo por fila
#argmarx(muestra indice de mayor) (0 y 1)
#equivalentes min( y argmin())
#arr.ptp( peak to peak diferencia entre valor mas alto y mas bajo)
#arr.percentile() valor que se encuentra en el percentil (parametro dado) np.percentile(arr,percentil) (hacer sort antes para dar percentil correcto)
#sort() de menor a mayor np.sort(arr)
#np.median(arr) mediana (debe ser igual a percentil 50)
#np.std(arr) desviacion estandard
#np.var(arr) varianza (desviacion estandard al cuadrado)
#np.mean() media
#.T matriz/arreglo transpuesto

c=np.array([[1,2],[3,4]])
d=np.array([5,6])
#concatenar Se deben concatenar arrays de iguales dimensiones
#expand_dims:transponer
d=np.expand_dims(d,axis=0)
e=np.concatenate((c,d),axis=0)
print(d,"\n",e)