#JUEGO TRIQUI
import numpy as np
import util as u
import pandas as pd
def run_triqui():

    tablero=np.array([["1","2","3"],["4","5","6"],["7","8","9"]])
    c=0
    while c==0:
     tablero=u.jug1(tablero)
     tablero=u.jug2(tablero)
     
     t=pd.DataFrame(tablero)
     

     if c==1:
        break
     print(t)





if __name__=="__main__":
    run_triqui()