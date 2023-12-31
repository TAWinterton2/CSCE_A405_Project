
#Base Class Template for Card
class Card:
    def __init__(self, cardName):
        self.cardName = cardName
        self.description = None
        self.type = None
        
    def __str__(self):
        return f"Card(Name: {self.cardName})"

    # Debugging Functions
    def printname(self):
        print(self.cardName)
    def printDescription(self):
        print(self.description)
      
#Generic Card Template

class GenericAction(Card):
    def __init__(self, cardName, pitch, cost, block, go_again ):
        super().__init__(cardName)
        self.block = block
        self.pitch = pitch 
        self.go_again = bool(go_again)
        self.cost = cost
        self.type = "Generic Action"
    
    def __str__(self):
        return f"Generic Attack Action(Name: {self.cardName}, Cost: {self.cost}, Pitch: {self.pitch}, Attack: {self.attack}, Block: {self.block}, Go Again: {self.go_again})"

    
    def show(self):
        return print("{} Cost:{} Pitch:{} Attack:{} Block:{}")




    # Debugging Functions
    def printblock(self):
        print(self.block)

    def printgoAgain(self):
        print(self.go_again)
    
    def printPitch(self):
        print(self.pitch)

    

class GenericAttackAction(GenericAction):
    def __init__(self, cardName, pitch, cost, attack, block, go_again):
        super().__init__(cardName, pitch, cost, block, go_again)
        self.attack = attack
        self.type = "Generic Action - Attack"

    def __str__(self):
        return f"Generic Action(Name: {self.cardName}, Cost: {self.cost}, Pitch: {self.pitch}, Attack: {self.attack} Block: {self.block}, Go Again: {self.go_again})"

    def show(self):
        return print("{}: \n Cost:{} Pitch:{} Attack:{} Block:{}".format(self.cardName, self.cost, self.pitch, self.attack, self.block))

    #Debugging Functions    
    def printAttack(self):
        print(self.attack)
   
#Class card template 

#Ninja Card Template
class NinjaAttackAction(GenericAttackAction):
    def __init__(self, cardName, pitch, cost, attack, block, go_again):
        super().__init__(cardName, pitch, cost, attack, block, go_again)
        self.type = "Ninja Action - Attack"

    def __str__(self):
        return f"Ninja Attack Action(Name: {self.cardName}, Cost: {self.cost}, Pitch: {self.pitch}, Attack: {self.attack}, Block: {self.block}, Go Again: {self.go_again})"
    
    
    def show(self):
        return print("{}: \n Cost:{} Pitch:{} Attack:{} Block:{}".format(self.cardName, self.cost, self.pitch, self.attack, self.block))

        

        






    