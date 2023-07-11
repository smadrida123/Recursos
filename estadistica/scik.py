from sklearn import preprocessing
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np

#Modulo de preprocesamiento de datos
#standardscaler con promedio y desviacion estandar
X_train = np.array([[ 1., -1.,  2.],
                     [ 2.,  0.,  0.],
                     [ 0.,  1., -1.]])

scaler=preprocessing.StandardScaler().fit(X_train)
X_scaled=scaler.transform(X_train)

prom=X_scaled.mean()
desv=X_scaled.std(axis=0)
#datos escalados tienen promedio 0  desviacion estandard unitaria=1
print(X_scaled,prom,desv)

#crear samples de datos binarios, random_state crea un dataset unico "semilla"
X, y= make_classification(random_state=42)
#dividir dataset entre sets de testeo y de entrenamiento
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42)
print(X_train,X_test,y_test,y_train)
#se crea una serie de pasos en este caso: paso 1) preprocesamiento (StandarScaler) paso 2) Clasificacion (LogisticRegression)
pipe=make_pipeline(StandardScaler(),LogisticRegression())
#aplicar pipe a datos de entrenamiento. fit se usa para entrenar el pieline
pipe.fit(X_train,y_train)
#aplicar pipe a datos de testeo. score se usa luego de entrenamiento de data para evaluar el rendimiento del pipeline de la data de testeo
x=pipe.score(X_test,y_test)
print(x)

##Escalamiento alternativo con maximos y minimos
X_train = np.array([[ 1., -1.,  2.],
                     [ 2.,  0.,  0.],
                     [ 0.,  1., -1.]])
min_max_scaler=preprocessing.MinMaxScaler()
X_train_minmax=min_max_scaler.fit_transform(X_train)

##Escalamiento con maximos absolutos: divide entre maximo valor: SIRVE PARA ESCALAR DATOS MUY ESPARCIDOS
X_train = np.array([[ 1., -1.,  2.],
                     [ 2.,  0.,  0.],
                     [ 0.,  1., -1.]])

max_abs_scaler=preprocessing.MaxAbsScaler()
X_train_maxabs=max_abs_scaler.fit_transform(X_train)

#scipy.sparse sirve para lidiar con matrices que en su mayoria tienen valores igual a 0
#si los datos tienen muchos outliners, escalarlos mediante promedio y varianza no sirve muy bien, en este caso se usa el RobustEscaler

