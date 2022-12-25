#VOCAL MAS COMUN: Funcion que reciba un texto y retorne la vocal que mas se repita
texto=input()
from collections import Counter
def v_comun(texto):
    ls=[]
    texto=texto.lower()
    counter=[]
    for x in texto:
      if x in "aeiou":
        ls.append(x)
      else:
        continue  

    c=Counter(ls)

    for y in c.values():
      counter.append(y)
      z=max(counter)
      key = [i for i in c if c[i]==z]
    print("la vocal que mas veces se repite en el texto es:",key[0], "con el siguiente numero de veces",z)
    print("lista de vocales con sus repeticiones",c)
      


        

    


v_comun(texto)



        
