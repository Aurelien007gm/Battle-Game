from data.map import MapData
from territory import Territory
from attackmanager import AttackManager

def test():
    data = MapData

def testWave():
    print("====Début du test====")
    t0 = Territory(**{"name": "Jungle Maléfique","id": 1})
    t1 = Territory(**{"name": "Brousse argente","id": 2})
    t0.troop = ({"field":5,"navy":1,"para":0,"animal":0})
    t1.troop = ({"field":4,"navy":1,"para":0,"animal":0})
    t0.print()
    t1.print()
    att = AttackManager()
    att.wave(**{"attacker":t0,"defender":t1,
              "attackcompo":["field","field","field"],"defensecompo":["field","field"]})

    t0.print()
    t1.print()

def testCompo():
    t0 = Territory(**{"name": "Jungle Maléfique","id": 1})
    t0.owner = 1
    t0.troop = ({"field":1,"navy":1,"para":1,"animal":0})
    compo = t0.GetCompo(2,True)
    print(compo == ["field","navy","para"])
    compo = t0.GetCompo(1,True)
    print(compo == ["navy","para"])
    compo = t0.GetCompo(0,True)
    print(compo == ["para"])

    t0.troop = ({"field":2,"navy":1,"para":2,"animal":0})
    compo = t0.GetCompo(2,True)
    print(compo == ["field","field","navy"])
    compo = t0.GetCompo(1,True)
    print(compo == ["navy","para","para"])
    compo = t0.GetCompo(0,True)
    print(compo == ["para","para"])



def main():
    testWave()
    testCompo()
main()