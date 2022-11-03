#ejemplo funciones
def my_print(text):
  print(text)

my_print("parametro")

#ejemplo funcion de print y suma
def sum(a,b):
  print(a+b)
sum(3,11)

#ejemplo 2 con return
def sum_with_range(a,b):
  print(a,b)
  sum=0
  for x in range(a,b):
    sum +=x
  return sum

result= sum_with_range(1,10)
print(result)
sum_with_range(20,30)

#ejemplo por valor por defecto si no se envian parametros
#se pueden enviar un parametro en especifico
#ejemplo para varios returns. Resultados en tupla se pueden sacar por posicion o tener varias variables para sacarlas individual
def find_volume(lenght=1,width=1,height=1):
  return lenght*width*height, width,"hola"
result,width,string=find_volume(width=10)
print(result,width,string)