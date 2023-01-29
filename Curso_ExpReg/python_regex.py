import re
# 1876-03-04,Scotland,England,3,0,Friendly,Glasgow,Scotland,FALSE ejemplo formato datos
fhandle=open("./results.csv","r")
match=0
nomatch=0
pattern=re.compile(r'^([\d]{4,4})\-\d\d\-\d\d,(.+),(.+),(\d+),(\d+),.*$')

for line in fhandle:
   res=re.match(pattern,line)
   if res:
    goles=int(res.group(4))+int(res.group(5))
    if goles>30:
        match=match+1
        print("Año(%s): %s,%s [%s-%s]" % res.group(1,2,3,4,5))
        print(goles,"\n",match)
    

fhandle.close()
