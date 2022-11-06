#EJEMPLO CALCULADORA CON FUNCIONES
def conv_input():
    print("La calculadora mas perrona de python")
    options=("/","+","-","x")
    try:
       n1=float(input("Ingrese primer numero "))
       n2=float(input("Ingrese segundo numero "))
    except:
        print("No se ingreso número")
        exit()
    op=input("Ingrese operacion ")
    if op not in options:
        print("opcion no valida")
        exit()
    return n1,n2,op

def sum(n1,n2,op):
    if op=="+":
        print("La suma de valores es ",n1+n2)
    return n1+n2

def resta(n1,n2,op):
    if op=="-":
        print("La resta de valores es ",n1-n2)
    return n1-n2

def multi(n1,n2,op):
    if op=="x":
        multi=n1*n2
        print("Multiplicacion entre valores es ",n1*n2)
    return n1*n2

def div(n1,n2,op):
    if op=="/":
       print("resultado division es",n1/n2)
    return n1/n2


def calc():
    n1,n2,op=conv_input()
    sum(n1,n2,op)
    resta(n1,n2,op)
    multi(n1,n2,op)
    div(n1,n2,op)

calc()


