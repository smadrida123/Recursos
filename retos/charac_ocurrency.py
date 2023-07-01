#b) Write a function that takes a string as input and returns the most common character in the string. 
#If there are multiple characters with the same highest frequency, return the one that occurs first.
from collections import Counter

def hig_freq_char(lista:list):
 #retorna diccionario que tiene numero de ocurrencias por caracter
    counter=Counter(lista)
    max_val=0
 #almacena valor maximo de ocurrencia   
    for x in counter.values():
        if x >= max_val:
            max_val=x
 #imprime llave (caracter que se repite mas) y numero de veces que se repite (max_val)
    for key,value in counter.items():
        if value==max_val:
            print(key,max_val)
            break

lista=list(input("Ingrese frase/palabra a contar caracteres: "))
hig_freq_char(lista)
