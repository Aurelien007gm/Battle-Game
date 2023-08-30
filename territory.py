from card import Card
class Territory:



    def __init__(self,**kwargs):
        self.name = kwargs.get("name") or "Plaine des abysses"
        self.id = kwargs.get("id") or 0
        self.owner = 0 # 0 is for animals
        self.troop = {"field":0,"navy":0,"para":0,"animals":0}

    
    def DrawCards(self,nb):
        cards = []
        for i in range(nb):
            card = Card()
            cards.append(card)
        return(cards)
    
    def LooseTroop(self,nb,compo):
        for i in range(nb):
            self.troop[compo[i]] -= 1
        return
    
    def GetCompo(self,way,isAttack = False):
        compo = []
        if(self.owner == 0):
            nb = min(2,self.troop["animals"])
            for i in range(nb):
                compo.append(["animals"])

        else:
            remaining = 3 if isAttack else 2
            d = {2:"field",1:"navy",0:"para"}
            for w in range(2,-1,-1):
                if(w <= way or not isAttack):
                    nb = min(remaining,self.troop[d[w]])
                    for i in range(nb):
                        compo.append(d[w])
                    remaining -= nb
            return(compo)



    
    def print(self):
        print("Territory " + self.name + " is owned by player number " +str(self.owner) + " and has :")
        print(self.troop)
