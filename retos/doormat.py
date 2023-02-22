#TAPETE
def tapete():
    n=int(input("Ingrese tamaño de tapete: "))
    w=int(n/2)
    m=3*n
    y=int(m/2)
    ls=[]
    for x in range(0,w):
     linesup= "-"*(y-(3*x))  + ".|."*(2*x+1) + "-"*(y-(3*x))
     ls.append(linesup)
     welcome="-"*(y-2) + "WELCOME" + "-"*(y-2)
     print(linesup)
     if x==(w-1):
        print(welcome)
    for z in reversed(ls):
        print(z)

tapete()