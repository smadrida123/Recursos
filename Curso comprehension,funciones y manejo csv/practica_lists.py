#list comprehension
numbers=[]
for element in range(1,11):
  numbers.append(element)
print(numbers)
#List comprehension 
numbers_v2=[element for element in range(1,11)]
print(numbers_v2)

numbers_v2=[element*2 for element in range(1,11)]
print(numbers_v2)

#list comprehension +if
#Plantilla [var for var in iterable if condition]
numbers_v3=[element*2 for element in range(1,11) if element %2==0]
print(numbers_v3)