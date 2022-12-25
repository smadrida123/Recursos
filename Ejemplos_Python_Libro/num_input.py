#Programa que pide ingresar numeros hasta escribir "Done" y cuando esto suceda imprimir suma, promedio y conteo de numeros ingresados
x=0
y=0
c=0
while x !="Done":
 x=input("Ingrese Numero: ")
 try:
  num=float(x)
 except:
    print("Numero no valido")
    continue
 c=c+1
 y=y+num
 prom=y/c

print(y,c,prom)

