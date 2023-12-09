#Player Template
from card import card_template

class player():
    def __init__(self):
        self.hand = []
        self.handsize = 4
        self.pitchzone = []
        self.resources = 0
        self.playedcards = []
        print("Player has joined the game\n ")
    
    def draw(self, deck):
        while len(self.hand) < self.handsize:
            self.hand.append(deck.drawCard())
        print("New hand drawn: ")
        return self
    
    def pitch(self, cardname):
        index = cardname
        try:
            self.resources += index.pitch
            self.pitchzone.append(self.hand.pop(index))

        except:
            print("Error trying to pitch card")
    
    def showHand(self):
        for card in self.hand:
            card.show()

    def showPitch(self):
        for card in self.pitchzone:
            card.show()
