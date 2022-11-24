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
    if int(año) not in range(1980,2018):
        print("Año no valido")
        exit()
    
    newdata=data[data["Ano"]==int(año)]
    datasel=newdata[["Venta Millones","Plataforma"]].groupby(data["Plataforma"]).sum("Venta Millones")
    max_mill=datasel.max()
    print("4. Plataforma mas vendida del año",año,"es",datasel[datasel["Venta Millones"]==float(max_mill)])

def jueg_cont(juego,data):
     newdata=data[data["Nombre"]==juego]
     datasel=newdata[["Venta Millones","Region"]].groupby([newdata["Ano"],newdata["Region"]]).sum("Venta Millones")
     print("5. Venta de juego seleccionado por año y region:",datasel)

def cont_jue(continente,data):
     newdata=data[data["Region"]==continente]
     datasel=newdata[["Nombre","Venta Millones"]].groupby(newdata["Nombre"]).sum("Venta Millones")
     max=datasel.max()
     print("6. Juego mas vendido de la region",continente,"es",datasel[datasel["Venta Millones"]==float(max)])
