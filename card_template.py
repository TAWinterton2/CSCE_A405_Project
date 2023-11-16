#Base Class Template for Card
class Card:
    def __init__(self, cardName):
        self.cardName = cardName
        self.cardType = None
        self.description = None
        self.cardClass = None
        self.cardBlock = None
        self.cardAttack = None
        self.cardDiscript = None

    def printname(self):
        print(self.cardName)


class GenericActionCard(Card):
    def __init__(self, cardName, block):
        super().__init__(cardName)
        self.cardType = 'Action'
        self.cardClass = "Generic"

class GenericAttackActionCard(GenericActionCard):
    def __init__(self, cardName):
        super().__init__(cardName)
        self.cardtype = "Action Card - Attack"



    