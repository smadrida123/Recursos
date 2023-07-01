#There is an array of n integers. There are also 2 disjoint sets,  A
#and B, each containing  integers. You like all the integers in set A and dislike all 
#the integers in set B. Your initial happiness is 0. For each i integer in the array, if i e A, you add 1 to your happiness
#. If i e B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

#Ingresar numero de enteros de array de chequeo y creación de arrays de chequeo y sets A y B a chequear
n=int(input("Ingrese numero de enteros en lista de chequeo: "))
m=int(input("Ingrese numero de enteros en sets A y B a chequear: "))
res1=0
res2=0
res3=0
contA=0
contB=0
chequeo=list(range(1,n+1))
A=set()
B=set()
for x in chequeo:
    chequeo[res1]=int(input("Ingrese numero para agregar a chequeo: "))
    res1=res1+1

while res2 < m:
    A.add(int(input("Ingrese numero para Array A: ")))
    B.add(int(input("Ingrese numero para Array B: ")))
    res2=res2+1

#Chequeo de existencia de elementos de sets A y B en array chequeo
while res3 < m:
    if chequeo[res3] in A:
        contA=contA+1

    if chequeo[res3] in B:
        contB=contB-1

    
    res3=res3+1

print("Su puntaje es: ",contA+contB)