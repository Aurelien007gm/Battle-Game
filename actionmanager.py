from coremanager import CoreManager
from action import Action
class ActionManager:
    def __init__(self):
        self.cm = CoreManager()

    def Call(self,name,**kwargs):
        act = Action(name,**kwargs)
        self.cm.SetAction(act)

    def Run(self):
        self.cm.Run()

    def print(self):
        self.cm.print()



