from card import Card
from player import Player,Animal
import random as rd
class Territory:



    def __init__(self,**kwargs):
        self.name = kwargs.get("name") or "Plaine des abysses"
        self.id = kwargs.get("id") or 0
        self.animals = kwargs.get("animals")
        self.owner = None
        self.owner_id =-1 # -1 is for animals
        self.owner_name="None"
        self.troop = {"field":0,"navy":0,"para":0,"animals":0}
        self.value = kwargs.get("value") or 500
        self.hasbeentaken = False
        self.hasAttacked = False
        self.effect = "This territory has no effect"
        self.maxTroopAttack = 3
        self.baseMaxTroopAttack = 3
        self.baseMaxTroopDefense = 2
        self.maxTroopDefense = 2
    
    def SetMaxTroop(self, hasContinent = False):
        self.maxTroopAttack = self.baseMaxTroopAttack
        self.maxTroopDefense = self.baseMaxTroopDefense
        print("???")
        if(hasContinent):
            self.maxTroopDefense += 1
            print("Hey, someone have this continent")
        else:
            print("No one has this continent")
        return

    def ShowEffect(self):
        print(self.effect)

    
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
            print(compo[i])
            self.troop[compo[i]] -= 1
        return
    
    def GetCompo(self,way,isAttack = False):
        compo = []
        if(self.owner_id == -1):
            nb = min(self.troop["animals"],2)
            for i in range(nb):
                compo.append("animals")

        else:
            remaining = self.ComputeMaxTroop(isAttack)
            if(isAttack):
                maximum = self.CountTroop()-1
                remaining = min(remaining,maximum)
            d = {2:"field",1:"navy",0:"para"}
            for w in range(2,-1,-1):
                if(w <= way or not isAttack):
                    nb = min(remaining,self.troop[d[w]])
                    for i in range(nb):
                        compo.append(d[w])
                    remaining -= nb
        return(compo)
    
    def ComputeMaxTroop(self,isAttack):
        remaining = self.maxTroopAttack if isAttack else self.maxTroopDefense
        return(remaining)
        
        
    def CanBattle(self,way,isAttack = True):
        d = {2:"field",1:"navy",0:"para"}
        globalCount = 0
        if(self.hasbeentaken):
            return(False)
        if self.owner_id == -1:
            nb = self.troop["animals"]
            globalCount = nb
        else:
            nb = 0
            for w in range(3):
                globalCount+= self.troop[d[w]]
                if(w<= way or not isAttack):
                    nb+= self.troop[d[w]]

        return(nb>0 and (globalCount>1 or not isAttack))
    
    def CountTroop(self):
        d = {2:"field",1:"navy",0:"para",-1:"animals"}
        nb = 0
            
        for w in range(-1,3):
            nb+= self.troop[d[w]]
        return(nb)
    
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
        self.hasbeentaken = True
        self.SetOwner(newOwner)
    
    def print(self):
        print("Territory " + self.name + " is owned by player number " +str(self.owner.name) + " and has :" + str(self.troop))
        #print(self.troop)

    def EndTurn(self):
        self.hasbeentaken = False
        self.maxTroopAttack = 3
        self.maxTroopDefense = 2
        if(self.owner_id != -1 and self.CountTroop() <= 1):
            if(rd.random() < 0.15):
                self.Uprise()
        elif(self.owner_id == -1):
            self.Regenerate()
        return

    def Uprise(self):
        print("Uprise of the animals on territory" + self.name)
        self.owner = self.animals
        self.owner_id = -1
        self.owner_name = "animals"
        self.troop = {"field":0,"navy":0,"para":0,"animals":3}

    def Regenerate(self):
        self.troop = {"field":0,"navy":0,"para":0,"animals":3}

class TerritoryMultiple(Territory):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.effect ="Reward is multiplied by 1.05 each turn. Reset when owner changes"
      
    def SetOwner(self,p:Player):
        super().SetOwner(p)
        self.value = 500

    def EndTurn(self):
        self.value = int(self.value*1.05)
        super().EndTurn()

class TerritoryCard(Territory):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.effect ="Discard the worst card of the owner and draw another card each turn"

    def EndTurn(self):
        super().EndTurn()
        self.owner.DiscardCard()
        
class TerritoryGorilla(Territory):

        def __init__(self,**kwargs):
            super().__init__(**kwargs)
            self.effect ="If no attack from this territory, 20percent of adding a bonus troop at the end of the turn"
        
        def EndTurn(self):
            print("Bonus troop on gorilla territory")
            if(not self.hasAttacked and rd.random()< 0.2 and self.owner !=-1):
                self.Deploy(field = 1)
            super().EndTurn()

class TerritoryAlpaga(Territory):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.effect ="No uprise of animals on this territory"
        
    def EndTurn(self):
        self.hasbeentaken = False
        return
        
class TerritoryCoati(Territory):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.effect ="Uprise can happens if troop are less or equal to 4"
        
    def EndTurn(self):
        self.hasbeentaken = False
        if(self.owner_id != -1 and self.CountTroop() <= 4):
            if(rd.random() < 0.15):
                self.Uprise()
        elif(self.owner_id == -1):
            self.Regenerate()
        return

class TerritoryYack(Territory):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.value = 1000
        self.effect ="Reward is twice the normal price"

class TerritoryElephant(Territory):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.effect ="35 percent to attack with one more card"

    def SetMaxTroop(self, hasContinent = False):
        super().SetMaxTroop(hasContinent)

        if(rd.random() <= 0.35):
            self.maxTroopAttack += 1 
        return
        

