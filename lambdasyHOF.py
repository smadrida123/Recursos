#EJEMPLO FUNCION LAMBDA
def increment1(x):
  return x+1

result1=increment1(10)
print(result1)

#MISMO EJEMPLO CON FUNCION LAMBDA
result=lambda x:x+1
result_v2=result(10)
print(result_v2)

#LAMBDA CON VARIOS PARAMETROS
full_name= lambda name,last_name: f"Fullname es {name.title()} {last_name.title()}"

text=full_name("nicolas","perez casas")
print(text)

#EJEMPLO HIGH ORDER FUNCTIONS
def increment2(x):
  return x+1
#funcion que dentro de su bloque de codigo ejecuta una funcion. No necesita ejecutarla, solo su definicion
def high_order(x,increment):
  return x+increment2(x)

result=high_order(10,increment2)
#10+(10+1)
print(result)

#mismo ejemplo con lambda
increment3=lambda x:x+1
high_order2=lambda x,increment2:x+increment2(x)
result=high_order2(10,increment3)
print(result)
result=high_order2(10,lambda x:x+1)
print(result)

