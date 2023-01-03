#Enunciado: Escribe una función que reciba un texto 
# y retorne verdadero o falso (Boolean) según sean o no palíndromos.
#Un Palíndromo es una palabra o expresión que es igual si se 
# lee de izquierda a derecha que de derecha a izquierda.
#NO se tienen en cuenta los espacios, signos de puntuación y tildes.
texto=input("Ingrese texto a analizar: ")

def palindromo(texto):
    texto=texto.rstrip()
    lst=[x for x in texto if x in "abcdefghijklmnopqrstuvwxyz"]
    rev=[]
    count=0
    l=len(lst)-1
    for y in lst:
      rev.append(lst[l-count])
      count=count+1
    print(lst,rev)
    if lst==rev:
        print("Es un palindromo!")
    else:
        print("No es un palindromo")


palindromo(texto)