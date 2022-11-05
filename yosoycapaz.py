import random
opciones=("piedra","papel","tijera")
user_wins=0
computadora_wins=0
rondas=0

while True:
    print("/"*10)
    print("RONDA",rondas)
    print("!"*10)

   
    user_option=input("Piedra, papel o tijera bobis: ")
    rondas +=1
    
    if user_option not in opciones:
        print("opcion no valida")
        break

    computadora_option=random.choice(opciones)

    print("computadora escogió",computadora_option)
    print("usuario escogió",user_option)


    if user_option==computadora_option:
        print("empate")
    elif user_option=="papel":
        if computadora_option=="piedra":
            print("gana usuario")
            user_wins +=1
        elif computadora_option=="tijera":
            print("gana computadora")
            computadora_wins +=1
    elif user_option=="piedra":
        if computadora_option=="tijera":
            print("gana usuario")
            user_wins +=1
        elif computadora_option=="papel":
            print("gana computadora")
            computadora_wins +=1
    elif user_option=="tijera":
        if computadora_option=="papel":
            print("gana usuario")
            user_wins +=1
        elif computadora_option=="piedra":
            print("gana computadora")
            computadora_wins +=1
    if user_wins== 2:
        print("ganamos papá")
        break
    
    if computadora_wins==2:
        print("perdió")
        break

            
            


