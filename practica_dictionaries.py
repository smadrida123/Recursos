#DICTIONARY COMPREHENSION
dict={}
for i in range(1,5):
  dict[i]=i*2
print(dict)
dict_v2={i:i*2 for i in range(1,5) }
print(dict_v2)

#ejemplo iterar de una lista y crear diccionario
import random
countries=["col","mex","bol","pe"]
population={}
for country in countries:
  population[country]=random.randint(1,100)
print(population)

#con list y dictionaries comprehension
population_v2={country:random.randint(1,100) for country in countries}
print(population_v2)

#ejemplo con dos listas diferentes para key y value
names=["nico","zule","santi"]
ages=[12,56,98]
u=list(zip(names,ages)) #resultado es lista de tuplas de names y ages
resul={name:age for (name,age) in u}
print(resul)

#DICTIONARY COMPREHENSION + IF
#Plantilla {key:value for var in iterable if condition}
#dictionary comprehension + if
population_v2={country:random.randint(1,100) for country in countries}
print(population_v2)
resul={country:population for (country,population) in population_v2.items() if population>50 }
print(resul)

#AGREGAR VOCALES A UN DICT
text="hola soy santiago"
unique={c:c.upper() for c in text if c in "aeiou"}
print(unique)