import matplotlib.pyplot as plot
import numpy as np
def donut_chart(data):
    labels=data["Region"].unique()
    values=(data["Venta Millones"].groupby(data["Region"])).sum()
    colors=["#EB0F0F","#48EB0F","#080BD8","#D508D8"]
    print(labels,values)
    explode=(0.05,0.05,0.05,0.05)
    plot.pie(values,colors=colors,labels=labels,autopct="%1.1f%%",pctdistance=0.85,explode=explode)
    centre_circle=plot.Circle((0,0),0.50,fc="white")
    fig=plot.gcf()
    fig.gca().add_artist(centre_circle)
    plot.title("Ventas totales por región")
    plot.legend(labels,loc="lower right")
    plot.show()

def vert_barra(data):
    labels=np.sort(data["Ano"].unique())
    values=(data["Venta Millones"].groupby(data["Ano"])).sum()
    colors=["#EB0F0F","#48EB0F","#080BD8","#D508D8"]
    fig,ax=plot.subplots()
    ax.bar(labels,values,color=colors)
    ax.set_xlabel("Años")
    ax.set_ylabel("Venta Millones")
    ax.set_title("Ventas totales por año")
    ax.grid(True)
    ax.set_xticks(range(1980,2018))
    ax.set_yticks(range(0,300,25))
    plot.xticks(rotation=90,fontsize=7)
    plot.show()

def hor_barra(data):
    labels=np.sort(data["Plataforma"].unique())
    values=(data["Venta Millones"].groupby(data["Plataforma"])).sum()
    fig,ax=plot.subplots()
    ax.barh(labels,values,color="navy")
    ax.set_title("Ventas totales por plataforma",color="#080ED8",fontweight="bold")
    ax.set_xlabel("Venta Millones")
    ax.set_ylabel("Plataforma")
    ax.grid(True)
    plot.show()