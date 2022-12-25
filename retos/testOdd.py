#Dado un numero chequear si es impar imprimir weird sino not weird
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    
x=n%2

if x!=0:
    print("Weird")
elif x==0 and n in range(2,5):
    print("Not Weird")
elif x==0 and n in range(6,21):
    print("Weird")
elif x==0 and n>20:
    print("Not Weird")