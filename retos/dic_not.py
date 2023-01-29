#Ejercicio
#Escribir una función que reciba un diccionario con las notas de los 
#alumno de un curso y devuelva una serie con la nota mínima, la máxima, media y la desviación típica.

import pandas as pd
def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadisticos = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index=['Min', 'Max', 'Media', 'Desviación típica'])
    return estadisticos

def notas_ordenadas(notas):
    notas = pd.Series(notas)
    orden = pd.Series(notas.sort_values(ascending=False))
    return orden

notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
notas2=[1,2,3,4]
print(estadistica_notas(notas))
print(notas_ordenadas(notas))
 
