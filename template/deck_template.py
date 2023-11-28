import random
from card import card_template

#deck Template
class deck():
    def __init__(self):
        self.decklist = []

    def constructDeck(self, list):
        self.decklist = list
        return print("Deck Constructed!")
    

    def drawCard(self):
        return self.decklist.pop()
    
    def shuffle(self):
        random.shuffle(self.decklist)
        return print("Deck shufffled")

    def printDeckList(self):
        for x in len(self.decklist):
            return self.decklist[x]
        
    def show(self):
        for x in self.decklist:
            x.show()

