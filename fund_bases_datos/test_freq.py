#Finding the most frequently occurring words in a text file: You need to write a program that reads a large text file and finds the top 10 most 
#frequently occurring words. You can use techniques such as tokenization, counting frequencies, 
#and sorting to achieve this. Consider using data structures like dictionaries to store word frequencies.

from collections import Counter

filehandle=open("notas_fund.txt")
ls=[]

for x in filehandle:
    if x not in ls:
     ls.append(x)
     

histogram=Counter(ls)
print(histogram)