import numpy as np
class TerritoryManager:

    def __init__(self):
        self.territories = []
        self.nb_territory = len(self.territories)
        
        self.connectivity = np.array((len(self.territories),len(self.territories)))

    def GetConnectedMatrix(self,player:int):
        new = np.zeros((self.nb_territory,self.nb_territory))
        for i in range(self.nb_territory):
            for j in range(self.nb_territory):
                if ((self.territories[i].owner == player) and (self.territories[j].owner == player)):
                    new[i,j] = self.connectivity[i,j]

        nbIter = self.CountTerritory(player)
        playerTerritories = self.GetPlayerTerritories(player)

        for i in range (nbIter):
            old = np.copy(new)
            new = np.zeros((self.nb_territory,self.nb_territory))

            for t0 in playerTerritories:
                for t1 in playerTerritories:
                    for tinter in playerTerritories:
                        val = max(old[t0,t1],min(old[t0,tinter],old[tinter,t1])) 
                        new[t0,t1] = max(val,new[t0,t1])
            print(new)
            print("===")

        return(new)



    def CountTerritory(self,player:int):
        count:int  = 0
        for territory in self.territories:
            if territory.owner == player:
                count+=1
        return(count)
    
    def GetPlayerTerritories(self,player:int):
        res = []
        for territory in self.territories:
            if territory.owner == player:
                res.append(territory.id)
        return(res)

