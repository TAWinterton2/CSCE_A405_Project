
#Base Class Template for Card
class Card:
    def __init__(self, cardName):
        self.cardName = cardName
        self.description = None
        self.type = None
        

    # Debugging Functions
    def printname(self):
        print(self.cardName)
    def printDescription(self):
        print(self.description)

#Generic Card Template

class GenericAction(Card):
    def __init__(self, cardName, pitch, block, goAgian):
        super().__init__(cardName)
        self.block = block
        self.pitch = pitch 
        self.goagian = bool(goAgian)
        self.type = "Generic Action"


    # Debugging Functions
    def printblock(self):
        print(self.block)

    def printgoAgain(self):
        print(self.goagian)
    
    def printPitch(self):
        print(self.pitch)

class GenericAttackAction(GenericAction):
    def __init__(self, cardName, pitch, attack, block, goAgian):
        super().__init__(cardName, pitch, block, goAgian)
        self.attack = attack
        self.type = "Generic Action - Attack"
    def printAttack(self):
        print(self.attack)

#Class card template 

#Ninja Card Template
class NinjaAttackAction(GenericAttackAction):
    def __init__(self, cardName, pitch, attack, block, goAgian):
        super().__init__(cardName, pitch, attack, block, goAgian)
        self.type = "Ninja Action - Attack"

        

        






    