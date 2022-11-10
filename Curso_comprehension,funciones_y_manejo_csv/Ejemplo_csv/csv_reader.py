import csv

#Ejecucion de funcion arroja lista de filas [infocol1,infocol2,infocol3,...,]
def read_csv(path):
  with open(path,"r") as csvfile:
    reader=csv.reader(csvfile,delimiter=",")
    #obtener nombre de columnas en lista (fila 1)
    header=next(reader)
    data=[]
    for row in reader:
      #metodo zip para unir header con cada row (header fuera de loop) que se esta iterando
      iterable=zip(header,row)
      #generar diccionario con dictionary comprehension para tener header,info header
      country_dict={header:row for header,row in iterable}
      #generar lista con diccionarios
      data.append(country_dict)
    return data

if __name__=="__main__":
  data=read_csv("/home/smadrida/Compartido/Compartido/Ejemplo_csv/world_population.csv")
  print(data[0])