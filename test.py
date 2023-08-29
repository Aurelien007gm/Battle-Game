from data.map import MapData
from territory import Territory
from attackmanager import AttackManager

def test():
    data = MapData

def main():
    print("====Début du test====")
    t0 = Territory(**{"name": "Jungle Maléfique","id": 1})
    t1 = Territory(**{"name": "Brousse argente","id": 2})
    t0.troup = ({"field":5,"navy":1,"para":0,"animal":0})
    t1.troup = ({"field":4,"navy":1,"para":0,"animal":0})
    t0.print()
    t1.print()
    att = AttackManager()
    att.wave(**{"attacker":t0,"defender":t1,
              "attackcompo":["field","field","field"],"defensecompo":["field","field"]})

    t0.print()
    t1.print()

main()