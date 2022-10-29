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