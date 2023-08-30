from territory import Territory
from debug import DEBUG

class AttackManager:


    def Wave(self,**kwargs):
        attacker : Territory = kwargs.get("attacker")
        defender : Territory = kwargs.get("defender")
        attackcompo : list = kwargs.get("attackcompo")
        defensecompo :list  = kwargs.get("defensecompo")


        nbAttacker : int = len(attackcompo)
        nbDefender : int = len(defensecompo)
        nbAttack = min(nbAttacker,nbDefender)

        attackerLoss = 0
        defenderLoss = 0

        attackCards : list =attacker.DrawCards(nbAttacker)
        attackCards.sort(key =lambda x: x.attack,reverse = True)
        defenseCards: list =defender.DrawCards(nbDefender)
        defenseCards.sort(key= lambda x: x.defense,reverse = True)

        if(DEBUG):
            for card in attackCards:
                card.print()
            print("====")
            for card in defenseCards:
                card.print()

        for i in range(nbAttack):
            attack = attackCards[i].attack
            defense = defenseCards[i].defense
            if(attack <= defense):
                attackerLoss += 1
            else:
                defenderLoss += 1
        kwargs["attackerLoss"] = attackerLoss
        kwargs["defenderLoss"] = defenderLoss
        attacker.LooseTroop(attackerLoss,attackcompo)
        defender.LooseTroop(defenderLoss,defensecompo)
        return(kwargs)

    def Attack(self,**kwargs):
        attacker : Territory = kwargs.get("attacker")
        defender : Territory = kwargs.get("defender")
        way: int = kwargs.get("way")

        maxIter: int = 10
        iteration = 0
        while attacker.CanBattle(way,True) and defender.CanBattle(way,False) and iteration  <maxIter:
            if(DEBUG):
                attacker.print()
                defender.print()

            kwargs["attackcompo"] = attacker.GetCompo(way,True)
            kwargs["defensecompo"] = defender.GetCompo(way,False)
            kwargs = self.Wave(**kwargs)
            iteration += 1

        if(DEBUG):
            attacker.print()
            defender.print()






