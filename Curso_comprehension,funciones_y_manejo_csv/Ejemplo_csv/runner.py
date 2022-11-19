#PARA USAR EL ARCHIVO DESCARGAR DE https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset
import utils
import csv_reader as reader
import pandas as pd
import graph

def run():
  """
  #forma de hacer con csv
  data=reader.read_csv("world_population.csv")
  #para grafico de pie, linea para filtrar por continente
  data=list(filter(lambda item:item["Continent"]=="South America",data))
  labels2,values2=utils.population_percentage(data)
  graph.generate_pie_chart(labels2,values2)
  """
  #reemplaza csv_reader de volver datos en lista de diccionarios
  df=pd.read_csv("world_population.csv")
  df=df[df["Continent"]=="Africa"]

  countries=df["Country/Territory"].values
  percentages=df["World Population Percentage"].values
  print(df,countries,percentages)
  graph.generate_pie_chart(countries,percentages)
  data=reader.read_csv("world_population.csv")
  country=input("Type country => ")
  result=utils.population_by_countries(data,country) 
  if len(result)>0:
    #result saca lista de dict de pais seleccionado
    #country saca elemento en formato diccionario
    country1=result[0]
    labels,values=utils.get_population(country1)
    graph.generate_bar_chart(country,labels,values)

#Ejecuta como script el archivo main si se llama desde terminal pero si llamo el archivo example solo me ejecuta lo que yo llame controladamente
if __name__=="__main__":
  run()