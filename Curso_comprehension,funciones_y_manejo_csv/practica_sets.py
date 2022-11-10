#CLASE 1
set_countries={"col","mex","bol"}
print(set_countries)
print(type(set_countries))

set_from_string=set("hola")
print(set_from_string)
set_from_tuples=set(("abc","cbv","as","abc"))
print(set_from_tuples)
numbers=[1,2,3,1,2,3,1,4]
set_numbers=set(numbers)
print(set_numbers)
#saca numeros repetidos, solo coge unicos
unique_numbers=list(set_numbers)
print(unique_numbers)

#CLASE 2
set_countries={"col","mex","bol"}
size=len(set_countries)
#si elemento esta en conjunto
print("col" in set_countries)
#adicionar elemento
set_countries.add("pe")
print(set_countries)
#actualizar conjunto
set_countries.update({"ar","ecu","pe"})
print(set_countries)
#eliminar elemento
set_countries.remove("col")
#.discard no arroja error
print(set_countries)
#limpiar conjunto, queda set en vacio
set_countries.clear()

#CLASE 3
#Union de dos conjuntos
set_1={"col","mex","bol"}
set_2={"pe","bol"}
set_3=set_1.union(set_2)
print(set_3)
#otra manera
print(set_1 | set_2)

#Interseccion entre dos conjuntos
set_3=set_1.intersection(set_2)
print(set_3)
print(set_1 & set_2)

#diferencia (resta entre conjuntos)
set_3=set_1.difference(set_2)
print(set_3)
print(set_1-set_2)

#diferencia simetrica excluye elementos comunes entre conjuntos
set_3=set_1.symmetric_difference(set_2)
print(set_3)
print(set_1^set_2)