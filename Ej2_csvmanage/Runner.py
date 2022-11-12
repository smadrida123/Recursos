import csv_reader as csv
import utilidades as u

def run(path):
    data=csv.csv_reader(path)
    vent_tot=u.vet_tot(data)
    print("1. Las ventas totales son:",vent_tot,"millones")
    vent_año,comp=u.vet_años(data)
    if comp==vent_tot:
        print("Suma por años igual a suma total!. Comprobacion aceptada",comp,"=",vent_tot)
    print("2. Las ventas totales por año son",vent_año,"en millones")



if __name__=="__main__":
    run("/home/smadrida/Compartido/Compartido/Ej2_csvmanage/data_ventas_video_juegos_1 1.csv")
