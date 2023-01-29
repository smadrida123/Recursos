# Enter your code here. Read input from STDIN. Print output to STDOUT
#Check if number is boolean
import re

cases=input()
def eval_float(cases):
    cases=int(cases)
    pattern=re.compile(r'^([\+\-\.0-9])(\d{1,5})?\.?(\d{1,8})?$')
    data=[]
    for x in range(cases):
        valuate=input()
        data.append(valuate)
        for y in data:
            if len(y)>1:
             res=re.match(pattern,y)
            else:
                continue
        print(bool(res))
        
if __name__=="__main__":
    eval_float(cases)
        