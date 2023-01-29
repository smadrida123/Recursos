#PARTIDO DE TENIS
import random
print("!"*10)
print("Bienvenido al partido de tenis mas perrón")
print("!"*10)
j1=0
j2=0
p1=0
p2=0
for y in range(1,12):
    print("Empieza el game #",y)
    x=random.randint(0,1)
    print("jugador 1",p1,"-",p2,"jugador 2") 
        if x==1:
            p1=p1+15
        else:
            p2=p2+15
        if p1==45 and p2==45:
            if x==1:
                p1="ADV"
            else:
                p2="ADV"
        if p1=="ADV" and x==1:
            j1=j1+1
            print("set para jugador 1: [","jugador 1",60,"-",p2,"jugador 2","]")
        if p2=="ADV" and x==0:
            j2=j2+1

            print("set para jugador 2: [","jugador 1",p1,"-",60,"jugador 2","]")

        if p1==60:
            print("set para jugador 1: [","jugador 1",p1,"-",p2,"jugador 2","]")
            j1=j1+1
            print(j1)
            break
        if p2==60:
            print("set para jugador 2: [","jugador 1",p1,"-",p2,"jugador 2","]")
            j2=j2+1
            print(j2)
            break



if j1==6:
    print("Ganador de partido es j1")
if j2==6:
    print("Ganador de partido es j2")




