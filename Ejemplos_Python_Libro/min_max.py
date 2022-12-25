#MINIMOS Y MAXIMOS DE UNA LISTA DE NUMEROS DADA POR EL USUARIO
min=0
max=0
x=0
while x != "Done":
    x=input("Ingrese numero ")
    try:
        num=float(x)
    except:
        print("Numero no valido ")
        continue
    if num>max:
        max=num
    if num<min or num!=0:
        min=num

print("Numero minimo es: ",min,"Numero maximo es: ",max)
   