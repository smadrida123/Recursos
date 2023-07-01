#Write a recursive function to calculate the factorial of a given number.

def calc_fac():
    num=0
    multiplo=1
    ls=[]
    try:
        num=int(input("Ingrese numero entero para calculo de factorial (!): "))
    except: print("Número ingresado no valido")
    ls=[x for x in range(num)]
    x=ls.pop(0)
    for cont in ls:
       multiplo=multiplo*cont


    print(multiplo*num)

calc_fac()


