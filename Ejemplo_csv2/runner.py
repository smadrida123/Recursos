import csv_reader
import utils
import graph

def run():
    #obtengo lista de diccionarios de archivo segun path que coloque
    datos=csv_reader.csv_reader("/home/smadrida/Compartido/Compartido/Ejemplo_csv2/world_population.csv")
    #grafica 1: años vs cantidad poblacion según Capital de pais seleccionada
    capital=input("Ingrese capital de pais a evaluar => ")
    country_info=utils.capital_reader(datos,capital)
    if len(country_info)>0:
        country_dict=country_info[0]
        labels,values=utils.pop_ages(country_dict)
        graph.generate_bar_chart(labels,values)
    #grafica 2 pie chart de porcentaje de poblacion mundial por pais
    #si se desea filtrar por continente
    datos=list(filter(lambda x:x["Continent"]=="Africa",datos))
    labels2,values2=utils.pop_perc(datos)
    
    graph.generate_pie_chart(labels2,values2)


if __name__=="__main__":
    run()
