 #* Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2)
 #  e imprima otras dos cadenas como salida (out1, out2).
 #* - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
 #* - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
str1=input("Ingrese primera cadena de caracteres: ")
str2=input("Ingrese segunda cadena de caracteres: ")

def out_cad(str1,str2):
 out1=[]
 out2=[]  
 for x in str1:
    if x not in str2:
        out1.append(x)
    else:
        continue
 for x in str2:
    if x not in str1:
        out2.append(x)
    else:
         continue
 print("".join(out1),"".join(out2))


out_cad(str1,str2)





