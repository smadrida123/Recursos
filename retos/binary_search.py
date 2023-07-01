#Implement a binary search algorithm to search for a given element in a sorted list.
import numpy as np
"""
def binary_search(ls:list):
    v=int(input("Ingrese numero a buscar: "))
    mediana=np.median(ls)
    print("La lista a analizar es: ",ls)
    if v not in ls:
     print("Numero no se enuentra en lista")
    else:
     print("La mediana es: ",mediana)
     mitad=closest_median(mediana,ls)
     mitad=ls.index(mitad)
     ls.sort()

    
     if v < mediana:
        print("Menor a valor de la mitad")
        for idx,x in enumerate(ls[0:mitad]):
            if x == v:
                print("Numero encontrado en posicion",idx,"Numero es: ",x)
 
     elif v > mediana:
        print("Mayor a valor de la mitad")
        for idx,x in enumerate(ls[mitad::]):
            if x == v:
                print("Numero encontrado en posicion",idx,"Numero es: ",x)

     elif v == mediana:
        print("Igual a valor de la mitad")
        print("Numero encontrado en posicion",mitad,"Numero es: ",x)
    

def closest_median(x:float,ls:list):
    closest=None
    min_diff=float("inf")
    for y in ls:
        diff=abs(x-y)
        if diff < min_diff:
            min_diff=diff
            closest=y
    return closest


x=list(np.random.randint(0,100,100))
binary_search(x)
"""
#solucion chatgpt
def binary_searchgpt(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target value not found

# Example usage
sorted_list = (list(np.random.randint(0,100,100))).sort()
target_value = 10

result = binary_searchgpt(sorted_list, target_value)

if result != -1:
    print("Target value", target_value, "found at index", result)
else:
    print("Target value", target_value, "not found in the list")
