import csv

#Funcion para abrir,leer y transformar datos de un archivo csv a par header,dato en lista de diccionarios
def csv_reader(path):
 with open(path,"r") as csvfile:
    handle=csv.reader(csvfile,delimiter=";")
    header=next(handle)
    data=[]
    for x in handle:
        iterable=zip(header,x)
        dict={header:x for (header,x) in iterable}
        data.append(dict)
    return data
    
    

csv_reader("/home/smadrida/Compartido/Compartido/Ej2_csvmanage/data_ventas_video_juegos_1 1.csv")