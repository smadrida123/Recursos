#MAIN DE MODULO (AQUI SE EJECUTAN MODULOS QUE CREE desde archivo utils.py)
import Ejemplo_csv.utils as utils
def get_population():
  keys,values=utils.get_population()
  print(keys,values)


#A partir de una lista con diccionarios chequear si existe pais y arrojarlo en lista con su poblacion
data=[
  {
    "Country":"Colombia",
    "Population":350
  },
  {
    "Country":"Bolivia",
    "Population":450
  }
]

def population_by_countries():
  item=utils.population_by_countries(data,input("Ingrese pais "))
  print(item)


#ENTRY POINT (ejecutar como script)
if __name__=="__main__":
  get_population()
  population_by_countries()
  print("Ejecutado directamente")
else:
  print("Ejecutado importado")


