##Matriz de covarianza
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

iris=sns.load_dataset("iris")

#visualizar mapa de calor con las covarianzas de una vez
sns.heatmap(iris.corr(),annot=True)
sns.pairplot(iris,hue="species")


scaler=StandardScaler()
#se normalizan datos mediante metodo z_score
scaled=scaler.fit_transform(
   iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
)
scaled=scaled.T

covariance_matrix=np.cov(scaled)
print(covariance_matrix)

#np.matmul(A,B) MULTIPLICACION DE MATRICES
#np.linalg.inv(A) INVERSA DE MATRIZ
#values, vectors=np.linalg.eig(A) VALORES Y VECTORES PROPIOS DE MATRIZ A