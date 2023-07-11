#Implementing a deck of cards: You need to design and implement a class that represents a deck of cards. 
#This class should have methods for shuffling the deck and dealing a specific number of cards. Consider 
#using lists or arrays to represent the deck of cards.
import numpy as np
import random
picas=np.linspace(1,12,12)
corazon=np.linspace(1,12,12)
trebol=np.linspace(1,12,12)
diamante=np.linspace(1,12,12)
class Deck_cards:
    num_cards=int
    nom_baraja=list
    game=list

    def __init__(self,num_cards,nom_baraja,game):
        self.num_cards=num_cards
        self.nom_baraja=nom_baraja
        self.game=game

    def shuffle_deck(self):
       game=self.game
       juego=input("Ingrese juego a jugar: ")
       nom_baraja=self.nom_baraja
       juego=juego.upper()
       print(game)
       baraja={}
       if juego not in game: 
          print("Juego seleccionado no valido") 
       else:
         x,y=np.random.randint(1,12,2)
         for w in range(1,12,1):
            if x == w or y==w :
               baraja[random.choice(nom_baraja)]=w
         return baraja,juego
        
       
my_deck=Deck_cards(48,["Picas","Diamantes","Corazones","Treboles"],["POKER","BLACKJACK"])
baraja,juego=my_deck.shuffle_deck()
print("Su baraja es: ",baraja,"Para su juego: ",juego)
          

        
          
