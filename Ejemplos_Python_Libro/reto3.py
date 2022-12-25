#RETO 3 FUNCION QUE RECIBA ARCHIVO.TXT Y RETORNE 0 SI HAY ELEMENTOS REPETIDOS Y 1 SI SOLO SE INGRESARON ELEMENTOS UNICOS


def uniq_repet():
    texto=input("Ingrese archivo a analizar ")
    handle=open(texto)
    lsuniq=[]
    for x in handle:
        words=x.split()
        for word in words:
            if word not in lsuniq:
              lsuniq.append(word)
    if len(lsuniq)==len(words):
      print(1)
      print("Elementos sin repeticion",lsuniq)
    else:
      print(0)
      print("Elementos repetidos",words)
     

uniq_repet()
 
