#MODULO CON FUNCIONES A EJECUTAR EN ARCHIVO Modulos2.py
def get_population():
  keys=["col","bol"]
  values=[300,400]
  return keys,values

def population_by_countries(data,country):
  result=list(filter(lambda item:item["Country"]==country,data))
  return result
