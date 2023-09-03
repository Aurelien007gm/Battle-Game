from player import Player
from coremanager import CoreManager
from action import Action
import random as rd

class Bot:
    N_TERRITORY = 7
    def __init__(self,p:Player,cm:CoreManager):
        self.player = p
        self.cm = cm

    def GetAction(self):
        # First we get deployment
        act = []
        terr = self.cm.GetTerritory(self.player.id)
        money = self.player.money
        price = {"field": 1000,"navy":1200,"para":1500}
        troopToDeploy = {"field": 0,"navy":0,"para":0}
        if(terr):
            randomterr = rd.choice(terr).id
            troopToDeploy["territory"] = randomterr
            while(money > 1500):
                troop,value = rd.choice(list(price.items()))
                troopToDeploy[troop] += 1
                money-= value

            act.append(Action("Deploy",**troopToDeploy))

            randomterrAttack = rd.choice(terr).id
            randomterrDef = rd.choice(self.cm.tm.territories).id
            act.append(Action("Attack",t0 = randomterrAttack,t1 = randomterrDef))
        return(act)
        
        
                

