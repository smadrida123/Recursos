#a) Write a function that takes a sentence as input and returns the reverse of each word in the sentence 
#while preserving the order of words. For example, if the input is "Hello World", the output should be "olleH dlroW".


def reverse(list_of_words:list,tamaño_frase:int):
    final_string1=""
    final_string2=""
#Invertir orden de letras dentro de palabras
    nueva_list=[list_of_words[tamaño_frase-cont1-1] for cont1 in range(tamaño_frase)]
#Volver a unir en palabras y formar lista de palabras        
    for x in nueva_list:
        final_string1 +=x
        nueva_list2=final_string1.split()
#Convertir en string lista de palabras obtenida
    nueva_list2=nueva_list2[::-1]
    final_string2=" ".join(nueva_list2)
    print(final_string2)

        
list_of_words=list(input("Ingrese frase a transformar: "))
tamaño_frase=len(list_of_words)
reverse(list_of_words,tamaño_frase)

"""
    for x in nueva_list:
        final_string1 +=x
        nueva_list2=final_string1.split()
"""