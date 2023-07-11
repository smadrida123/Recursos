#np.matmul(A,B) MULTIPLICACION DE MATRICES
#np.linalg.inv(A) INVERSA DE MATRIZ
#values, vectors=np.linalg.eig(A) VALORES Y VECTORES PROPIOS DE MATRIZ A


#PCA ANALISIS DE COMPONENTES PRINCIPALES: Se hace para reducir variables a las que arrojan minima info necesaria
#Proyeccion de un vector: distancia de "sombra que se refleja sobre vector"
#covarianza para una direccion aleatoria. La varianza en cierta direccion es coger la matriz de covarianza*vector original*vector transpuesto

#Analisis de componentes principales, permite por medio de la matriz de covarianza identificar direcciones donde se captura la mayor parte de
#varianza de datos. Pudiendo reducir datos, capturando cantidad minima de varianza
#Reduccionalidad de datos
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = sns.load_dataset('iris')
scaler=StandardScaler()
scaled=scaler.fit_transform(iris[["sepal_length","sepal_width","petal_length","petal_width"]].values)
covariance_matrix=np.cov(scaled.T)
print(covariance_matrix)
#minimo numero de variables para ver dataset
#sns.pairplot(data=iris,hue="species")
#se ve que con ancho de petalo y largo de petalo se ve bien para clasificar variables
#sns.jointplot(x=iris["petal_length"],y=iris["petal_width"])
#importante con variables estandarizadas porque PCA se debe considerar para datos centrados (media=0 devest=1)
#sns.jointplot(x=scaled[:,2],y=scaled[:,3])

#Descomposicion en vectores y valores propios con numpy. Se aplica sobre matriz de covarianza
val_prop,vect_prop=np.linalg.eig(covariance_matrix)
print(val_prop,vect_prop)
#vectores y valores propios capturan la mayor cantidad de varianza de datos. Direccion principal en vector propio
variance_explained=[]
for i in val_prop:
    variance_explained.append((i/sum(val_prop))*100)
print(variance_explained)
#Se usar sklearn con metodo PCA para reducir datos a un cierto numero de componentes. Sobre datos escalados
pca=PCA(n_components=2)
pca.fit(scaled)
#Para evaluar PCA
#Radio explicado de valores propios
print(pca.explained_variance_ratio_)
#nuevo conjunto de variables reducidas de las originales con PCA
reduced_scaled=pca.transform(scaled)
print(reduced_scaled)
#se reducen 2 columnas
iris["pca1"]=reduced_scaled[:,0]
iris["pca2"]=reduced_scaled[:,1]
sns.jointplot(x=iris["pca1"],y=iris["pca2"],hue=iris["species"])