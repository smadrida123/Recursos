import csv
#Funcion que lee archivo csv y retorna lista de diccionarios con par titulo (fila 1); datos
def csv_reader(path):
    #abre archivo
    with open(path,"r") as csvfile:
        #lee archivo
        handle=csv.reader(csvfile,delimiter=",")
        #saca lista de fila 1 (titulos) con iteracion manual
        header=next(handle)
        data=[]
        for x in handle:
            iterable=zip(header,x)
            #de objeto iterable genera diccionario con fila1 (titulos) y datos para cada pais (resto de filas)
            dict={header:row for header,row in iterable}
            data.append(dict)
        return data



if __name__=="__main__":
 x=csv_reader("/home/smadrida/Compartido/Compartido/Ejemplo_csv2/world_population.csv")
 print(x)