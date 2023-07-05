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
    num_cards=48
    nom_baraja=["Picas","Diamantes","Corazones","Treboles"]
    game=str


    def __init__(self,num_cards,nom_baraja,game):
        self.num_cards=num_cards
        self.nom_baraja=nom_baraja
        self.game=game

    def shuffle_deck(self):
       game=self.game
       nom_baraja=self.nom_baraja
       game.upper()
       print(game)
       baraja={}
       if game is "POKER" or "BLACKJACK":
         x,y=np.random.randint(1,12,2)
         for w in range(1,12,1):
            if x == w or y==w :
               baraja[random.choice(nom_baraja)]=w
         return(baraja)
            
            
       if game is "VIUDA":
          return np.random.randint(1,56,5)
       
my_deck=Deck_cards(48,["Picas","Diamantes","Corazones","Treboles"],"Poker")
baraja=my_deck.shuffle_deck()
print("Su baraja es: ",baraja,"Para su juego: ",my_deck.game)
          

        
          

