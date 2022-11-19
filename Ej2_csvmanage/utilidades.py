#ARCHIVO CON FUNCIONES PARA CORRER EN RUNNER.PY
import pandas as pd
#FUNCION QUE CALCULA VENTAS TOTALES
def vet_tot(data):
   vent_tot=data["Venta Millones"].sum()
   return vent_tot

def tot_año(data):

     tot_año=(data["Venta Millones"].groupby(data["Ano"])).sum()
     tot_año.loc["total"]=sum(tot_año)
     return tot_año

def tot_plat(data):
     tot_plat=(data["Venta Millones"].groupby(data["Plataforma"])).sum()
     tot_plat.loc["total"]=sum(tot_plat)
     return tot_plat
     
def plat_vende(año,data):
    if int(año) not in range(1980,2017):
        print("Año no valido")
        exit()
    #newdata=(data[["Ano","Venta Millones"]].groupby(data["Plataforma"])).sum()
    #newdata=(data["Venta Millones"].groupby([data["Ano"],data["Plataforma"]])).sum()
    #newdata=data[["Ano","Plataforma","Venta Millones"]]
    newdata=data["Venta Millones"].groupby(data["Ano"])
    get_año=newdata.get_group(año)
    

    print(newdata)

