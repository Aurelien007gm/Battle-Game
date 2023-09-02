from attackmanager import AttackManager
from territorymanager import TerritoryManager
from territory import Territory,TerritoryMultiple,TerritoryCard
from player import Player
import random as rd
import pygame
class CoreManager:

    def __init__(self):
        self.territory = []
        self.p1 = Player(**{"name":"Arnaud","id":0})
        self.p2 = Player(**{"name":"Aurélien","id":1})
        self.am = AttackManager()
        self.tm = TerritoryManager()
        self.INIT()

    def Deploy(self,territory:int,field,navy,para):
        t = self.tm.territories[territory]
        owner_id = t.owner_id
        if(owner_id == 0):
            owner = self.p1
        else:
            owner = self.p2
        t.Deploy(**{"field":field,"navy":navy,"para":para})
        price = {"field": 1000,"navy":1200,"para":1500}
        owner.AddMoney(-price["field"]*field)
        owner.AddMoney(-price["navy"]*navy)
        owner.AddMoney(-price["para"]*para)

    def Attack(self,t0,t1,way):
        T0 = self.tm.territories[t0]
        T1 = self.tm.territories[t1]
        self.am.Attack(**{"attacker":T0,"defender":T1,"way":way})
    def Transfer(self,t0,t1,field,navy,para):
        self.tm.Transfer(t0,t1,{"field":field,"navy":navy,"para":para})

    def SetOwner(self,t,p):
        if(p== 0):
            self.tm.territories[t].owner = self.p1
        else:
            self.tm.territories[t].owner = self.p2

    def DiscardCard(self,p):
        if(p==0):
            self.p1.DiscardCard(100)
        else:
            self.p2.DiscardCard(100)

        

    def EndTurn(self):
        for t in self.tm.territories:

            reward = t.value
            owner = t.owner_id
            if(owner == 0):
                self.p1.AddMoney(reward)
            else:
                self.p2.AddMoney(reward)
            t.EndTurn()

    def INIT(self):
        t = []
        fairness = 0
        for i in range(7):
            if(i== 3):
                terr = TerritoryMultiple(**{"name": "Moutain "+str(i),"id": i})
            elif(i==4):
                terr = TerritoryCard(**{"name": "Volcano "+str(i),"id": i})
            else:
                terr = Territory(**{"name": "Jungle "+str(i),"id": i})
            terr.owner_id = rd.randint(0,1)
            if(terr.owner_id)== 0:
                terr.owner = self.p1
            else:
                terr.owner = self.p2

            
            field = rd.randint(1,5)
            terr.troop["field"] = field
            fairness += (field*(terr.owner_id*2-1))
            t.append(terr)
        if(abs(fairness) > 2):
            return(self.INIT())
        print(fairness)
        t[6].value = 1000
        t[6].name = "Desert 6"
        self.tm.territories = t

    def print(self):
        self.p1.print()
        self.p2.print()

        for t in self.tm.territories:
            t.print()
