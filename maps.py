numbers=[1,2,3,4]
numbers_v2=[]
#ejemplo de transformacion de una lista
for i in numbers:
 numbers_v2.append(i*2)
print(numbers_v2)

#ejemplo con map y lambda function
numbers_v3=list(map(lambda i:i*2,numbers))
#se debe transformar a una lista para poder dar resultado
print(numbers_v3)

#ejemplo 2 transformacion entre listas de tamaños distintos
numbers_1=[1,2,3,4]
numbers_2=[5,6,7]
result=list(map(lambda x,y: x+y,numbers_1,numbers_2))
print(result)

#ejemplo 3 transformacion de lista con diccionarios a lista con enteros
items=[
  {
  "product":"camisa",
  "price":100,
  },
  {
  "product":"pantalones",
  "price":230,
  },
  {
  "product":"zapatos",
  "price":120,
  }
]
prices=list(map(lambda item:item["price"],items))
print(prices)

#ejemplo 4 maps con funcion dentro de parametro (map es high order function)
items=[
  {
  "product":"camisa",
  "price":100,
  },
  {
  "product":"pantalones",
  "price":230,
  },
  {
  "product":"zapatos",
  "price":120,
  }
]
prices=list(map(lambda item:item["price"],items))
print(prices)

def add_taxes(item):
 item["taxes"]=item["price"]*0.19
 return item
   
new_items=list(map(add_taxes,items))
print(new_items)

#PROBLEMA: Al agregar el atributo taxes, se modifica diccionario original
items2=[
  {
  "product":"camisa",
  "price":100,
  },
  {
  "product":"pantalones",
  "price":230,
  },
  {
  "product":"zapatos",
  "price":120,
  }
]

def add_taxes(item2):
  #solucion problema con funcion copy()
  new_item=item2.copy()
  new_item["taxes"]=new_item["price"]*0.19
  return new_item
   
new_items=list(map(add_taxes,items))
print("nueva lista",new_items)

print("vieja lista",items2)