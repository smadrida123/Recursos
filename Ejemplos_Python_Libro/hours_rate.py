#FUNCION QUE DEVUELVE PAGA PARA UNAS HORAS Y YNA TASA DE PAGO
def paga(hours,rate):
    try:
     hours=int(hours)
     rate=int(rate)
    except:
        print("Valor ingresado no valido")
        exit()
        
    mayores=0
    u=0
    if hours>40:
        mayores=hours-40
        u=mayores*1.5*rate
    
    pagatotal=u+((hours-mayores)*rate)
    print("la paga total es: ",pagatotal," dolares por ",hours,"horas trabajadas")
    if u>0:
        print("pago horas trabajadas tarifa normal: ",(hours-mayores)*rate,"pago horas trabajadas tarifa extra: ",u,"pago total: ", pagatotal)

hours=input("Ingrese horas laboradas: ")
rate=input("ingrese pago por hora laborada: ")
paga(hours,rate)
