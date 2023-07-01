#a) Implement a class called Circle that has a radius attribute. Include methods to calculate the area and circumference of the circle.
class circle:
    id=str

#metodo constructor para inicializar clase y atributos
    def __init__(self,id):
        self.id=id
#creacion de metodos 
    def saludar(self):
        print("Se calcularán valores de ",self.id)

    def calcular_area(self,radius:int):
        return radius*3.1416**2
        
#a metodos se ingresan creando una instancia de la clase creada de la manera:
circulo1=circle("circulo1")
area=circulo1.saludar()
area=circulo1.calcular_area(5)
print(f"El area de {circulo1} es: ",area)

#b) Create a class called BankAccount that represents a bank account with balance and owner attributes. 
#Implement methods to deposit and withdraw money from the account.

class BankAccount:
    owner=str
    initial_balance=float

    def __init__(self,owner,initial_balance):
        self.owner=owner
        self.balance=initial_balance

    def saludar(self):
        print("Saludos dueño de cuenta: ",self.owner)

    def entrada_salida(self,deposito:float):
        if deposito <0:
            print("Esto es un retiro")
            self.balance +=deposito
        else:
           print("Esto es un deposito")
           self.balance +=deposito
       
        return self.balance
    
    def display_balance(self):
        print("Current balance: ",self.balance)


cuenta1=BankAccount("Santiago",0)
cuenta1.saludar()
monto=float(input("ingrese monto: "))
cuenta1.entrada_salida(monto)
cuenta1.display_balance()

    