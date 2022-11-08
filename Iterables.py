#Iteraciones Manuales
for i in range(1,5):
  print(i)

my_iter=range(1,5)
#Se debe crear tipo de objeto iterable con iter()
#Iteracion de forma manual
my_iter2=iter(range(1,5))
print(my_iter)
print(my_iter2)
#se pueden controlar iteraciones de forma manual con next()
print(next(my_iter2))
#va a siguiente numero dentro de mi rango
print(next(my_iter2))
#si se pasa de rango genera error stopiteration
