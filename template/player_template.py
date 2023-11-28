#Player Template
from card import card_template

class player():
    def __init__(self):
        self.hand = []
        self.handsize = 4
        print("Player has joined the game\n ")
    
    def draw(self, deck):
        while len(self.hand) < self.handsize:
            self.hand.append(deck.drawCard())
        print("New hand drawn: ")
        return self
    
    def showHand(self):
        for card in self.hand:
            card.show()
