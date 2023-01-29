#Ingresar organizacion y se devuelve acronimo
import re
def acronym():
    pattern=re.compile(r'^([A-Z])([a-z]{2,20})[\s]?[A-Z]?([a-z]{2,20})?[\s]?[A-Z]?([a-z]{2,20})?[\s]?[A-Z]?([a-z]{2,20})?[\s]?[A-Z]?([a-z]{2,20})?$')
    intentos=0
    while intentos!=3:
        data=input("Ingresa organizacion a analizar (Palabras separadas por espacio en mayusculas): ")
        x=re.match(pattern,data)
        if bool(x) == False:
            print("Datos ingresados invalidos prueba otra vez", "intentos restantes: ",2-intentos)
            intentos=intentos+1
        if intentos==3:
            print("acronimo se puso triste por 3 datos invalidos y se morirá")
            break
        if bool(x)==True:
            break
    d=data.split(sep=" ")
    for x in d:
        print(x[0])
if __name__=="__main__":
  acronym()