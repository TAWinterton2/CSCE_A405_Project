import random

#deck Template
class deck():
    def __init__(self):
        self.decklist = []

    def constructDeck(self, list):
        self.decklist = list
        return print("Deck Constructed")
    

    def drawCard(self):
        return self.decklist.pop()
    
    def shuffle(self):
        random.shuffle(self.decklist)

    def printDeckList(self):
        for x in len(self.decklist):
            return self.decklist[x]


#Player Template

class player():
    def __init__(self):
        self.hand = []
    
    def draw(self, deck):
        while len(self.hand) < 4:
            self.hand.append(deck.drawCard())
        return self

