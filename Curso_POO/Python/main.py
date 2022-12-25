from car import Car
from account import Account
from user import User
from uberX import UberX
from driver import Driver


if __name__=="__main__":
    print("sapo pa")
    uberx=UberX("EZS32F",Account("Oreo","1053869189"),"Chevrolet","Spark")
    uberx.set_passenger()
    print(vars(uberx.driver),vars(uberx))
    user=User(Account("OREO2","123456789"))
    print(vars(user.name),vars(user.document))
    driver=Driver(Account("OREO3","123455589"))
    print(vars(driver.name),vars(driver.document))