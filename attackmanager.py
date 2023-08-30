from territory import Territory

class AttackManager:


    def wave(self,**kwargs):
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
        for card in attackCards:
            card.print()
        for card in defenseCards:
            card.print()

        for i in range(nbAttack):
            attack = attackCards[i].attack
            defense = defenseCards[i].defense
            if(attack <= defense):
                attackerLoss += 1
            else:
                defenderLoss += 1
        attacker.LooseTroop(attackerLoss,attackcompo)
        defender.LooseTroop(defenderLoss,defensecompo)

