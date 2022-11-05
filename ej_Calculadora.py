#EJEMPLO CALCULADORA CON FUNCIONES
def conv_input():
    print("La calculadora mas perrona de python")
    options=("/","+","-","x")
    try:
       n1=float(input("Ingrese primer numero "))
       n2=float(input("Ingrese primer numero "))
    except:
        print("No se ingreso número")
        exit()
    op=input("Ingrese operacion ")
    if op not in options:
        print("opcion no valida")
        exit()
    return n1,n2,op

def sum(n1,n2,op):
    suma=0
    if op=="+":
        suma=n1+n2
        print("La suma de valores es ",suma)
    return suma

def resta(n1,n2,op):
    resta=0
    if op=="-":
        resta=n1-n2
        print("La resta de valores es ",resta)
    return resta

def multi(n1,n2,op):
    multi=0
    if op=="x":
        multi=n1*n2
        print("Multiplicacion entre valores es ",multi)
    return multi

def div(n1,n2,op):
    div=0
    if op=="/":
       div=n1/n2
       print("resultado division es",div)
    return div


def calc():
    n1,n2,op=conv_input()
    sum(n1,n2,op)
    resta(n1,n2,op)
    multi(n1,n2,op)
    div(n1,n2,op)

calc()


