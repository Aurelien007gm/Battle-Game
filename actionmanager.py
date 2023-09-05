from coremanager import CoreManager
from bot import Bot
from action import Action
from player import Player
class ActionManager:
    def __init__(self,bot = True):
        self.players = []
        self.bots =[]
        self.players.append(Player(**{"name":"Bot","id":0,"color":(0,0,255)}))
        self.players.append(Player(**{"name":"SuperBot","id":1,"color":(0,255,0)}))
        self.players.append(Player(**{"name":"ArnaudBot","id":2,"color":(255,0,0)}))
        self.players.append(Player(**{"name":"Aurélien","id":3,"color":(255,255,0)}))
        for i in range(3):
            self.bots.append(Bot(self.players[i],None))
        kwargs = {"players":self.players}
        self.cm = CoreManager(**kwargs)
        for bot in self.bots:
            bot.cm = self.cm
        

    """def Call(self,name,**kwargs):
        act = Action(name,**kwargs)
        self.cm.SetAction(act)"""
    def Call(self,act):
        self.cm.SetAction(act)

    def Run(self):
        for bot in self.bots:
            botAct = bot.GetAction()
            for act in botAct:
                self.cm.SetAction(act)
                act.print()
        self.cm.Run()

    def print(self):
        self.cm.print()



