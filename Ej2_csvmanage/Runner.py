import pandas as pd
import utilidades as u
import graph as gr


def run(path):
    
    data=pd.read_csv(path,sep=";")
    """
    vent_tot=u.vet_tot(data)
    print("1. Las ventas totales son:",vent_tot,"millones")
    tot_año=u.tot_año(data)
    print("2. Las ventas totales por año son \n",tot_año)
    tot_plat=u.tot_plat(data)
    print("3. Las ventas totales por plataforma son \n",tot_plat)
    año=input("Ingrese año: ")
    u.plat_vende(año,data)
    juego=input("Ingrese juego: ")

    u.jueg_cont(juego,data)
    continente=input("Ingrese continente para ver informacion deseada: ")
    u.cont_jue(continente,data)
    gr.donut_chart(data)
    """
    gr.vert_barra(data) 
    gr.hor_barra(data)
    
    


if __name__=="__main__":
    run("data_ventas_video_juegos_1 1.csv")
