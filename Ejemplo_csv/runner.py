import utils
import csv_reader as reader
import graph

def run():
  data=reader.read_csv("/home/smadrida/Compartido/Compartido/Ejemplo_csv/world_population.csv")
  #para grafico de pie, linea para filtrar por continente
  data=list(filter(lambda item:item["Continent"]=="South America",data))
  labels2,values2=utils.population_percentage(data)
  graph.generate_pie_chart(labels2,values2)
  
  country=input("Type country => ")
  result=utils.population_by_countries(data,country) 
  if len(result)>0:
    #result saca lista de dict de pais seleccionado
    #country saca elemento en formato diccionario
    country=result[0]
    labels,values=utils.get_population(country)
    graph.generate_bar_chart(labels,values)

#Ejecuta como script el archivo main si se llama desde terminal pero si llamo el archivo example solo me ejecuta lo que yo llame controladamente
if __name__=="__main__":
  run()