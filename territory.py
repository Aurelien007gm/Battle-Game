from card import Card
class Territory:



    def __init__(self,**kwargs):
        self.name = kwargs.get("name") or "Plaine des abysses"
        self.id = kwargs.get("id") or 0
        self.owner = 0 # 0 is for animals
        self.troup = {"field":0,"navy":0,"para":0,"animals":0}

    
    def DrawCards(self,nb):
        cards = []
        for i in range(nb):
            card = Card()
            cards.append(card)
        return(cards)
    
    def LooseTroop(self,nb,compo):
        for i in range(nb):
            self.troup[compo[i]] -= 1
        return
    
    def print(self):
        print("Territory " + self.name + " is owned by player number " +str(self.owner) + " and has :")
        print(self.troup)
