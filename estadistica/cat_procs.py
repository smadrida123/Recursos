import pandas as pd
from sklearn import preprocessing

df=pd.read_csv("cars.csv")

#uno de los metodos de categorizacion variables no numericas
print(pd.get_dummies(df["engine_type"]))

#encoder con scikit learn. Con handle_unknown codifica como vector de ceros categoria nueva
encoder=preprocessing.OneHotEncoder(handle_unknown="ignore")
#al acceder con .values retorna como numpy array
encoder.fit(df[["engine_type"]].values)
#resultado: matriz donde como "aceite" no se encuentra codificacion es 0,0,0
encoder.transform([["gasoline"],["diesel"],["aceite"]]).toarray()

#Las variables numericas pueden ser codificadas como categoricas segun el caso que se requiera
encoder.transform([[2016],[2009],[1990]]).toarray()

# cada campo es una variable: desventaja de One Hot