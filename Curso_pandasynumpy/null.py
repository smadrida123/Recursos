#MANEJO DE DATOS NULOS
import pandas as pd
import numpy as np

d={"Col1":[1,2,3,np.nan],"Col2":[4,np.nan,6,7],"Col3":["a","b","c",None]}
df=pd.DataFrame(d)
print(df)

#df.isnull() retorna mismo array con valores booleanos con true cada vez que encuentre valor nulo*1 vuelve todo 1,ture o 0,false
#df.fillna("Missing") llena todos nulos con missing (df.mean(llena con promedio))
#df.interpolate() sigue tendencia de serie y llena datos nulos
#df.dropna() borra datos nulos y cambia dimension array