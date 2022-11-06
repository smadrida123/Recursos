#MODULOS
Son ficheros que contienen un conjunto de funciones
#import
import sys
print(sys.path)
#devuelve lista con ruta donde se esta ejecutando archivo

import re
#expresiones regulares
text="mi numero es 289 34 8 858"
result=re.findall("[0-9]+",text)
print(result)

import time
timestamp=time.time()
print(timestamp) #hora formato computadora
local=time.localtime()
result=time.asctime(local)
print(result)

import collections 
#para manejar listas
numbers=[1,1,2,2,3,5,1,1,1,5,56,6,4,2,3,]
counter=collections.Counter(numbers)
print(counter)
#devuelve diccionario con frecuencia de aparicion de numero key(numero):value(numero de veces que aparece)