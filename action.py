class Action:

    def  __init__(self,name,**kwargs):
        self.name = name
        self.args = kwargs
        self.value = self.GetValue()

    def GetValue(self):
        dictionnary = {"Deploy":1,"Discard":1,"Transfer":2,"Attack":3}
        get = dictionnary.get(self.name) or 5
        return(get)

    
