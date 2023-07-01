#a) Write a function that takes a list of numbers as input and calculates the average.
#Handle the exception if the input list is empty and return an appropriate error message.
import numpy as np
import warnings

def avg_ls():
    warnings.filterwarnings("error")
    ls=[]
    try:
     num_inputs=int(input("Ingrese numero de elementos: "))
    except: print("Numero ingresado no valido")
    try:
     for x in range(num_inputs):
       ls.append(int(input("Ingrese numeros: ")))
     return np.mean(ls)
    except Warning as warn:
     print("Lista vacia o ingreso no valido",warn)
    except:
     print("Lista vacia o ingreso no valido")

    

avg=avg_ls()
print("El promedio de la lista es: ",avg)

#b) Write a program that reads an integer from the user and performs the division operation by 2.
#Handle the exception if the user enters a non-integer value and display an error message.
def div_2():
    try:
        x=int(input("Ingrese numero a dividir:"))
        return x/2
    except: print("Ingreso de numero no valido")
    
x=div_2()
print(x)