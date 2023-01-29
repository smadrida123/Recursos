#You are given a string and your task is to swap cases.
#In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
 import re
 ls=[]
 result=""
 for x in s:
    if x.lower()==x:
        result=result+x.upper()       
    elif x.upper()==x:
        result=result+x.lower()
             
 return result
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)