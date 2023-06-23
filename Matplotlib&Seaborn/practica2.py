import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


##numpy
#1
a1=np.array(np.arange(1,11))
a2=np.reshape(a1,(2,5))
print(a1,"\n",a2)

#2
a3=np.array(np.random.randint(0,100,(5,5)))
sum_dig=np.diagonal(a3).sum()
print(a3,sum_dig)

#3
a4=np.array([1,2,3,4,5])
print(a4*2)

##pandas
#1
a5={"Name":("Santiago","Stefania","Oreo"),"Age":(10,40,35),"City":("NY","Manizales","Chinchina")}
data=pd.DataFrame(a5)
print(data)

#2
data2=pd.read_csv("bestsellers-with-categories.csv",sep=",")
print(data2.head(10))

#3
a6=data["Age"]>30
print(data[a6])

##matplotlib
#1
a7=np.array(np.arange(1,11))
a8=a7*2
plt.plot(a7,a8,"ro-")
plt.grid(True)
plt.title("a7 vs a8")
for i, j in zip(a7, a8):
    plt.text(i, j, str(j), ha='right', va='bottom')

plt.show()

#2
a9=["A","B","C","D"]
a10=[10,15,7,12]
fig=plt.figure()

plt.bar(a9,a10)
plt.show()

#3
a11=np.random.randint(1,50,(1,50))
a12=np.random.randint(1,50,(1,50))
plt.scatter(a11,a12)
plt.show()