import matplotlib.pyplot as plt

def generate_bar_chart(labels,values):
  fig,ax=plt.subplots()
  ax.bar(labels,values,color="navy")
  plt.title("Tendencia de poblacion a traves de los años para pais seleccionado")
  plt.xlabel("Años")
  plt.ylabel("Cantidad de poblacion")
 
  plt.show()

def generate_pie_chart(labels,values):
  fig,ax=plt.subplots()
  plt.title("Grafico de torta Porcentaje poblacion mundial de paises")
  ax.pie(values,labels=labels)
  ax.axis("equal")
  plt.show()


if __name__=="__main__":
  #eje x
  labels=["a","b","c"]
  #eje y
  values=[100,500,300]
  #genera grafica coordenadas x,y
  plt.scatter(labels,values)
  #muestra linea de tendencia (une puntos entre coordenadas)
  plt.plot(labels,values)
  plt.show()
  #generate_bar_chart(labels,values)
  generate_pie_chart(labels,values)

