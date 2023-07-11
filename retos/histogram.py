#histogram for numbers within a list

ls1=[1,2,2,2,4,5,5,6,6,6,6,6,7,8,9,10]
d={}
d2={}
n=1
filehandle=open("clown.txt")
ls_words=[word for line in filehandle for word in line.split()]


for x in ls1:
    if x in d.keys():
        d[x]=d.get(x)+1
        
    if x not in d.keys():
     d[x]=n

for x in ls_words:
    if x in d.keys():
        d2[x]=d2.get(x)+1
        
    if x not in d2.keys():
     d2[x]=n
    

print(d,d2)
