class Continent :

    def __init__(self,**kwargs):
        self.continent = {0:[0,1,2],1:[3,4,5,6,7],2:[8,9,10,11]}
        self.tm = kwargs.get("tm")


    def Reward(self):
        for continent, territories in self.continent.items():
            owner = self.tm.territories[territories[0]].owner_id
            owned = (owner>= 0)
            for t in territories:
                if(self.tm.territories[t].owner_id != owner):
                    owned = False
            
            if(owned):
                self.tm.territories[territories[0]].owner.AddMoney(1000)
            
