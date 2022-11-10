#EJEMPLO 1 FUNCION REDUCE. Sumar todos los valores de una lista
import functools
numbers=[1,2,3,4]
result=functools.reduce(lambda counter,item:counter+item,numbers)
print(result)

#EJEMPLO 2. Valor mayor en una lista
numbers2=[4,6,7,99]
def mayor(contador,item):
    if contador>item:
        return contador
    else:
        return item

resultado=functools.reduce(mayor,numbers2)
print(resultado)

