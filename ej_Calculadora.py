#EJEMPLO CALCULADORA CON FUNCIONES
def calc(n1,n2,op):
    if op=="+":
        print(n1+n2)
    elif op=="-":
        print(n1-n2)
    elif op=="x":
        print(n1*n2)
    elif op=="/":
        print(n1/n2)

calc(float(input()),float(input()),input())


