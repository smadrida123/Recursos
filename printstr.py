#The included code stub will read an integer, , from STDIN.Without using any string methods, try to print the following:Note that "" represents the consecutive values in between.ExamplePrint the string .

if __name__ == '__main__':
    n = int(input())
ls=[]   
while n!=0:
    ls.append(n)
    n=n-1
    if n==1:
        break

y=sorted(ls)

s=str(n)
for x in y:
    y=str(x)
    s=s+y
print(s)

