import random
import functools
def user1():
    dado_1=random.randint(1,6)
    dado_2=random.randint(1,6)
    res1=[]
    res1.extend([dado_1,dado_2])
    sum1=functools.reduce(lambda contador,x:contador+x,res1)
    print("user1:",res1,"suma es",sum1)
    return sum1

def user2():
    dado_1=random.randint(1,6)
    dado_2=random.randint(1,6)
    res2=[]
    res2.extend([dado_1,dado_2])
    sum2=functools.reduce(lambda contador,x:contador+x,res2)
    print("user2:",res2,"suma es",sum2)
    return sum2

def check_winner():
    sum1=user1()
    sum2=user2()
    if sum1>sum2:
        print("Dado mayor gana user1 con: ",sum1)
        exit()
    elif sum1==sum2:
        print("Empate! Tire otra vez")
        check_winner()
        exit()
    elif sum2>sum1:
        print("Dado mayor gana user2 con: ",sum2)
        exit()

def run():
    check_winner()

run()

    

