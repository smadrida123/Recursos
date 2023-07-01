import numpy as np
import matplotlib.pyplot as plt

#funcion lineal

m=1
b=5

def f1(x):
    return m*x+b

#numeros a ingresar a la funcion
N=100
#rango
x=np.linspace(-10,10,num=N)
y1=f1(x)
fig, ax = plt.subplots(3,3,figsize=(10,10))
ax[0,0].plot(x,y1,"r")
ax[0,0].grid()

#funcion polinomica
def f2(x):
    return (2*x**7)-(x**4)+(3*x**2)+4

y2=f2(x)
ax[0,1].plot(x,y2,"r")
ax[0,1].grid()

#funcion exponencial
def f3(x):
    return (x**5)

y3=f3(x)
ax[0,2].plot(x,y3,"r")
ax[0,2].grid()

#funcion trascendente: no puede ser expresada con polinomios
#funciones trigonometricas
def f4(x):
    return np.arccos(x)

y4=f4(x)
ax[1,0].plot(x,y4,"b")
ax[1,0].grid()
#funciones exponencial
def f5(x):
    return np.exp(x)

y5=f5(x)
ax[1,1].plot(x,y5,"b")
ax[1,1].grid()

#funciones logaritmica
x2=np.linspace(0.001,256,num=1000)
def f6(x):
    return np.log2(x)

y6=f6(x2)
ax[1,2].plot(x2,y6,"b")
ax[1,2].grid()

#funcion escalonada
def f7(x):
    Y=np.zeros(len(x))
    for idx,x in enumerate(x):
        if x >=0:
            Y[idx]=1
    return Y

y7=f7(x)
ax[2,0].plot(x,y7,"g")
ax[2,0].grid()

#funciones compuestas f(g(x)): input de nesima funcion es output de nesima-1 funcion
#funcion como argumento de funcion
def f8(x):
   return x**2
def f9(x):
    return np.sin(x)

y9=f9(f8(x))
ax[2,1].plot(x,y9,"g")
ax[2,1].grid()

#y=f(x)+c se desplaza c unidades hacia arriba
#y=f(x)-c se desplaza c unidades hacia abajo
#y=f(x-c) se desplaza c unidades hacia la derecha
#y=f(x+c) se desplaza c unidades hacia la izquierda
#y=c*f(x) alarga la grafica verticalmente en factor c o si divide lo comprime
#y=f(c*x) alarga horizontalmente
#y=-f(x) refleja la grafica respecto al eje x
#y=f(-x) refleja la grafica respecto al eje y
def f10(x):
    return x**2
y10=-f10(x)

ax[2,2].plot(x,y10,"g")
ax[2,2].axvline(x=0,color="r")
ax[2,2].axhline(y=0,color="r")
ax[2,2].grid()




fig.tight_layout()

#Perceptron: neurona artificial
#señales de entrada ->pesos sinapticos -> union sumadora ->funcion de activacion ->salida
#señales de entrada: caracteristicas o "features" normalmente 1s y 0s
#Pesos sinapticos: numeros encargados de ponderar que tan importante es señal de entrada
#union sumadora: suma de operaciones de xn*fn. combinacion lineal. linea recta
#Funcion de activacion: le da comportamiento no lineal a union sumadera

#Red neuronal artificial
#Funcion de activacion
#Función lineal: mantener valores a lo largo de un proceso, predecir venta

#Función escalón o de Heaviside: clasificaciones categóricas, ej. binarias

#Función sigmoide: regresión logística, para probabilidades

#Función tangente hiperbólica: para escalamiento

#Función ReLU: simulación de “neuronas muertas”

#Regresion lineal simple
#error=abs(y´ - y)
#error**2=(y´-y)**2 sirve para que cuando errores esten mas alejados se sube valor y entre mas pequeño error mas pequeño se hace
#E=suma(i,n) de (y´-y)**2
#ECM: Error cuadratico promedio: 1/Numero de datos * E



