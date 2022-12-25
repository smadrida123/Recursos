#RETO 2 FUNCION QUE RECIBA LISTA Y RETORNE 0 SI HAY ELEMENTOS REPETIDOS Y 1 SI SOLO SE INGRESARON ELEMENTOS UNICOS


def uniq_repet():
    texto=input("Ingrese caracteres/digitos a analizar: ")
    lstod=[]
    lsuniq=[]
    for x in texto:
        lstod.append(x)
        if x not in lsuniq:
            lsuniq.append(x)
    if len(lsuniq)==len(lstod):
      print(1)
      print("Elementos sin repeticion",lsuniq)
    else:
      print(0)
      print("Elementos repetidos",lstod)
     

uniq_repet()
 
