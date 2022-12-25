##funciones juego triqui
import numpy as np
#ingreso posiciones
options=["1","2","3","4","5","6","7","8","9"]
def jug1(tablero):
    jug1_x=input("Ingrese posicion dentro de tablero (1-9): ")
    if jug1_x not in options:
        print("posicion fuera de tablero")
        exit()
    tablero=np.where(tablero==jug1_x,"x",tablero)
    print(tablero)
    return tablero

def jug2(tablero):
    jug2_o=input("Ingrese posicion dentro de tablero (1-9): ")
    if jug2_o not in options:
        print("posicion fuera de tablero")
        exit()
    tablero=np.where(tablero==jug2_o,"o",tablero)
    print(tablero)
    return tablero




    




