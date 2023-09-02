from attackmanager import AttackManager
from territorymanager import TerritoryManager
from territory import Territory,TerritoryMultiple,TerritoryCard
from player import Player
import random as rd
import pygame
class CoreManager:

    def __init__(self):
        self.territory = []
        self.players = []
        self.players.append(Player(**{"name":"Arnaud","id":0}))
        self.players.append(Player(**{"name":"Aurélien","id":1}))
        self.am = AttackManager()
        self.tm = TerritoryManager()
        self.INIT()

        self.actions = []

    def _Deploy(self,t:Territory,field,navy,para):
        owner = t.owner
        t.Deploy(**{"field":field,"navy":navy,"para":para})
        price = {"field": 1000,"navy":1200,"para":1500}
        owner.AddMoney(-price["field"]*field)
        owner.AddMoney(-price["navy"]*navy)
        owner.AddMoney(-price["para"]*para)

    def Deploy(self,**kwargs):
        territory = kwargs.get("territory")
        field = kwargs.get("field")
        navy = kwargs.get("navy")
        para = kwargs.get("para")
        price = {"field": 1000,"navy":1200,"para":1500}
        cost = price["field"]*field + price["navy"]*navy + price["para"]*para
        t = self.tm.territories[territory]
        money = t.owner.money
        if(cost > money):
            print("Attempted to buy to many troop")
            return
        self._Deploy(t,field,navy,para)


    def _Attack(self,t0:Territory,t1:Territory,way):
        self.am.Attack(**{"attacker":t0,"defender":t1,"way":way})

    def Attack(self,**kwargs):
        """Check if: the owner of the two territories are different
        The territory are adjacent
        The attackant have at least one troop available
        """
        t0 = kwargs.get("t0")
        t1 = kwargs.get("t1")
        attacker = self.tm.territories[t0]
        defender = self.tm.territories[t1]
        if(attacker.owner_id == defender.owner_id):
            print("Tried to attack from ally territories")
            return
        
        way = self.tm.adjacent[t0,t1]
        if(not attacker.CanBattle(way)):
            return
        self._Attack(attacker,defender,way)
        return
    
    def Transfer(self,**kwargs):
        """Check if: the owner of the two territories are different
        The territory are adjacent
        The attackant have at least one troop available
        """

        t0 = kwargs.get("t0")
        t1 = kwargs.get("t1")
        field = kwargs.get("field")
        navy = kwargs.get("navy")
        para = kwargs.get("para")
        way = 2
        if(navy > 1):
            way = 1
        if(para> 1):
            way = 0
        kwargs = {"t0":t0,"t1":t1,"way":way,"compo":{"field":field,"navy":navy,"para":para}}
        possible = self.tm.TransferPossible(**kwargs)
        if(possible):
            self._Transfer(t0,t1,field,navy,para)
        else:
            print("Transfer was not possible ?")
        return



    def _Transfer(self,t0,t1,field,navy,para):
        self.tm.Transfer(t0,t1,{"field":field,"navy":navy,"para":para})

    def SetOwner(self,t,p):
        self.tm.territories[t].owner = self.players[p]

    def _DiscardCard(self,p):
        self.players[p].DiscardCard(100)

    def DiscardCard(self,**kwargs):
        player = kwargs.get("player")
        cost = 100
        p = self.player[p]
        money = p.owner.money
        if(cost > money):
            print("Attempted to buy to discard card while not enough money")
            return
        self._DiscardCard(p)

    def EndTurn(self):
        for t in self.tm.territories:

            reward = t.value
            owner = t.owner
            owner.AddMoney(reward)
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
            terr.owner = self.players[terr.owner_id] 

            
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
        self.players[0].print()
        self.players[1].print()

        for t in self.tm.territories:
            t.print()

    def SetAction(self,action):
        self.actions.append(action)

    def Run(self):
        self.actions.sort(key = lambda t:t.value)
        action_dict = {"Attack":self.Attack,"Deploy":self.Deploy,"Transfer":self.Transfer,"DiscardCard":self.DiscardCard}
        for action in self.actions:
            func = action_dict.get(action.name)
            func(**action.args)
        self.actions = []
        self.EndTurn()



    