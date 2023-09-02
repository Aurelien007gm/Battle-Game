from card import Card
from player import Player
class Territory:



    def __init__(self,**kwargs):
        self.name = kwargs.get("name") or "Plaine des abysses"
        self.id = kwargs.get("id") or 0
        self.owner = None
        self.owner_id =-1 # -1 is for animals
        self.owner_name="None"
        self.troop = {"field":0,"navy":0,"para":0,"animals":0}
        self.value = kwargs.get("value") or 500


    
    def DrawCards(self,nb):
        cards = []
        """for i in range(nb):
            card = Card()
            cards.append(card)"""
        
        for i in range(nb):
            card = self.owner.DrawCard()
            cards.append(card)
        return(cards)
    
    def LooseTroop(self,nb,compo):
        for i in range(nb):
            self.troop[compo[i]] -= 1
        return
    
    def GetCompo(self,way,isAttack = False):
        compo = []
        if(self.owner_id == -1):
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
        
    def CanBattle(self,way,isAttack):
        d = {2:"field",1:"navy",0:"para"}
        if self.owner_id == -1:
            nb = self.troop["animals"]
        else:
            nb = 0
            for w in range(3):
                if(w<= way or not isAttack):
                    nb+= self.troop[d[w]]
            print(nb)
        return(nb>0)
    
    def Deploy(self,**kwargs):
        for kind,value in kwargs.items():
            self.troop[kind] +=value
        return
    
    def SetOwner(self,p:Player):
        self.owner = p
        self.owner_id = p.id
        self.owner_name = p.name

    def Conquest(self,**kwargs):
        newOwner = kwargs.get("attacker").owner
        self.SetOwner(newOwner)
    
    def print(self):
        print("Territory " + self.name + " is owned by player number " +str(self.owner.name) + " and has :" + str(self.troop))
        #print(self.troop)

    def EndTurn(self):
        return


class TerritoryMultiple(Territory):
        def __init__(self,**kwargs):
            super().__init__(**kwargs)

        def SetOwner(self,p:Player):
            super.SetOwner(p)
            self.value = 500

        def EndTurn(self):
            self.value = int(self.value*1.3)

class TerritoryCard(Territory):
        def __init__(self,**kwargs):
            super().__init__(**kwargs)

        def EndTurn(self):
            self.owner.DiscardCard()
        

        
