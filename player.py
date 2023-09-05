import random as rd
from card import Card
class Player:

    def __init__(self,**kwargs):
        self.money = 5000
        self.name = kwargs.get("name") or "Unknown"
        self.id = kwargs.get("id") or 0
        self.cards = []
        for i in range(10):
            self.cards.append(Card())

    def AddMoney(self,nb):
        self.money+= nb

    def print(self):
        print("Player "+ self.name +" has " + str(self.money) )
        print("Player Cards are " )
        for c in self.cards:
            c.print()

    def DiscardCard(self,cost = None):
        self.cards.sort(key=lambda t:t.attack + t.defense)
        print("Discard card")
        self.cards[0].print()
        self.cards[0] = Card()
        print("Get ")
        self.cards[0].print()
        if(cost):
            self.money -= cost

    def DrawCard(self):
        i = rd.randint(0,9)
        card = self.cards[i]
        self.cards[i] = Card()
        self.cards.sort(key=lambda t:t.attack + t.defense)
        return(card)
    
class Animal(Player):

    def __init__(self,**kwargs):
        self.money = 0
        self.name = "animals"
        self.id = -1
        self.cards = []

    def AddMoney(self,nb):
        return

    def print(self):
        print("Animals")

    def DiscardCard(self,cost = None):
        return

    def DrawCard(self):
        return(Card())